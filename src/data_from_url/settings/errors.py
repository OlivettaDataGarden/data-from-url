"""
Module to define Errors for the data-from-url module
"""

from errors import ErrorCode, ErrorListByMixin


class GetDataErrors():
    """Class to define enumerator with functional errors for GetData module."""

    CONNECTIVITY_ERROR = ErrorCode(
        code="GD_NETW_0001", description="Network connectivity issues"
    )

    INVALID_JSON_IN_RESPONSE = ErrorCode(
        code="GD_CONV_00101", description="Response contains invalid JSON"
    )

    INVALID_XML_IN_RESPONSE = ErrorCode(
        code="GD_CONV_00201", description="Response contains invalid XML"
    )

    NO_JSON_FOUND_IN_HTML = ErrorCode(
        code="GD_CONV_00301", description="No JSON string was found in HTML"
    )

    INVALID_JSON_FOUND_IN_HTML = ErrorCode(
        code="GD_CONV_00302", description="JSON string found in HTML is invalid"
    )

    INVALID_CSV_IN_RESPONSE = ErrorCode(
        code="GD_CONV_00401", description="CSV in response is not valid CSV"
    )

    INVALID_STATUS_CODE_200 = ErrorCode(
        code="GD_STATUSCODE_00200",
        description="Response with unexpected statuscode 200",
    )

    INVALID_STATUS_CODE_201 = ErrorCode(
        code="GD_STATUSCODE_00201",
        description="Response with unexpected statuscode 201",
    )

    INVALID_STATUS_CODE_401 = ErrorCode(
        code="GD_STATUSCODE_00401",
        description="Response with unexpected statuscode 401",
    )

    INVALID_STATUS_CODE_402 = ErrorCode(
        code="GD_STATUSCODE_00402",
        description="Response with unexpected statuscode 402",
    )

    INVALID_STATUS_CODE_403 = ErrorCode(
        code="GD_STATUSCODE_00403",
        description="Response with unexpected statuscode 403",
    )

    INVALID_STATUS_CODE_404 = ErrorCode(
        code="GD_STATUSCODE_00404",
        description="Response with unexpected statuscode 404",
    )

    INVALID_STATUS_CODE_500 = ErrorCode(
        code="GD_STATUSCODE_00500",
        description="Response with unexpected statuscode 500",
    )

    INVALID_STATUS_CODE = ErrorCode(
        code="GD_STATUSCODE_00001", description="Response with unexpected statuscode"
    )

    INVALID_URL = ErrorCode(
        code="GD_INVALID_URL_00001", description="URL missing schema"
    )

    INVALID_URL_SCHEMA = ErrorCode(
        code="GD_INVALID_URL_00002", description="URL with invalid schema"
    )


class LocListErrors(ErrorListByMixin, GetDataErrors):
    pass
