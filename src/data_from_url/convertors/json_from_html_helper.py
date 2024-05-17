"""
Helper module for json_from_html_convertor

helper methods:
    - replace_strings
    - find_str_sequence_in_str
    - get_json_between_quotes
    - get_html_from_response
"""
from json.decoder import JSONDecodeError
from typing import Union

from requests.models import Response


def in_bytes(input_string: Union[bytes, str]) -> bytes:
    """ ensures that input bytes or string is returned in bytes """
    if isinstance(input_string, str):
        return bytes(input_string, encoding='UTF-8')

    return input_string


def replace_strings(input_string: bytes, convertor_params: dict) -> bytes:
    """
    Replace part of the json string based upon provided argument
    self.replace

    Args:
        input_string (str): string where replacement is needed
        convertor_params (dict): contains replace dict that contains
                                key value pairs where key needs to be
                                replaced by value

    Returns:
        (str): json string with replacements
    """
    replace_dict = convertor_params.get('replace', None)
    if not replace_dict:
        return input_string
    new_string = input_string
    for str_to_replace, replacement in replace_dict.items():
        new_string = new_string.replace(
            in_bytes(str_to_replace), in_bytes(replacement)
        )

    return new_string


def find_str_sequence_in_str(
        search_str: str, byte_string: bytes, start_position=None) -> int:
    """
    finds the starting index of a string in a bytestring
    """
    if start_position:
        return byte_string.find(search_str.encode(), start_position)
    return byte_string.find(search_str.encode())


def get_string_between_quotes(byte_string_containing_json: bytes) -> bytes:
    """
    Returns the byte string between the first and last quote in the
    provided byte_string_containing_json
    """
    # find position of first charachter after first quote
    json_begins_at = byte_string_containing_json.find(b'"') + 1
    # find position of last quote
    json_ends_at = byte_string_containing_json.rfind(b'"')

    return byte_string_containing_json[json_begins_at:json_ends_at]


def get_html_from_response(response: Response) -> bytes:
    """ retrieves encoded html from reponse object """
    html = response.text
    return html.encode()


def get_error_content_from_json_exception(
        error: JSONDecodeError, content_size: int = 80) -> str:
    """ Return part of the string that caused the JSONDecode error

    Args:
        error (JSONDecodeError): the exception
        content_size: size of string before and after location to be returned

    Returns:
        str: part of string that caused the exception
    """
    if not isinstance(error, JSONDecodeError):
        raise TypeError('exception must be of type JSONDecodeError')

    return error.doc[(error.pos-content_size):(error.pos+content_size)]
