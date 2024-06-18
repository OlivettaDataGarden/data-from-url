"""
test methods for get_data converter module TextConverter
"""

import pytest
from data.test_data import (
    CONVERTOR_PARAMS_ESCAPED_QUOTES,
    CONVERTOR_PARAMS_JSON_FROM_HTTP,
    JSON_FROM_HTML_IN_BYTES,
    VALID_HTML_GET_DATA_RESPONSE,
)
from imports import (
    GetDataResponse,
    JSONFromHTMLConvertor,
    ListErrors,
    json_from_html_convertor,
)

JSON_FROM_HTML_PATCH_PATH = (
    "data_from_url.convertors.json_from_html_convertor.JSONFromHTMLConvertor"
)

JSON_FROM_HTML_HELPER_PATCH_PATH = "data_from_url.convertors.json_from_html_helper"


def copy_get_data_response(get_data_response: GetDataResponse) -> GetDataResponse:
    """
    returns a copy of GetDataResponse object.
    This method is needed if GetDataResponse objects are reused in the tests
    as error pile up in the error_msg array.
    """
    return GetDataResponse(
        response=get_data_response.response,
        is_valid=get_data_response.is_valid,
        error_msg=get_data_response.error_msg.copy(),
        data=get_data_response.data,
        io_time=get_data_response.io_time,
    )


def test_json_from_html_convertor_class_exists():
    """
    test that JSONFromHTMLConvertor exists
    """
    assert JSONFromHTMLConvertor


def test_json_from_html_validate_convertor_params_method_returns_none():
    """
    test that JSONFromHTMLConvertor _validate_convertor_params method returns
    none when valid convertor_params are provided.

    A None return implies that the convertor_params are valid
    """
    assert (
        JSONFromHTMLConvertor._validate_convertor_params(
            CONVERTOR_PARAMS_JSON_FROM_HTTP
        )
        is None
    )


def test_validate_convertor_params_without_json_within_quotes_argument():
    """
    test that JSONFromHTMLConvertor _validate_convertor_params method returns
    none when json_within_quotes is not included in convertor_params

    A None return implies that the convertor_params are valid
    """
    convertor_params = CONVERTOR_PARAMS_JSON_FROM_HTTP.copy()
    convertor_params.pop("json_within_quotes")
    assert JSONFromHTMLConvertor._validate_convertor_params(convertor_params) is None


def test_validate_convertor_params_with_empty_convertor_params():
    """
    test that JSONFromHTMLConvertor _validate_convertor_params raises an
    exception when empty format params are provided
    """
    with pytest.raises(ValueError):
        JSONFromHTMLConvertor._validate_convertor_params({})


def test_validate_convertor_params_with_invalid_params():
    """
    test that JSONFromHTMLConvertor _validate_convertor_params raises an
    exception when invalid parameter is provided
    """
    invalid_convertor_params = CONVERTOR_PARAMS_JSON_FROM_HTTP | {
        "invalid_param": "value"
    }
    with pytest.raises(ValueError):
        JSONFromHTMLConvertor._validate_convertor_params(invalid_convertor_params)


def test_validate_convertor_params_with_non_dict_convertor_params():
    """
    test that JSONFromHTMLConvertor _validate_convertor_params raises an
    exception when format params of type other then dict are provided
    """
    with pytest.raises(ValueError):
        JSONFromHTMLConvertor._validate_convertor_params("non dict type")


def test_validate_convertor_params_with_no_convertor_params_raises_exception():
    """
    test that JSONFromHTMLConvertor _validate_convertor_params raises an
    exception when no format params are provided
    """
    with pytest.raises(ValueError):
        JSONFromHTMLConvertor._validate_convertor_params()


def test_result_with_data_field_calls_get_html_from_response(mocker):
    """
    test that JSONFromHTMLConvertor _result_with_data_field calls
    get_html_from_repsonse
    """
    mocker.patch(
        JSON_FROM_HTML_PATCH_PATH + "._find_json_byte_in_html",
        return_value="html content",
    )
    mocker.patch(
        JSON_FROM_HTML_PATCH_PATH + "._format_json", return_value="html content"
    )
    get_html_from_response_spy = mocker.spy(
        json_from_html_convertor, "get_html_from_response"
    )
    JSONFromHTMLConvertor._result_with_data_field(
        result=VALID_HTML_GET_DATA_RESPONSE,
        convertor_params=CONVERTOR_PARAMS_JSON_FROM_HTTP,
    )
    assert get_html_from_response_spy.called


def test_result_with_data_field_calls_no_json_found(mocker):
    """
    test that JSONFromHTMLConvertor _result_with_data_field calls
    _no_json_found_in_html when no json string is found in the html
    """
    valid_html_data_response = copy_get_data_response(VALID_HTML_GET_DATA_RESPONSE)
    mocker.patch(
        JSON_FROM_HTML_PATCH_PATH + "._find_json_byte_in_html", return_value=None
    )
    no_json_found_in_html_spy = mocker.spy(
        JSONFromHTMLConvertor, "_no_json_found_in_html"
    )
    JSONFromHTMLConvertor._result_with_data_field(
        result=valid_html_data_response,
        convertor_params=CONVERTOR_PARAMS_JSON_FROM_HTTP,
    )
    assert no_json_found_in_html_spy.called


def test_result_with_data_field_calls_format_json(mocker):
    """
    test that JSONFromHTMLConvertor _result_with_data_field calls
    _format_json when json string is found in the html
    """
    valid_html_data_response = copy_get_data_response(VALID_HTML_GET_DATA_RESPONSE)
    mocker.patch(
        JSON_FROM_HTML_PATCH_PATH + "._find_json_byte_in_html",
        return_value=b"html content",
    )
    format_json_spy = mocker.spy(JSONFromHTMLConvertor, "_format_json")
    JSONFromHTMLConvertor._result_with_data_field(
        result=valid_html_data_response,
        convertor_params=CONVERTOR_PARAMS_JSON_FROM_HTTP,
    )
    assert format_json_spy.called


def test_invalid_json_result():
    """
    test that invalid_json_result returns an invalid GetDataResponse with
    INVALID_JSON_FOUND_IN_HTML in the error_msg
    """
    valid_html_data_response = copy_get_data_response(VALID_HTML_GET_DATA_RESPONSE)
    result = JSONFromHTMLConvertor._invalid_json_result(
        result=valid_html_data_response, json_snippet="test snippet"
    )
    assert isinstance(result, GetDataResponse)
    assert not result.is_valid
    assert ListErrors.INVALID_JSON_FOUND_IN_HTML.code in str(result.error_msg)
    assert result.error_msg[0].error_data == {"json_snippet_with_error": "test snippet"}


def test_no_json_found_in_html():
    """
    test that _no_json_found_in_html returns an invalid GetDataResponse with
    NO_JSON_FOUND_IN_HTML in the error_msg
    """
    result = JSONFromHTMLConvertor._no_json_found_in_html(
        result=VALID_HTML_GET_DATA_RESPONSE
    )
    assert isinstance(result, GetDataResponse)
    assert not result.is_valid
    assert ListErrors.NO_JSON_FOUND_IN_HTML in result.error_msg


def test_valid_result_with_json():
    """
    test that _valid_result_with_json returns a valid GetDataResponse object
    with data attribute filled with valid_json input
    """
    result = JSONFromHTMLConvertor._valid_result_with_json(
        result=VALID_HTML_GET_DATA_RESPONSE, valid_json={"a": 1}
    )
    assert isinstance(result, GetDataResponse)
    assert result.is_valid
    assert result.data == {"a": 1}


def test_find_json_byte_in_html_returns_false_no_begin():
    """
    test that _find_json_byte_in_html returns False when json_begin is not
    found
    """
    html_in_byte_resp = b"abcdef"
    convertor_params = {"json_begin": "not found", "json_end": "d"}
    assert not JSONFromHTMLConvertor._find_json_byte_in_html(
        html_in_byte_resp=html_in_byte_resp, convertor_params=convertor_params
    )


def test_find_json_byte_in_html_returns_false_no_end():
    """
    test that _find_json_byte_in_html returns False when json_end is not
    found
    """
    html_in_byte_resp = b"abcdef"
    convertor_params = {"json_begin": "b", "json_end": "not found"}
    assert not JSONFromHTMLConvertor._find_json_byte_in_html(
        html_in_byte_resp=html_in_byte_resp, convertor_params=convertor_params
    )


def test_find_json_byte_in_html_calls_get_string_between_quotes(mocker):
    """
    test that _find_json_byte_in_html calls get_string_between_quotes
    method when convertor_params `json_within_quotes` attr is set to true
    """
    html_in_byte_resp = b"abcdef"
    convertor_params = {"json_begin": "b", "json_end": "e", "json_within_quotes": True}
    get_string_between_quotes_spy = mocker.spy(
        json_from_html_convertor, "get_string_between_quotes"
    )

    JSONFromHTMLConvertor._find_json_byte_in_html(
        html_in_byte_resp=html_in_byte_resp, convertor_params=convertor_params
    )
    assert get_string_between_quotes_spy.called


def test_find_json_byte_in_html_returns_correct_string():
    """
    test that _find_json_byte_in_html returns correct string when
    convertor_params `json_within_quotes` attr is set to false.
    json_begin and json_end strings should be removed from resulting byte
    string. Resulting byte string should be stripped from leading and lagging
    spaces
    """
    html_in_byte_resp = b"begin bcde end f"
    convertor_params = {
        "json_begin": "begin",
        "json_end": "end",
        "json_within_quotes": False,
    }
    assert (
        JSONFromHTMLConvertor._find_json_byte_in_html(
            html_in_byte_resp=html_in_byte_resp, convertor_params=convertor_params
        )
        == b"bcde"
    )


def test_format_json_calls_invalid_json_result(mocker):
    """
    test that format_json calls the _invalid_json_result method
    when an invalid json byte string is processed
    """
    invalid_json_result_spy = mocker.spy(JSONFromHTMLConvertor, "_invalid_json_result")

    JSONFromHTMLConvertor._format_json(
        result=VALID_HTML_GET_DATA_RESPONSE,
        convertor_params=CONVERTOR_PARAMS_JSON_FROM_HTTP,
        json_in_byte=b"invalid_json",
    )
    assert invalid_json_result_spy.called


def test_format_json_returns_valid_json():
    """
    test that format_json calls returns a GetDataResponse with status
    valid and a dict as datafield when valid json byte string is provided
    """
    result = JSONFromHTMLConvertor._format_json(
        result=VALID_HTML_GET_DATA_RESPONSE,
        convertor_params=CONVERTOR_PARAMS_JSON_FROM_HTTP,
        json_in_byte=JSON_FROM_HTML_IN_BYTES,
    )
    assert result.is_valid
    assert isinstance(result.data, dict)


def test_format_json_returns_correct_json():
    """
    test that format_json calls returns a GetDataResponse with a correct json
    as dict in the data
    """
    result = JSONFromHTMLConvertor._format_json(
        result=VALID_HTML_GET_DATA_RESPONSE,
        convertor_params=CONVERTOR_PARAMS_JSON_FROM_HTTP,
        json_in_byte=b'{"a": 1}',
    )
    assert result.data == {"a": 1}


def test_format_json_replaces_strings_when_required():
    """
    test that format_json calls runs the replace instructions from the
    convertor_params
    """
    convertor_params = CONVERTOR_PARAMS_JSON_FROM_HTTP | {"replace": {"//d": "d"}}
    result = JSONFromHTMLConvertor._format_json(
        result=VALID_HTML_GET_DATA_RESPONSE,
        convertor_params=convertor_params,
        json_in_byte=b'{"a//d": 1}',
    )
    assert result.data == {"ad": 1}


def test_format_json_replaces_double_backslashes():
    """
    test that format_json replaces `\\"` with `"` in a json byte string
    """
    result = JSONFromHTMLConvertor._format_json(
        result=VALID_HTML_GET_DATA_RESPONSE,
        convertor_params=CONVERTOR_PARAMS_ESCAPED_QUOTES,
        json_in_byte=b'{"a\\": 1}',
    )
    assert result.data == {"a": 1}
