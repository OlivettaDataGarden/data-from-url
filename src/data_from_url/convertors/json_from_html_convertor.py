"""
Module to define JSONConvertor class for the get_data module
"""

import json
import urllib
from typing import Optional

from errors.base import add_error_data
from errors.error import ListErrors

from ..settings.dataclass import GetDataResponse
from ..settings.enumerator import GetDataExceptions
from ..settings.settings import CONVERTOR_PARAMS_JSON_FROM_HTTP
from .abstract_convertor import AbstractConvertor, AllConvertors
from .json_from_html_helper import (
    find_str_sequence_in_str,
    get_error_content_from_json_exception,
    get_html_from_response,
    get_string_between_quotes,
    replace_strings,
)


class JSONFromHTMLConvertor(AbstractConvertor):
    """Class to add JSON as a dict to the GetDataResponse tuple"""

    convertor_name = "JSON_FROM_HTML"

    @classmethod
    def _result_with_data_field(cls, result, convertor_params):
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
        html_in_byte_repr = get_html_from_response(result.response)
        json_byte_in_html = cls._find_json_byte_in_html(
            html_in_byte_resp=html_in_byte_repr, convertor_params=convertor_params
        )

        if not json_byte_in_html:
            return cls._no_json_found_in_html(result)

        return cls._format_json(result, convertor_params, json_byte_in_html)

    @staticmethod
    def _invalid_json_result(
        result: GetDataResponse, json_snippet: str
    ) -> GetDataResponse:
        """
        Method to add proper ErrorCode object to GetDataResponse in case of
        invalid JSON.

        Args:
            result (GetDataResponse):
                GetDataResponse that needs to have the ErrorCode added.
            json_snippet (str):
                The incorrect part of the JSON that needs to be added

        Returns:
            GetDataResponse with added ErrorCode
        """
        error = add_error_data(
            error=ListErrors.INVALID_JSON_FOUND_IN_HTML,
            error_data={"json_snippet_with_error": json_snippet},
        )
        error_msg = result.error_msg
        error_msg.append(error)
        return GetDataResponse(
            response=result.response,
            is_valid=False,
            data=None,
            error_msg=error_msg,
            io_time=result.io_time,
        )

    @staticmethod
    def _no_json_found_in_html(result: GetDataResponse) -> GetDataResponse:
        error_msg = result.error_msg
        error_msg.append(ListErrors.NO_JSON_FOUND_IN_HTML)
        return GetDataResponse(
            response=result.response,
            is_valid=False,
            data=None,
            error_msg=error_msg,
            io_time=result.io_time,
        )

    @staticmethod
    def _valid_result_with_json(
        result: GetDataResponse, valid_json: dict
    ) -> GetDataResponse:
        """return class return object for succesfull json conversion"""
        return GetDataResponse(
            response=result.response,
            is_valid=True,
            data=valid_json,
            error_msg=result.error_msg,
            io_time=result.io_time,
        )

    @staticmethod
    def _validate_convertor_params(convertor_params=None) -> None:
        """
        private method to validate convertor_params argument for
        JSONFromHTMLConvertor class

        args:
            - convertor_params (dict):

        returns:
            - None: when convertor_params are valid

        raises:
            - ValueError: if convertor_params is not valid
        """
        if not convertor_params:
            raise ValueError(GetDataExceptions.NO_RESPONSE_CONVERTOR_PARAMS.value)

        if (
            isinstance(convertor_params, dict)
            and all(
                [
                    key in CONVERTOR_PARAMS_JSON_FROM_HTTP
                    for key in convertor_params.keys()
                ]
            )
            and "json_begin" in convertor_params.keys()
            and "json_end" in convertor_params.keys()
        ):
            return

        raise ValueError(GetDataExceptions.INVALID_RESPONSE_CONVERTOR_PARAMS.value)

    @classmethod
    def _find_json_byte_in_html(
        cls, html_in_byte_resp: bytes, convertor_params: dict
    ) -> Optional[bytes]:
        """Finds the json bytes string in the html

        Args:
            html_in_byte_resp (bytes): html from response
            convertor_params (dict): params for retrieving json from html

        Returns:
            (bytes): JSON bytes string from HTML
            (bool): False if JSON string could not be found
        """
        json_begin = convertor_params.get("json_begin")
        json_end = convertor_params.get("json_end")
        if not json_begin or not json_end:
            raise ValueError("No json_begin and/or json_end not defined")
        begin = find_str_sequence_in_str(json_begin, html_in_byte_resp)
        end = find_str_sequence_in_str(json_end, html_in_byte_resp, begin)
        if begin == -1 or end == -1:
            return None

        if convertor_params.get("json_within_quotes", None):
            byte_string_containing_json = html_in_byte_resp[begin : end + len(json_end)]
            return get_string_between_quotes(byte_string_containing_json)

        # if json not within quotes then return json string excluding
        # the json_begin and json_end part
        byte_string_containing_json = html_in_byte_resp[begin:end]
        return byte_string_containing_json[len(json_begin) :].strip()

    @classmethod
    def _format_json(
        cls, result: GetDataResponse, convertor_params: dict, json_in_byte: bytes
    ) -> GetDataResponse:
        """ """
        # if json in html has escaped quotes then replace these
        if convertor_params.get("escaped_quotes"):
            format_step_1 = json_in_byte.replace(b'\\"', b'"')
        else:
            format_step_1 = json_in_byte

        # execute specified string replacements (in byte format)
        format_step_2 = replace_strings(format_step_1, convertor_params)
        # turn bytes representation to string
        format_step_3 = str(format_step_2, encoding="UTF-8")
        # remove all url encodings
        format_step_4 = urllib.parse.unquote(format_step_3)
        try:
            json_result = json.loads(format_step_4)
            return cls._valid_result_with_json(result, json_result)

        except json.decoder.JSONDecodeError as error:
            json_snippet = get_error_content_from_json_exception(error)
            return cls._invalid_json_result(result, json_snippet)


AllConvertors.register_convertor(JSONFromHTMLConvertor)
