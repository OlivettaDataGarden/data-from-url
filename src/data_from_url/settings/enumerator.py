"""
Module to define enumerators for get_data module

enumerators:
    - BaseEnumerator
"""
from enum import Enum

from errors.base import ErrorCode, FunctionalErrorsBaseClass
from errors.error import ListErrors

from .exceptions import InvalidConvertorRequested


class BaseEnumerator(Enum):
    """
    Class to define base enumerator with values and keys methods
    Only to be used for defining new enumerators
    """

    @classmethod
    def values(cls):
        return [item.value for item in list(cls.__members__.values())]

    @classmethod
    def keys(cls):
        return list(cls.__members__.keys())


class RestMethod(BaseEnumerator):
    """
    Class to define enumerator for get_data allowed rest methods
    """
    GET = 'GET'
    POST = 'POST'


class GetDataExceptions(BaseEnumerator):
    """
    Class to define enumerator for get_data exceptions.
    These exceptions should halt the processing of the flow
    """
    INVALID_RESPONSE_FORMAT = \
        'response_format argument contains unkwown response format type'

    INVALID_RESPONSE_CONVERTOR_PARAMS = \
        'convertor_params contains invalid arguments'

    NO_RESPONSE_CONVERTOR_PARAMS = \
        'convertor_params required but not provided'

    INVALID_METHOD = \
        'Method should be one of ' + \
        f'{str(RestMethod.keys())}'

    INVALID_PROXY = 'provided proxy service not defined'

    INVALID_DATA_CONVERTOR = InvalidConvertorRequested

    UNKNOWN_CONVERTOR = 'Provided convertor is not registered.'

    INVALID_URL = 'Invalid url provided.'


def status_code_errors(status_code: int) -> ErrorCode:
    """method to retrieve status_code error based on actual status code"""
    return {
        200: ListErrors.INVALID_STATUS_CODE_200,
        201: ListErrors.INVALID_STATUS_CODE_201,
        403: ListErrors.INVALID_STATUS_CODE_403,
        404: ListErrors.INVALID_STATUS_CODE_404,
        500: ListErrors.INVALID_STATUS_CODE_500
    }.get(status_code, None) or ListErrors.INVALID_STATUS_CODE


class GettDataErrors(FunctionalErrorsBaseClass):
    """Class to define enumerator with functional errors for GetData module."""
    CONNECTIVITY_ERROR = ErrorCode(
        code='GD_NETW_0001',
        description='Network connectivity issues')

    INVALID_JSON_IN_RESPONSE = ErrorCode(
        code='GD_CONV_00101',
        description='Response contains invalid JSON')

    INVALID_XML_IN_RESPONSE = ErrorCode(
        code='GD_CONV_00201',
        description='Response contains invalid XML')

    NO_JSON_FOUND_IN_HTML = ErrorCode(
        code='GD_CONV_00301',
        description='No JSON string was found in HTML')

    INVALID_JSON_FOUND_IN_HTML = ErrorCode(
        code='GD_CONV_00302',
        description='JSON string found in HTML is invalid')

    INVALID_CSV_IN_RESPONSE = ErrorCode(
        code='GD_CONV_00401',
        description='CSV in response is not valid CSV')

    INVALID_STATUS_CODE_200 = ErrorCode(
        code='GD_STATUSCODE_00200',
        description='Response with unexpected statuscode 200')

    INVALID_STATUS_CODE_201 = ErrorCode(
        code='GD_STATUSCODE_00201',
        description='Response with unexpected statuscode 201')

    INVALID_STATUS_CODE_403 = ErrorCode(
        code='GD_STATUSCODE_00403',
        description='Response with unexpected statuscode 403')

    INVALID_STATUS_CODE_404 = ErrorCode(
        code='GD_STATUSCODE_00404',
        description='Response with unexpected statuscode 404')

    INVALID_STATUS_CODE_500 = ErrorCode(
        code='GD_STATUSCODE_00500',
        description='Response with unexpected statuscode 500')

    INVALID_STATUS_CODE = ErrorCode(
        code='GD_STATUSCODE_00001',
        description='Response with unexpected statuscode')

    INVALID_URL = ErrorCode(
        code='GD_INVALID_URL_00001',
        description='URL missing schema')

    INVALID_URL_SCHEMA = ErrorCode(
        code='GD_INVALID_URL_00002',
        description='URL with invalid schema')


ListErrors.register_errors(GettDataErrors)
