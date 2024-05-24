"""
test methods for get_data module get_data

"""

import pytest
from data.test_data import DEFAULT_QUERY_PARAMS, QUERY_PARAMS_WITH_PROXY
from imports import GetData, GetProxiedQueryParams, LogicalApi


def test_get_data_class_exists():
    """test that GetData exists"""
    assert GetData


def test_get_data_result_method_with_no_query_params():
    """
    test that GetData result class method raises value error
    if no query_params are provided
    """
    with pytest.raises(ValueError):
        GetData.result(query_params={})


def test_get_data_resul_method_calls_query_params_validator(mocker):
    """
    test that Proxy does not call GetProxiedQueryParams without proxy arg
    """
    mocker.patch(
        "data_from_url.proxy.GetProxiedQueryParams.get_query_params", return_value=None
    )
    mocker.patch("data_from_url.logical_api.LogicalApi.result", return_value=None)
    validate_query_params_spy = mocker.spy(GetData, "validate_query_params")
    GetData.result(query_params=DEFAULT_QUERY_PARAMS)
    assert validate_query_params_spy.called


def test_logical_api_called_without_proxy_argument(mocker):
    """
    test that Proxy does not call GetProxiedQueryParams without proxy arg
    """
    mocker.patch(
        "data_from_url.proxy.GetProxiedQueryParams.get_query_params", return_value=None
    )
    mocker.patch("data_from_url.logical_api.LogicalApi.result", return_value=None)
    logical_api_result_spy = mocker.spy(LogicalApi, "result")
    GetData.result(query_params=DEFAULT_QUERY_PARAMS)
    assert logical_api_result_spy.called


def test_proxied_queries_called_without_proxy_argument(mocker):
    """
    test that Proxy does not call GetProxiedQueryParams without proxy arg
    """
    mocker.patch(
        "data_from_url.proxy.GetProxiedQueryParams.get_query_params", return_value=None
    )
    mocker.patch("data_from_url.logical_api.LogicalApi.result", return_value=None)
    proxy_query_params_spy = mocker.spy(GetProxiedQueryParams, "get_query_params")
    GetData.result(query_params=DEFAULT_QUERY_PARAMS)
    assert proxy_query_params_spy.called


def test_proxied_queries_called_with_proxy_argument(mocker):
    """test that GetData calls GetProxiedQueryParams with proxy argument"""
    mocker.patch(
        "data_from_url.proxy.GetProxiedQueryParams.get_query_params", return_value=None
    )
    mocker.patch("data_from_url.logical_api.LogicalApi.result", return_value=None)
    proxy_query_params_spy = mocker.spy(GetProxiedQueryParams, "get_query_params")
    GetData.result(query_params=QUERY_PARAMS_WITH_PROXY)
    assert proxy_query_params_spy.called


def test_logical_api_called_with_proxy_argument(mocker):
    """
    test that GetaData called with proxy arg calls LogicalApi result method
    """
    mocker.patch(
        "data_from_url.proxy.GetProxiedQueryParams.get_query_params", return_value=None
    )
    mocker.patch("data_from_url.logical_api.LogicalApi.result", return_value=None)
    logical_api_result_spy = mocker.spy(LogicalApi, "result")
    GetData.result(query_params=QUERY_PARAMS_WITH_PROXY)
    assert logical_api_result_spy.called
