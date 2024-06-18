"""
test methods for get_data converter module CSVConvertor
"""

import pytest
from data.test_data import (
    CONVERTOR_PARAMS_CSV,
    CSV_GET_DATA_RESPONSE,
    INVALID_CSV_GET_DATA_RESPONSE,
)
from imports import CSVConvertor, ListErrors


def test_csv_converter_class_exists():
    """
    test that CSVConvertor exists
    """
    assert CSVConvertor


def test_csv_converter_returns_dict():
    """
    test that CSVConvertor returns a dict with a valid csv
    """
    assert isinstance(
        CSVConvertor._result_with_data_field(
            CSV_GET_DATA_RESPONSE, CONVERTOR_PARAMS_CSV
        ).data,
        dict,
    )


def test_csv_converter_returns_dict_with_invalid_csv():
    """
    test that CSVConvertor returns a dict with an invalid csv
    """
    result = CSVConvertor._result_with_data_field(
        INVALID_CSV_GET_DATA_RESPONSE, CONVERTOR_PARAMS_CSV
    )
    assert not result.is_valid
    assert ListErrors.INVALID_CSV_IN_RESPONSE in result.error_msg


def test_csv_converter_returns_header_with_non_lower_char():
    """
    test that CSVConvertor returns a header with some upper case characters
    if header_in_lower_case is set to False
    """
    convertor_params = CONVERTOR_PARAMS_CSV | {"header_in_lower_case": False}
    result = CSVConvertor._result_with_data_field(
        CSV_GET_DATA_RESPONSE, convertor_params
    ).data
    first_item = result.get("result")[0]

    str_of_all_keys = "".join(first_item.keys())
    assert any(ele.isupper() for ele in str_of_all_keys)


def test_csv_converter_returns_header_with_non_ascii_char():
    """
    test that CSVConvertor returns a header with some upper case characters
    if normalize_header is set to False
    """
    convertor_params = CONVERTOR_PARAMS_CSV | {"normalize_header": False}
    result = CSVConvertor._result_with_data_field(
        CSV_GET_DATA_RESPONSE, convertor_params
    ).data
    first_item = result.get("result")[0]
    str_of_all_keys = "".join(first_item.keys())

    with pytest.raises(UnicodeEncodeError):
        str_of_all_keys.encode("ascii")


def test_csv_converter_raises_exception_if_no_convertor_params_are_provided():
    """
    test that CSVConvertor _validate_convertor_params method raises exception
    if no convertor_params are provided.
    """
    with pytest.raises(ValueError) as value_error:
        CSVConvertor._validate_convertor_params(None)

    assert "not provided" in str(value_error)


def test_csv_converter_raises_excepetion_if_convertor_params_is_not_a_dict():
    """
    test that CSVConvertor _validate_convertor_params method raises excpetion
    if no convertor_params is not a dict
    """
    with pytest.raises(ValueError) as value_error:
        CSVConvertor._validate_convertor_params("convertor_params")

    assert "invalid arguments" in str(value_error)


def test_csv_converter_raises_exc_if_delimiter_not_in_convertor_params():
    """
    test that CSVConvertor _validate_convertor_params method raises excpetion
    if delimiter not convertor_params
    """
    with pytest.raises(ValueError) as value_error:
        CSVConvertor._validate_convertor_params({"not_delimiter": ";"})

    assert "invalid arguments" in str(value_error)


def test_validate_convertor_params_returns_none_with_valid_convertor_params():
    """
    test that _validate_convertor_params returns None with valid convertor
    params
    """
    assert CSVConvertor._validate_convertor_params({"delimiter": ";"}) is None
