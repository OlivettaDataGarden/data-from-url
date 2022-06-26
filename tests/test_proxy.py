"""
test methods for get_data module proxy
"""
import pytest
from imports import GetProxiedQueryParams, ScraperAPI


def test_get_proxied_query_params_without_proxy_returns_query_params():
    """
    test that GetProxiedQueryParams returns the query_params unchanged when
    no proxy parameter is provide
    """
    query_params = {'url': 'test'}
    assert GetProxiedQueryParams.get_query_params(
        query_params=query_params) == query_params


def test_proxy_argument_is_removed_from_query_params(mocker):
    """
    test that GetProxiedQueryParams returns the query_params where the
    proxy_argume
    """
    query_params = {'url': 'test', 'proxy': 'SCRAPERAPI'}
    new_query_params = GetProxiedQueryParams.get_query_params(
        query_params=query_params)
    assert 'proxy' not in new_query_params.keys()


def test_get_proxied_query_params_with_non_existing_proxy():
    """
    test that GetProxiedQueryParams raises value error if non existing
    proxy type is provided
    """
    with pytest.raises(ValueError):
        GetProxiedQueryParams.get_query_params(
            query_params={'proxy': 'DOES_NOT_EXIST'})


def test_get_proxied_query_params_calls_scraper_api_class(mocker):
    """
    test that GetProxiedQueryParams calls ScraperAPI when proxy argument
    set to `SCRAPERAPI`
    """
    scraper_api_spy = mocker.spy(ScraperAPI, 'query_params')
    GetProxiedQueryParams.get_query_params(
        query_params={'proxy': 'SCRAPERAPI', 'url': 'test'})
    assert scraper_api_spy.called


def test_get_proxied_query_params_returs_params_with_proxy_arg(mocker):
    """
    test that GetProxiedQueryParams return query_params without proxy
    argument
    """
    result = GetProxiedQueryParams.get_query_params(
        query_params={'proxy': 'SCRAPERAPI', 'url': 'test'})
    assert 'proxy' not in result.keys()
