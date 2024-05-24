"""
Module to provide scraper classes to transform query params into query params
that make use of a specific scraper.

Scrapers supported
    - ScraperAPI - www.scraperapi.com

Public class:
    - GetProxiedQueryParams

"""

from .helper import convert_params_to_url_ext
from .settings.credentials import SCRAPER_API_KEY
from .settings.enumerator import GetDataExceptions
from .settings.settings import SCRAPER_API_NAME, SCRAPER_API_URL


class ScraperAPI:
    """
    Class to transform input query params to query params that will do execute
    the required request via the extrenal ScraperAPI proxy

    Public class method:
        query_params - returns the ScraperAPI specific query params
    """

    @classmethod
    def query_params(cls, query_params: dict) -> dict:
        """creates query params specific to ScraperAPI requirements"""
        return query_params | {
            "url": SCRAPER_API_URL,
            "params": cls._params(query_params),
        }

    @staticmethod
    def _params(query_params: dict) -> dict:
        """Method to generate the params argument for ScraperAPI requests"""
        url = query_params["url"]
        url += convert_params_to_url_ext(params=query_params.get("params"))
        params = {"api_key": SCRAPER_API_KEY}
        params.update({"keep_headers": "true"})
        params.update({"url": url})
        return params


class GetProxiedQueryParams:
    """
    Class to select the requested Scraper class in order to retrieve the
    query_params needed for that scraper class.

    Public class method:
        query_params - returns the query params specific to the scraper type
    """

    @classmethod
    def get_query_params(cls, query_params: dict) -> dict:
        """method to tranform input query params to query params for proxy

        arguments:
            - query_params (dict): query_params for api/url to retrieve

        returns:
            - dict : query_params for api/url to retrieve via proxy

        raises:
            - ValueError when proxy name in query_params is unknown
        """
        proxy_name = query_params.pop("proxy", None)

        if not proxy_name:
            return query_params

        if proxy_name == SCRAPER_API_NAME:
            return ScraperAPI.query_params(query_params)

        raise ValueError(GetDataExceptions.INVALID_PROXY)
