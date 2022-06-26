"""
test methods for get_data converter module TextConverter
"""
from data.test_data import INVALID_XML_GET_DATA_RESPONSE, \
    VALID_XML_GET_DATA_RESPONSE
from errors.error import ListErrors
from imports import XMLConvertor


def test_xml_convertor_class_exists():
    """
    test that XMLConvertor exists
    """
    assert XMLConvertor


def test_xml_convertor_returns_a_dict():
    """
    test that XMConvertor returns a dict from proper XML in the response
    """
    xml_conversion_result = XMLConvertor._result_with_data_field(
        VALID_XML_GET_DATA_RESPONSE)
    assert isinstance(xml_conversion_result.data, dict)
    assert 'note' in xml_conversion_result.data


def test_xml_converter_sets_result_to_invalid_with_bad_xml():
    """
    test that XMLConvertor returns invalid GetDataResponse object when
    response contains invalid XML
    """
    result = XMLConvertor._result_with_data_field(
        INVALID_XML_GET_DATA_RESPONSE)
    assert result.data is None
    assert not result.is_valid
    assert ListErrors.INVALID_XML_IN_RESPONSE in \
        result.error_msg
