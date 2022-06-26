"""
This module provides test data for xml_convertor module in get_data module
"""

BASE_DIR = 'tests/data/'
BASIC_XML_FILE_NAME = BASE_DIR + 'basic_xml.xml'
INVALID_XML_FILE_NAME = BASE_DIR + 'invalid_xml.xml'


def xml_str_from_file(test_file_name):
    return open(test_file_name, 'r').read()


VALID_XML = xml_str_from_file(BASIC_XML_FILE_NAME)
INVALID_XML = xml_str_from_file(INVALID_XML_FILE_NAME)
