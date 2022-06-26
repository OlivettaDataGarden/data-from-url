"""
test methods for get_data abstract converter class
"""
import pytest
from data.test_data import DEFAULT_GET_DATA_RESPONSE, DEFAULT_QUERY_PARAMS, \
    INVALID_GET_DATA_RESPONSE
from imports import AbstractConvertor, AllConvertors, GetData, GetDataResponse

ABS_CONVT_CLASS = \
    'data_from_url.convertors.abstract_convertor.AbstractConvertor.'


def test_abstract_convertor_class_exists():
    """
    test that AbstractConvertor exists
    """
    assert AbstractConvertor


def test_convertor_implements_get_data_method(mocker):
    """
    test that get_data method exists in AbstractConvertor
    """
    mocker.patch(ABS_CONVT_CLASS + '_validate_convertor_params',
                 return_value=None)
    mocker.patch('data_from_url.get_data.GetData.result',
                 return_value=DEFAULT_GET_DATA_RESPONSE)
    mocker.patch(ABS_CONVT_CLASS + '_result_with_data_field',
                 return_value=DEFAULT_GET_DATA_RESPONSE)

    assert isinstance(
        AbstractConvertor.get_data(query_params=DEFAULT_QUERY_PARAMS),
        GetDataResponse)


def test_get_data_method_calls_validate_convertor_params(mocker):
    """
    test that get_data method exists in AbstractConvertor
    """
    mocker.patch(ABS_CONVT_CLASS + '_validate_convertor_params',
                 return_value=None)
    mocker.patch('data_from_url.get_data.GetData.result',
                 return_value=DEFAULT_GET_DATA_RESPONSE)
    mocker.patch(ABS_CONVT_CLASS + '_result_with_data_field',
                 return_value=DEFAULT_GET_DATA_RESPONSE)

    validate_convertor_params = mocker.spy(
        AbstractConvertor, '_validate_convertor_params')

    AbstractConvertor.get_data(query_params=DEFAULT_QUERY_PARAMS)
    assert validate_convertor_params.called


def test_get_data_method_does_not_call_result_with_data_field_method(mocker):
    """
    test that the result_with_data_field method is not called by get_data
    method when GetData result is invalid
    """
    mocker.patch(ABS_CONVT_CLASS + '_validate_convertor_params',
                 return_value=None)
    mocker.patch('data_from_url.get_data.GetData.result',
                 return_value=INVALID_GET_DATA_RESPONSE)

    result_with_data_spy = mocker.spy(
        AbstractConvertor, '_result_with_data_field')
    AbstractConvertor.get_data(query_params=DEFAULT_QUERY_PARAMS)
    assert not result_with_data_spy.called


def test_get_data_method_does_not_change_invalid_get_data_result(mocker):
    """
    test that the result from GetData.result is not changed when invalid
    """
    mocker.patch(ABS_CONVT_CLASS + '_validate_convertor_params',
                 return_value=None)
    mocker.patch('data_from_url.get_data.GetData.result',
                 return_value=INVALID_GET_DATA_RESPONSE)

    result = AbstractConvertor.get_data(query_params=DEFAULT_QUERY_PARAMS)
    assert result is INVALID_GET_DATA_RESPONSE


def test_get_data_method_calls_result_with_data_field_method(mocker):
    """
    test that the result_with_data_field method is called by get_data method
    """
    mocker.patch(ABS_CONVT_CLASS + '_validate_convertor_params',
                 return_value=None)
    mocker.patch('data_from_url.get_data.GetData.result',
                 return_value=DEFAULT_GET_DATA_RESPONSE)
    mocker.patch(ABS_CONVT_CLASS + '_result_with_data_field',
                 return_value=DEFAULT_GET_DATA_RESPONSE)

    result_with_data_spy = mocker.spy(
        AbstractConvertor, '_result_with_data_field')

    AbstractConvertor.get_data(query_params=DEFAULT_QUERY_PARAMS)
    assert result_with_data_spy.called


def test_get_data_method_calls_get_data_class_result_method(mocker):
    """
    test that the GetData class result method is called by get_data method
    """
    mocker.patch(ABS_CONVT_CLASS + '_validate_convertor_params',
                 return_value=None)
    mocker.patch('data_from_url.get_data.GetData.result',
                 return_value=DEFAULT_GET_DATA_RESPONSE)
    mocker.patch(ABS_CONVT_CLASS + '_result_with_data_field',
                 return_value=DEFAULT_GET_DATA_RESPONSE)

    get_data_result_spy = mocker.spy(GetData, 'result')
    AbstractConvertor.get_data(query_params=DEFAULT_QUERY_PARAMS)
    assert get_data_result_spy.called


def test_convertor_implements_abstract_result_with_data_field_method(mocker):
    """
    test that _result_with_data_field method exists in AbstractConvertor
    """
    assert AbstractConvertor._result_with_data_field() is None


def test_convertor_implements_validate_convertor_params_method(mocker):
    """
    test that _validate_convertor_params method exists in AbstractConvertor
    """
    assert AbstractConvertor._validate_convertor_params(None) is None


def test_validate_convertor_params_method_raises_value_error(mocker):
    """
    test that _validate_convertor_params method raises value error when
    provided argument `convertor_params` is invalid
    """
    with pytest.raises(ValueError):
        AbstractConvertor._validate_convertor_params('not_valid')


def test_abstract_all_convertors_class_exists():
    """
    test that AllConvertors class exists
    """
    assert AllConvertors


def test_convertors_list_in_convertors_class():
    """
    test that AllConvertors class has a list with convertor names
    """
    assert isinstance(AllConvertors.names, list)
    for convertor_name in AllConvertors.names:
        assert isinstance(convertor_name, str)


def test_register_convertor():
    """
    Test that a new convertor after being registered is in the
    list of convertors and that the convertor name can be used
    as an attribute to get the convertor class.
    """
    class NewConvertor(AbstractConvertor):
        convertor_name = 'TEST'

        @staticmethod
        def _result_with_data_field() -> GetDataResponse:
            """ private method to do the actual data coversion """
            return

    AllConvertors.register_convertor(NewConvertor)
    assert 'TEST' in AllConvertors.names
    assert getattr(AllConvertors, 'TEST') is NewConvertor
