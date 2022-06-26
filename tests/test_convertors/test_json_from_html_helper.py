"""
test methods for get_data json_from_html_helper module
"""
import json

import pytest
from data.test_data import HTML_RESPONSE, NON_HTML_RESPONSE
from imports import find_str_sequence_in_str, \
    get_error_content_from_json_exception, get_html_from_response, \
    get_string_between_quotes, in_bytes, replace_strings


def test_replace_strings_method_with_no_replace_dict():
    """
    test that replace_strings method without replace dict leaves input
    string as is
    """
    input_string = "{'a':1}"
    convertor_params = {}
    assert replace_strings(input_string, convertor_params) == input_string


def test_replace_strings_method_with_replace_dict_succes():
    """
    test that replace_strings method with replace dict replaces
    indicated string
    """
    input_string = b"{'a':1}"
    convertor_params = {'replace': {'a': 'b'}}
    assert replace_strings(input_string, convertor_params) == b"{'b':1}"


def test_replace_strings_method_with_replace_dict_items_not_found():
    """
    test that replace_strings method with replace dict items that are not
    found in the input string leave the input string unharmed
    """
    input_string = b"{'a':1}"
    convertor_params = {'replace': {'c': 'b'}}
    assert replace_strings(input_string, convertor_params) == input_string


def test_find_str_in_seq_success():
    """
    test that find_str_sequence_in_str resturns correct index of string in str
    """
    search_str = "9"
    byte_string = b"01234567890123456789"
    assert find_str_sequence_in_str(search_str, byte_string) == 9


def test_find_str_in_seq_with_start_position_success():
    """
    test that find_str_sequence_in_str resturns correct index of string in str
    if a startposition is given
    """
    search_str = "2"
    byte_string = b"01234567890123456789"
    start_position = 5
    assert \
        find_str_sequence_in_str(search_str, byte_string, start_position) == 12


def test_find_str_in_seq_returns_minus_one_when_str_not_found():
    """
    test that find_str_sequence_in_str resturns -1 when string not found
    """
    search_str = "not found"
    byte_string = b"01234567890123456789"
    assert find_str_sequence_in_str(search_str, byte_string) == -1


def test_get_html_from_response_returns_bytes_from_html():
    """
    test get_html_from_response return a bytes object from html
    """
    assert isinstance(get_html_from_response(HTML_RESPONSE), bytes)


def test_get_html_from_response_works_with_non_html_response():
    """
    test get_html_from_response still returns a bytes object from non
    html response
    """
    assert isinstance(get_html_from_response(NON_HTML_RESPONSE), bytes)


def test_get_string_between_quotes():
    """
    test get_string_between_quotes returns the string between first and last
    quote in bytes string
    """
    string_with_quotes = b'123"456"123'
    assert get_string_between_quotes(string_with_quotes) == b'456'


def test_get_string_between_quotes_with_more_the_two_quotes():
    """
    test get_string_between_quotes returns the string between first and last
    quote in bytes string also if there are more quotes in the string
    """
    string_with_quotes = b'12"3"456"1"23'
    assert get_string_between_quotes(string_with_quotes) == b'3"456"1'


def test_in_bytes_converts_string_to_bytes():
    """
    test in_bytes method returns a bytes string when normal string is given
    """
    assert isinstance(in_bytes('normal_string'), bytes)


def test_in_bytes_returns_in_bytes_string():
    """
    test in_bytes method returns a bytes string when bytes string is given
    """
    bytes_input = b'bytes string'
    assert in_bytes(bytes_input) == bytes_input


def test_get_error_content_from_json_exception():
    """
    test get_error_content_from_json_exception string were erro in json occured
    """
    try:
        json.loads('{"invalid_json": "quote to " much on postion 29"}')
    except json.decoder.JSONDecodeError as error:
        json_snippit = get_error_content_from_json_exception(error, 10)

    assert json_snippit == 'uote to " much on po'


def test_get_error_content_from_json_exception_with_wrong_exception():
    """
    test get_error_content_from_json_exception raises TypeError when
    no JSONDecodeError is provided
    """
    with pytest.raises(TypeError):
        get_error_content_from_json_exception(ValueError('text'))
