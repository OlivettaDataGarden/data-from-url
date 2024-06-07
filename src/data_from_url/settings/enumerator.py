"""
Module to define enumerators for get_data module

enumerators:
    - BaseEnumerator
"""

from enum import Enum
from typing import List

from .errors import ErrorCode, ListErrors
from .exceptions import InvalidConvertorRequested


class BaseEnumerator(Enum):
    """
    Class to define base enumerator with values and keys methods
    Only to be used for defining new enumerators
    """

    @classmethod
    def values(cls) -> List:
        """Returns all values from the enumerator."""
        return [item.value for item in list(cls.__members__.values())]

    @classmethod
    def keys(cls) -> List:
        """Returns all lists from the enumerator."""
        return list(cls.__members__.keys())


class RestMethod(BaseEnumerator):
    """
    Class to define enumerator for get_data allowed rest methods
    """

    GET = "GET"
    POST = "POST"


class GetDataExceptions(BaseEnumerator):
    """
    Class to define enumerator for get_data exceptions.
    These exceptions should halt the processing of the flow
    """

    INVALID_RESPONSE_FORMAT = (
        "response_format argument contains unkwown response format type"
    )

    INVALID_RESPONSE_CONVERTOR_PARAMS = "convertor_params contains invalid arguments"

    NO_RESPONSE_CONVERTOR_PARAMS = "convertor_params required but not provided"

    INVALID_METHOD = "Method should be one of " + f"{str(RestMethod.keys())}"

    INVALID_PROXY = "provided proxy service not defined"

    INVALID_DATA_CONVERTOR = InvalidConvertorRequested

    UNKNOWN_CONVERTOR = "Provided convertor is not registered."

    INVALID_URL = "Invalid url provided."


def status_code_errors(status_code: int) -> ErrorCode:
    """method to retrieve status_code error based on actual status code"""
    return {
        200: ListErrors.INVALID_STATUS_CODE_200,
        201: ListErrors.INVALID_STATUS_CODE_201,
        401: ListErrors.INVALID_STATUS_CODE_401,
        402: ListErrors.INVALID_STATUS_CODE_402,
        403: ListErrors.INVALID_STATUS_CODE_403,
        404: ListErrors.INVALID_STATUS_CODE_404,
        500: ListErrors.INVALID_STATUS_CODE_500,
    }.get(status_code, None) or ListErrors.INVALID_STATUS_CODE
