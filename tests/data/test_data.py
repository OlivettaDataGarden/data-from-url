"""
Module to define tests data for tests of get_data module
"""

import json

import chardet
from data.csv_test_data import INVALID_CSV, VALID_CSV
from data.json_from_html_example import json_byte_example
from data.test_json_from_html_data import HTML_DATA
from data.test_xml_data import INVALID_XML, VALID_XML
from errors import ErrorCode
from imports import GetDataResponse

TEST_ERROR_CODE = ErrorCode("TEST_CODE", "test")


class ResponseMock:
    """
    class to mimmick behavior of the requests.response class
    """

    def __init__(self, content=b'{"a": 1}', status_code=200):
        self._content = content
        self._status_code = status_code

    def json(self):
        return json.loads(self._content)

    @property
    def status_code(self):
        return self._status_code

    @property
    def text(self):
        """returns str value of content"""
        encoding = chardet.detect(self._content)["encoding"]
        return str(self._content, encoding)

    @property
    def content(self):
        """returns raw content"""
        return self._content


##################################################################
#                  test GetDataResponses                         #
##################################################################
DEFAULT_GET_DATA_RESPONSE = GetDataResponse(
    response=ResponseMock(), is_valid=True, error_msg=[], data=None, io_time=0
)

INVALID_GET_DATA_RESPONSE = GetDataResponse(
    response=ResponseMock(),
    is_valid=False,
    error_msg=[TEST_ERROR_CODE],
    data=None,
    io_time=0,
)

INVALID_JSON_GET_DATA_RESPONSE = GetDataResponse(
    response=ResponseMock(content=b'{"invalid json"}'),
    is_valid=True,
    error_msg=[],
    data=None,
    io_time=0,
)

INVALID_XML_GET_DATA_RESPONSE = GetDataResponse(
    response=ResponseMock(content=INVALID_XML),
    is_valid=True,
    error_msg=[],
    data=None,
    io_time=0,
)


VALID_XML_GET_DATA_RESPONSE = GetDataResponse(
    response=ResponseMock(content=VALID_XML),
    is_valid=True,
    error_msg=[],
    data=None,
    io_time=0,
)


##################################################################
#                  test Query Params                             #
##################################################################
DEFAULT_QUERY_PARAMS = {"url": "https://www.google.com", "expected_status_code": [200]}

QUERY_PARAMS_WITH_PROXY = DEFAULT_QUERY_PARAMS | {"proxy": "SCRAPERAPI"}


##################################################################
#                  test json from html settings                  #
#                  for use in test_json_from_html                #
##################################################################
CONVERTOR_PARAMS_JSON_FROM_HTTP = {
    "json_begin": "window.__PRELOADED_STATE_LISTING__=",
    "json_end": "</script>",
    "json_within_quotes": False,
}

CONVERTOR_PARAMS_ESCAPED_QUOTES = CONVERTOR_PARAMS_JSON_FROM_HTTP | {
    "escaped_quotes": True
}

JSON_FROM_HTML_IN_BYTES = json_byte_example

HTML_RESPONSE = ResponseMock(content=HTML_DATA)
NON_HTML_RESPONSE = ResponseMock(content=b"1234")

VALID_HTML_GET_DATA_RESPONSE = GetDataResponse(
    response=HTML_RESPONSE, is_valid=True, error_msg=[], data=None, io_time=0
)


##################################################################
#                  test csv settings                             #
#                  for use in CSVConvertor                       #
##################################################################
CONVERTOR_PARAMS_CSV = {"delimiter": ";"}

CSV_GET_DATA_RESPONSE = GetDataResponse(
    response=ResponseMock(content=VALID_CSV),
    is_valid=True,
    error_msg=[],
    data=None,
    io_time=0,
)

INVALID_CSV_GET_DATA_RESPONSE = GetDataResponse(
    response=ResponseMock(content=INVALID_CSV),
    is_valid=True,
    error_msg=[],
    data=None,
    io_time=0,
)
