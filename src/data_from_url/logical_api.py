"""
Module to provide the LogicalApi class for the get_data module
"""

from datetime import datetime

from errors.error import ListErrors
from requests.exceptions import InvalidSchema, MissingSchema

from .helper import (
    make_request_with_method,
    remove_none_values,
    retry_after_connection_error,
)
from .settings.dataclass import GetDataResponse
from .settings.enumerator import status_code_errors

CONNECTIVITY_ERROR_RESPONSE = GetDataResponse(
    response=None,
    is_valid=False,
    data=None,
    error_msg=[ListErrors.CONNECTIVITY_ERROR],
    io_time=0,
)

MISSING_SCHEMA_ERROR_RESPONSE = GetDataResponse(
    response=None,
    is_valid=False,
    data=None,
    error_msg=[ListErrors.INVALID_URL],
    io_time=0,
)

INVALID_SCHEMA_ERROR_RESPONSE = GetDataResponse(
    response=None,
    is_valid=False,
    data=None,
    error_msg=[ListErrors.INVALID_URL_SCHEMA],
    io_time=0,
)


def io_in_seconds(start_time: datetime) -> float:
    """
    returns time in seconds between now and start_time

    args:
        start_time (datetime): start time
    returns:
        float: time past in seconds
    """
    return (datetime.now() - start_time).total_seconds()


class LogicalApi:
    """
    This class will invoke the actual API call and return the response as part
    of the GetDataResponse object if the call was succesfull

    Public method:
        - result
    """

    @classmethod
    def result(cls, query_params: dict) -> GetDataResponse:
        """retrieve result from url or api for given query_params"""
        expected_status_code = query_params.pop("expected_status_code")
        result = cls._do_request(**query_params)
        if not result.is_valid:
            return result

        return cls._check_status_code(result, expected_status_code)

    @staticmethod
    @retry_after_connection_error(return_value_on_fail=CONNECTIVITY_ERROR_RESPONSE)
    def _do_request(**query_params: dict) -> GetDataResponse:
        """Method to invoke actual request based upon query_params

        Method will retry in case of network errors. In case network error is
        persistent a default GetDataResponse object with connectivity error
        code will be returned

        Returns:
            GetDataResponse: Contains response, is_valid, errors and (empty)
                             data field
        """
        clean_query_params = remove_none_values(query_params)
        start_time = datetime.now()
        try:
            response = make_request_with_method(**clean_query_params)
        except MissingSchema:
            return MISSING_SCHEMA_ERROR_RESPONSE
        except InvalidSchema:
            return INVALID_SCHEMA_ERROR_RESPONSE

        return GetDataResponse(
            response=response,
            is_valid=True,
            data=None,
            error_msg=[],
            io_time=io_in_seconds(start_time=start_time),
        )

    @staticmethod
    def _check_status_code(
        result: GetDataResponse, expected_status_code: list
    ) -> GetDataResponse:
        """Method to update result if status_code response is unexpected

        args:
            - result (GetDataResponse)

        Returns:
            GetDataResponse: Updated GetDataResponse in case of unexpected
                             status_code
        """
        response = result.response
        status_code = response.status_code
        io_time = result.io_time
        if status_code in expected_status_code:
            return result

        return GetDataResponse(
            response=response,
            is_valid=False,
            error_msg=[status_code_errors(status_code)],
            data=None,
            io_time=io_time,
        )
