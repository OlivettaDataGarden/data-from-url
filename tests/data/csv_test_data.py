"""
This module provides test data for csv_convertor module in get_data module
"""

BASE_DIR = 'tests/data/'
CSV_FILE_NAME = BASE_DIR + 'csv_valid.csv'
INVALID_CSV_FILE_NAME = BASE_DIR + 'csv_invalid.csv'


def csv_str_from_file(test_file_name):
    return open(test_file_name, 'r').read()


VALID_CSV = bytes(csv_str_from_file(CSV_FILE_NAME).encode())
INVALID_CSV = bytes(csv_str_from_file(INVALID_CSV_FILE_NAME).encode())
