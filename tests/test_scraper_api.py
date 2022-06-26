"""
test methods for get_data module scraper_api
"""
from data.test_data import DEFAULT_QUERY_PARAMS
from imports import ScraperAPI

import data_from_url.proxy


def test_scaper_api_class_exists():
    """ test that Proxy exists """
    assert ScraperAPI


def test_scaper_api_params_method_returns_url():
    """ test that the ScraperApi params method put requested url in params """
    params = ScraperAPI._params(query_params=DEFAULT_QUERY_PARAMS)
    assert params.get('url') == DEFAULT_QUERY_PARAMS.get('url')


def test_scaper_api_params_method_adds_params_to_url():
    """
    test that the ScraperApi params method copies params argument from
    query_params
    """
    additional_params = {'q1': 1, 'g2': 'test'}
    query_params = DEFAULT_QUERY_PARAMS | {'params': additional_params}
    params = ScraperAPI._params(query_params=query_params)
    assert params.get('url') == \
        DEFAULT_QUERY_PARAMS.get('url') + '?q1=1&g2=test'


def test_scaper_api_params_method_has_keep_headers_set_to_true():
    """ test that the ScraperApi params method set keep_headers to 'true'"""
    params = ScraperAPI._params(query_params=DEFAULT_QUERY_PARAMS)
    assert params.get('keep_headers') == 'true'


def test_scaper_api_params_method_sets_scraper_api_key(mocker):
    """ test that the ScraperApi params method sets API key properly"""
    mocker.patch.object(data_from_url.proxy, 'SCRAPER_API_KEY', 'test_key')
    params = ScraperAPI._params(query_params=DEFAULT_QUERY_PARAMS)
    assert params.get('api_key') == 'test_key'


def test_scaper_api_query_params_method_retruns_scraper_api_url(mocker):
    """ test that the ScraperApi query_params method scraperapi url"""
    mocker.patch.object(data_from_url.proxy, 'SCRAPER_API_URL', 'scraper_url')
    query_params = ScraperAPI.query_params(query_params=DEFAULT_QUERY_PARAMS)
    assert query_params.get('url') == 'scraper_url'
