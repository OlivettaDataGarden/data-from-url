"""
Module to define JSONConvertor class for the get_data module
"""
from json.decoder import JSONDecodeError

from errors.error import ListErrors
from requests.exceptions import InvalidJSONError

from ..settings.dataclass import GetDataResponse
from .abstract_convertor import AbstractConvertor, AllConvertors


class JSONConvertor(AbstractConvertor):
    """Class to add JSON as a dict to the GetDataResponse tuple
    """

    convertor_name = 'JSON'

    @classmethod
    def _result_with_data_field(
        cls, result: GetDataResponse, _=None
    ) -> GetDataResponse:
        """
        Extracts the JSON from the response and adds it to the results data
        field. If no proper JSON can be retrieved from response object in
        `result` argument the status of result is set to invalid and an error
        code is added.

        Args:
            result (GetDataResponse): result from API call

        Returns:
            [GetDataResponse]: new GetDataResponse with data field or status
                               and error field updated
        """
        response = result.response
        io_time = result.io_time
        try:
            data = response.json()
            return GetDataResponse(
                response=response, is_valid=True, error_msg=[], data=data,
                io_time=io_time)

        except (InvalidJSONError, JSONDecodeError):
            return GetDataResponse(
                response=response, is_valid=False, data=None,
                error_msg=[ListErrors.INVALID_JSON_IN_RESPONSE],
                io_time=io_time)


AllConvertors.register_convertor(JSONConvertor)
