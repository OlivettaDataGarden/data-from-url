"""
This module provides test data for json_from_html_convertor module
in get_data module
"""

BASE_DIR = "tests/data/"
HTML_FILE_NAME = BASE_DIR + "json_from_html.html"


def str_from_file(test_file_name):
    return open(test_file_name, "r").read()


HTML_DATA = bytes(str_from_file(HTML_FILE_NAME).encode())
