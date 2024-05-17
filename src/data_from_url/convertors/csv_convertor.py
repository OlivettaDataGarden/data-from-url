"""
Module to define CSVConvertor class for the get_data module
"""

import csv
from typing import Iterator

from errors.error import ListErrors

from ..helper import normalize_string
from ..settings.dataclass import GetDataResponse
from ..settings.enumerator import GetDataExceptions
from .abstract_convertor import AbstractConvertor, AllConvertors


class CSVConvertor(AbstractConvertor):
    """
    Class to concert a CSV dataset into dict and add it to the
    GetDataResponse tuple
    """

    convertor_name = "CSV"

    @classmethod
    def _result_with_data_field(
        cls, result: GetDataResponse, convertor_params: dict
    ) -> GetDataResponse:
        """
        Creates dict from CSV in response and adds it to the results data
        field. If no proper dict can be created from response object in
        `result` argument the status of result is set to invalid and an error
        code is added.

        Args:
            result (GetDataResponse): result from API call

        Returns:
            [GetDataResponse]: new GetDataResponse with data field or status
                               and error field updated
        """
        csv_reader = cls._csv_reader_from_response(result, convertor_params)
        header = cls._header_from_csv_reader(csv_reader, convertor_params)

        list_of_dicts = cls._zip_header_and_reader(csv_reader, header, convertor_params)

        if list_of_dicts:
            return cls._valid_result_from_csv(result, {"result": list_of_dicts})

        return cls._invalid_csv_result(result)

    @staticmethod
    def _invalid_csv_result(result: GetDataResponse) -> GetDataResponse:
        error_msg = result.error_msg
        error_msg.append(ListErrors.INVALID_CSV_IN_RESPONSE)
        return GetDataResponse(
            response=result.response,
            is_valid=False,
            data=None,
            error_msg=error_msg,
            io_time=result.io_time,
        )

    @staticmethod
    def _valid_result_from_csv(
        result: GetDataResponse, valid_csv_data: dict
    ) -> GetDataResponse:
        """return class return object for succesfull cvs conversion"""
        return GetDataResponse(
            response=result.response,
            is_valid=True,
            data=valid_csv_data,
            error_msg=result.error_msg,
            io_time=result.io_time,
        )

    @staticmethod
    def _validate_convertor_params(convertor_params=None) -> None:
        """
        private method to validate convertor_params argument for
        CSVConvertor class

        args:
            - convertor_params (dict):

        returns:
            - None: when convertor_params are valid

        raises:
            - ValueError: if convertor_params is not valid
        """
        if not convertor_params:
            raise ValueError(GetDataExceptions.NO_RESPONSE_CONVERTOR_PARAMS.value)

        if isinstance(convertor_params, dict) and convertor_params.get(
            "delimiter", None
        ):
            return

        raise ValueError(GetDataExceptions.INVALID_RESPONSE_CONVERTOR_PARAMS.value)

    @classmethod
    def _csv_reader_from_response(
        cls, result: GetDataResponse, convertor_params: dict
    ) -> Iterator[list[str]]:
        """Method to return a csv reader object"""
        response = result.response
        lines = response.text.split("\n")
        delimiter = convertor_params.get("delimiter", ",")
        return csv.reader(lines, delimiter=delimiter)

    @classmethod
    def _header_from_csv_reader(
        cls, csv_reader: Iterator[list[str]], convertor_params: dict
    ) -> list:
        """Method to return the header from a csv reader object"""
        header = next(csv_reader)

        if convertor_params.get("normalize_header", True):
            header = [normalize_string(item) for item in header]

        # header in lower case unless explicitely set to false
        if convertor_params.get("header_in_lower_case", True):
            header = [x.lower() for x in header]

        return header

    @classmethod
    def _zip_header_and_reader(
        cls, csv_reader: Iterator[list[str]], header: list, convertor_params: dict
    ) -> list[dict]:
        """
        Method to return a dict by zipping the header and the csv reader
        """
        # by default values in lower case is set to False
        values_in_lower_case = convertor_params.get("values_in_lower_case", False)

        def set_case(value):
            return str(value).lower() if values_in_lower_case else str(value)

        def cleaned_row(row):
            return [set_case(value.strip()) for value in row]

        return [dict(zip(header, cleaned_row(row))) for row in csv_reader]


AllConvertors.register_convertor(CSVConvertor)
