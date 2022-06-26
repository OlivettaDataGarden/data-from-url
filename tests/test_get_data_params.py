"""
Test module to test GetDataParams data class
"""
import pytest
from data.test_data import DEFAULT_QUERY_PARAMS
from imports import GetDataParams


def test_data_class_get_data_params_exists():
    """
    test that GetDataParams exists
    """
    assert GetDataParams


def test_instantiate_get_data_params():
    """
    test that GetDataParams contains all field in DEFAULT_QUERY_PARAMS
    """
    get_data_params = GetDataParams(**DEFAULT_QUERY_PARAMS)
    for field, field_value in DEFAULT_QUERY_PARAMS.items():
        assert field_value == getattr(get_data_params, field)


def test_get_data_params_succes_with_known_convertor():
    """
    test that GetDataParams does not allow for an unregistered convertor.
    """
    get_data_inp_params = DEFAULT_QUERY_PARAMS.copy() | {
        'convertor': 'XML'}

    assert GetDataParams(**get_data_inp_params).convertor == 'XML'


def test_get_data_params_fails_with_unkown_convertor():
    """
    test that GetDataParams does not allow for an unregistered convertor.
    """
    get_data_inp_params = DEFAULT_QUERY_PARAMS.copy() | {
        'convertor': 'UNKNOWN'}
    with pytest.raises(ValueError) as value_error:
        GetDataParams(**get_data_inp_params)

    assert 'not registered' in str(value_error)


def test_get_data_params_with_known_request_method():
    """
    test that GetDataParams does not allow for an unknown request method.
    """
    get_data_inp_params = DEFAULT_QUERY_PARAMS.copy() | {
        'method': 'POST'}
    assert GetDataParams(**get_data_inp_params).method == 'POST'


def test_get_data_params_fails_with_unknown_request_method():
    """
    test that GetDataParams does not allow for an unknown request method.
    """
    get_data_inp_params = DEFAULT_QUERY_PARAMS.copy() | {
        'method': 'UNKNOWN METHOD'}
    with pytest.raises(ValueError) as value_error:
        GetDataParams(**get_data_inp_params)

    assert "Method should be one of" in str(value_error)


def test_get_data_params_fails_with_invalid_url():
    """
    test that GetDataParams does not allow for an unknown request method.
    """
    get_data_inp_params = DEFAULT_QUERY_PARAMS.copy() | {
        'url': 'invalid'}
    with pytest.raises(ValueError) as value_error:
        GetDataParams(**get_data_inp_params)

    assert "Invalid url provided." in str(value_error)


def test_format_params_returns_a_dict():
    """
    test that format_params method returns a dict.
    """
    get_data_params = GetDataParams(**DEFAULT_QUERY_PARAMS).format_params()
    assert isinstance(get_data_params, dict)


def test_format_params_returns_a_dict_with_query_params_key():
    """
    test that format_params method returns a dict.
    """
    get_data_params = GetDataParams(**DEFAULT_QUERY_PARAMS).format_params()
    assert get_data_params.get('query_params', False)


def test_format_params_returns_a_dict_with_a_convertor_key():
    """
    test that format_params method returns a dict.
    """
    get_data_params = GetDataParams(**DEFAULT_QUERY_PARAMS).format_params()
    assert get_data_params.get('convertor', False)


def test_format_params_returns_a_dict_where_convertor_key_not_in_q_p():
    """
    test that format_params method returns a dict with query_params key that
    contains a dict without convertor key
    """
    get_data_params = GetDataParams(**DEFAULT_QUERY_PARAMS).format_params()
    query_params = get_data_params.get('query_params', False)
    assert query_params
    assert not query_params.get('query_params', False)
