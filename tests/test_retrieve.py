"""
test methods for get_data public interface DataFromAPI

This is outside interface to the get_data module
"""
import pytest
from imports import DataFromAPIorURL, JSONConvertor, exceptions


def test_data_form_api_or_url_exists():
    """ test that DataFromAPIorURL exists """
    assert DataFromAPIorURL()


def test_data_form_api_or_url_is_singleton_class():
    """ test that DataFromAPIorURL is a singleton class """
    data_from_api_1 = DataFromAPIorURL()
    data_from_api_2 = DataFromAPIorURL()
    assert data_from_api_1 is data_from_api_2


def test_looking_up_a_convertor_returns_a_convertor_class():
    """
    test that method _get_convertor_class raise exception when unknown
    convertor is requested
    """
    with pytest.raises(exceptions.InvalidConvertorRequested):
        DataFromAPIorURL._get_convertor_class('non_existing_convertor')


def test_looking_up_unknown_convertor_raises_exception():
    """
    test that method _get_convertor_class raise exception when unknown
    convertor is requested
    """
    with pytest.raises(exceptions.InvalidConvertorRequested):
        DataFromAPIorURL._get_convertor_class('non_existing_convertor')


def test_data_method_with_convertor_of_wrong_class_raises_excpeption():
    """
    test that method data raises and exception when convertor that is not
    string or AbstractConvertor
    """
    with pytest.raises(exceptions.InvalidConvertorType):
        DataFromAPIorURL.data(
            query_params={'a': 1},
            convertor=1)


def test_data_method_calls_get_convertor_class_with_str_input(mocker):
    """
    test that method data calls the _get_convertor_class method is called
    if convertor arguments is of type str
    """
    convertor = 'string'
    mocker.patch(
        'data_from_url.retrieve.DataFromAPIorURL._get_convertor_class',
        return_value=JSONConvertor())
    mocker.patch(
        'data_from_url.convertors.json_convertor.JSONConvertor.get_data',
        return_value=None)
    _get_convertor_class_spy = \
        mocker.spy(DataFromAPIorURL, '_get_convertor_class')
    DataFromAPIorURL.data(query_params={'a': 1}, convertor=convertor)

    assert _get_convertor_class_spy


def test_data_method_calls_get_convertor_class_with_convertor(mocker):
    """
    test that method data calls convertor get_data method when a convertor
    object is provided as input
    """
    convertor = JSONConvertor()
    mocker.patch('data_from_url.convertors.json_convertor.JSONConvertor.get_data',
                 return_value=None)
    _json_convertor_get_data_spy = \
        mocker.spy(JSONConvertor, 'get_data')
    DataFromAPIorURL.data(query_params={'a': 1}, convertor=convertor)

    assert _json_convertor_get_data_spy


def test_get_convertor_method_returns_convertor():
    """
    test that _get_convertor method returns a ConvertorClass
    """
    assert DataFromAPIorURL()._get_convertor_class('JSON') == \
        JSONConvertor
