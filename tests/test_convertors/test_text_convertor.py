"""
test methods for get_data converter module TextConverter
"""
from data.test_data import DEFAULT_GET_DATA_RESPONSE
from imports import TextConvertor


def test_text_convertor_class_exists():
    """
    test that TextConvertor exists
    """
    assert TextConvertor


def test_text_convertor_returns_text():
    """
    test that TextConvertor returns text
    """
    assert TextConvertor._result_with_data_field(
        DEFAULT_GET_DATA_RESPONSE).data == '{"a": 1}'
