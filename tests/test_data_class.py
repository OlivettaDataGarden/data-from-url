"""
test methods for get_data module dataclasses
"""
import pytest
from data.test_data import DEFAULT_QUERY_PARAMS
from imports import GetDataExceptions, QueryParams, RestMethod


def test_query_params_dataclass_exists():
    """
    test that QueryParams exists
    """
    assert QueryParams


def test_create_query_params_instance():
    """
    test that QueryParams can be create
    """
    assert QueryParams(**DEFAULT_QUERY_PARAMS)


def test_query_params_headers_is_dict():
    """
    test that QueryParams headers defaults to dict
    """
    assert isinstance(
        QueryParams(**DEFAULT_QUERY_PARAMS).headers,
        dict)


def test_query_params_default_method_is_get():
    """
    test that QueryParams method defaults to get
    """
    assert QueryParams(**DEFAULT_QUERY_PARAMS).method == \
        RestMethod.GET.value


def test_query_params_method_can_be_set_to_post():
    """
    test that QueryParams method can also be POST
    """
    query_params = DEFAULT_QUERY_PARAMS.copy()
    query_params['method'] = 'POST'
    assert QueryParams(**query_params).method == \
        RestMethod.POST.value


def test_query_params_raises_exception_with_unexcepted_method():
    """
    test that QueryParams data class raises exception for unexcepted method
    """
    query_params = DEFAULT_QUERY_PARAMS.copy()
    query_params['method'] = 'invalid'
    with pytest.raises(ValueError):
        QueryParams(**query_params)


def test_query_params_with_invalid_method():
    """
    test that QueryParams raises ValueError with invalid method
    """
    query_params = DEFAULT_QUERY_PARAMS | {'method': 'invalid'}
    with pytest.raises(ValueError) as validation_error:
        QueryParams(**query_params)
    assert GetDataExceptions.INVALID_METHOD.value in \
        str(validation_error)


def test_create_query_params_instance_without_url():
    """
    test that QueryParams without URL raise an Value error exception
    """
    query_params_without_url = DEFAULT_QUERY_PARAMS.copy()
    query_params_without_url.pop('url')
    with pytest.raises(ValueError):
        QueryParams(**query_params_without_url)


def test_create_query_params_without_expected_status_code():
    """
    test that QueryParams without expected_status_code raise a
    Value error exception
    """
    query_params_without_status_code = DEFAULT_QUERY_PARAMS.copy()
    query_params_without_status_code.pop('expected_status_code')
    with pytest.raises(ValueError):
        QueryParams(**query_params_without_status_code)


def test_create_query_params_not_allowed_expected_status_code():
    """
    test that QueryParams expected_status_code that is not allowed
    raises a Value error exception
    """
    query_params_with_not_allowed_status_code = DEFAULT_QUERY_PARAMS.copy()
    query_params_with_not_allowed_status_code['expected_status_code'] = [100]
    with pytest.raises(ValueError):
        QueryParams(**query_params_with_not_allowed_status_code)


def test_create_query_params_with_int_expected_status_code():
    """
    test that QueryParams valid expected_status_code as int is ok
    """
    query_params_with_int_allowed_status_code = DEFAULT_QUERY_PARAMS.copy()
    query_params_with_int_allowed_status_code['expected_status_code'] = 200
    assert QueryParams(**query_params_with_int_allowed_status_code)
