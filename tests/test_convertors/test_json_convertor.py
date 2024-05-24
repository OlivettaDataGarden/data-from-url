"""
test methods for get_data converter module JSONConvertor
"""

from data.test_data import DEFAULT_GET_DATA_RESPONSE, INVALID_JSON_GET_DATA_RESPONSE
from errors.error import ListErrors
from imports import JSONConvertor


def test_json_converter_class_exists():
    """
    test that JSONConvertor exists
    """
    assert JSONConvertor


def test_json_converter_returns_dict():
    """
    test that JSONConvertor exists
    """
    assert JSONConvertor._result_with_data_field(DEFAULT_GET_DATA_RESPONSE).data == {
        "a": 1
    }


def test_json_converter_set_result_to_invalid_with_bad_json():
    """
    test that JSONConvertor returns invalid GetDataResponse object when
    response contains invalid JSON
    """
    result = JSONConvertor._result_with_data_field(INVALID_JSON_GET_DATA_RESPONSE)
    assert result.data is None
    assert not result.is_valid
    assert ListErrors.INVALID_JSON_IN_RESPONSE in result.error_msg
