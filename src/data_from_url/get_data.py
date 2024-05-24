"""
Module to define the main classes for the get data module
"""

from .logical_api import LogicalApi
from .proxy import GetProxiedQueryParams
from .settings.dataclass import GetDataResponse, QueryParams


class GetData:
    """[summary]

    returns:
        - tuple (reponse, valid, error)
            response: response object from requests module (if available)
            valid (bool): True if proper response was obtained
            error (list[str]): list of error codes if no proper response was
                               obtained
    """

    @classmethod
    def result(cls, query_params: dict) -> GetDataResponse:
        """Method to retrieve

        Args:
            query_params (dict): [description]

        Returns:
            tuple: [description]
        """
        query_params = cls.validate_query_params(query_params=query_params)
        # replace query parmams by query_params that will use a proxy
        query_params = GetProxiedQueryParams.get_query_params(query_params)

        return LogicalApi.result(query_params)

    @staticmethod
    def validate_query_params(query_params: dict) -> dict:
        """
        validates if query params contains all required fields and only allowed
        values
        """
        return QueryParams(**query_params).model_dump()
