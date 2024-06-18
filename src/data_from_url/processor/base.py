from typing import Counter, Iterator, Optional, Union

from pydantic import BaseModel, Field

from ..settings.dataclass import GetDataResponse


class DictsStats(BaseModel):
    path: str = ""
    count: int = 0
    fields: list[str] = Field(default_factory=list)
    record_example: dict = Field(default_factory=dict)


def key_is_list_reference(partial_path: str) -> bool:
    if not partial_path:
        # partial path can be ''
        return False
    if partial_path[0] == "[" and partial_path[-1] == "]":
        try:
            int(partial_path[1:-1])
            return True
        except ValueError:
            return False

    return False


def get_list_index(partial_path: str) -> int:
    if not key_is_list_reference(partial_path):
        raise ValueError(f"partial path {partial_path} is not a list reference.")
    return int(partial_path[1:-1])


def split_path(path: str):
    nested_keys = path.split(".")
    before = ""
    list_reference_int = None
    after = ""

    list_reference_processed = False

    for key in nested_keys:
        if list_reference_processed:
            after = (".").join([after, key]) if after else key
            continue

        if key_is_list_reference(key):
            list_reference_int = get_list_index(key)
            list_reference_processed = True
            continue

        before = (".").join([before, key]) if before else key

    return (before, list_reference_int, after)


class DataResponseProcessor:
    """
    This class is aimed to provide suggestions to get the correct list of records form
    an API response object.

    It takes a GetDataResponse and if valid it provides the following methods

    - get_repsonse_content_stats:
        A list with a DictStat for each list of dictionaries in the response.
        Returns None if GetDataResponse in not valid
        A DictStat contains the following fields
            path: str
                - the path to the list of dicts in the response
                  nested paths divided by `.` for next keys and `[i]` for nested
                  list. i.e. field1.[1].field2 means take value in of field1 which
                  should be a list. Take the list entry of index 1 which should be
                  a dict and take the value for for field2
            count: int
                - the number of records in the given list
            fields: list[str]
                - the fields found in that record (for now only top level fields)
            record_example: dict
                - 1ste record in the list



    """

    def __init__(self, data_response: GetDataResponse):
        self._data_response = data_response
        self._lists_with_dict_stats: list[DictsStats] = []

    def __bool__(self) -> bool:
        """
        Returns true only if the data_response has a valid GetDataResponse object.
        """
        return self._data_response.is_valid is True

    def get_repsonse_content_stats(self) -> Optional[list[DictsStats]]:
        if not self:
            return None
        self._find_lists_with_dicts_in_data()
        return sorted(self._lists_with_dict_stats, key=lambda x: x.count, reverse=True)

    def _find_lists_with_dicts_in_data(self, data=None, path=""):
        if not self._data_response.is_valid:
            raise ValueError("Not a valid data repsonse")

        if not data:
            data = self._data_response.data

        if isinstance(data, list):
            dicts_in_list = [item for item in data if isinstance(item, dict)]
            if dicts_in_list:
                fields = set()

                for _dict in dicts_in_list:
                    fields.update(self._get_nested_fields_from_dict(_dict))

                self._lists_with_dict_stats.append(
                    DictsStats(
                        path=path,
                        count=len(data),
                        fields=list(fields),
                        record_example=dicts_in_list[0],
                    )
                )

            for index, item in enumerate(data):
                if isinstance(item, (dict, list)):
                    self._find_lists_with_dicts_in_data(
                        data=item, path=f"{path}.[{index}]"
                    )

        elif isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, (dict, list)) and value:
                    new_path = f"{path}.{key}" if path else key
                    self._find_lists_with_dicts_in_data(data=value, path=new_path)

    def _get_nested_fields_from_dict(self, input_dict: dict) -> set[str]:
        """
        Return a set of key names as str from a dict including nested dicts.
        Will not return keys for dicts that are stored in lists with a dict value

        """
        fields: set = set()
        fields.update(input_dict.keys())
        for key, value in input_dict.items():
            if isinstance(value, dict):
                nested_fields_from_value = self._get_nested_fields_from_dict(value)
                fields.update(
                    [key + "." + nested_key for nested_key in nested_fields_from_value]
                )

        return fields

    def _count_values(
        self, data: Union[dict, list], counter: Optional[Counter] = None
    ) -> Counter:
        if counter is None:
            counter = Counter()

        if isinstance(data, dict):
            for value in data.values():
                self._count_values(value, counter)
        elif isinstance(data, list):
            for item in data:
                self._count_values(item, counter)
        else:
            counter[data] += 1

        return counter

    def _get_nested_field_from_data(self, path: str, from_dict=None):
        """
        Return the value of a nested item in the data based upon the path defined in
        the _find_lists_with_dicts_in_data method.
        """
        nested_keys = path.split(".")
        result = from_dict or self._data_response.data
        for key in nested_keys:
            if not isinstance(result, (dict, list)):
                raise KeyError(f"path: {path} is not existing")
            if key[0] == "[" and key[-1] == "]":
                if not isinstance(result, (dict, list)):
                    raise ValueError(
                        f"For {key} in {path} list was expected but received dict"
                    )
                result = result[get_list_index(key)]
            elif isinstance(result, dict):
                result = result.get(key)
            else:
                raise ValueError(
                    f"Expected a dict for {key} in {path} but received list"
                )

            if not result:
                raise ValueError(f"No value found for {key} in {path}")

        return result

    def suggest_record_conversions_for_list_records_retrieval(self, path):
        """
        Suggest record convertor settings for conversion of a list of dicts where
        a single dict is needed in for the actual data.

        So
        {"values": [
            {"v1":"name1", "content": data object}
            {"v2":"name2", "content": data object we are looking for}
        ]}

        with path values[1]content refering to the field `content` in
        {"v2":"name2", "content": data object we are looking for}

        should become

        {"values":
            {"v2":"name2", "content": data object we are looking for}
        ]}

        so that we can lookup our data with key
            values.content

        for this the following conversion is to be generated

        "$convert1": {
            "fieldname": "values",
            "actions": [{"select_object_from_list": ["v2", "name2"]}],
        },

        this convertor resets the values value to the first item in its original list
        that has an dict key-value {"v2": "name2"}

        Args:
            path (_type_): _description_
        """
        before_key, list_reference_key, after_key = split_path(path)

        if not list_reference_key:
            # path contains not list references so no conversion needed
            return {"list_of_records": {"$full_record": {}}}

        list_with_target_dict = self._get_nested_field_from_data(before_key)
        if not list_with_target_dict:
            raise ValueError(f"No object found in data for path {before_key}")

        if not isinstance(list_with_target_dict, list):
            raise ValueError(f"Object for path {before_key} is not a list")

        target_dict = list_with_target_dict.pop(list_reference_key)
        # rename list for better readibility
        list_without_target_dict = list_with_target_dict

        if not isinstance(target_dict, dict):
            raise TypeError(
                f"Target in list for path {before_key} is of type {type(target_dict)}"
                " but should be dict"
            )

        # remove target key, value from dict so that remaining key value pairs can be
        # evaluted and checked if tehy can be used for selection purpose
        target_dict.pop(after_key.split(".")[0])

        for key in target_dict.keys():
            target_value = target_dict.get(key, None)
            values_for_same_key = [
                _dict.get(key, None) for _dict in list_without_target_dict
            ]
            if target_value and target_value not in values_for_same_key:
                result = [key, target_value]
                continue
        return {
            "$convert1": {
                "fieldname": before_key,
                "actions": [{"select_object_from_list": result}],
            },
            "list_of_records": before_key + "." + after_key,
        }
