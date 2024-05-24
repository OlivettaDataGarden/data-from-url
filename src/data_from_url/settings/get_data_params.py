""" """

from typing import Optional

from pydantic import BaseModel, Field, field_validator
from validators import url as url_is_valid

from ..convertors.abstract_convertor import AllConvertors
from .enumerator import GetDataExceptions, RestMethod


class GetDataParams(BaseModel):
    """data class to define GetDataParams for get_data module.

    Instances of GetDataParams can be used to call the ``data``
    method on ``DataFromAPIorURL`` class and define the html page or API
    details of the data object to be retrieved.
    """

    url: str
    convertor: str = "JSON"
    convertor_params: dict = Field(default_factory=dict)
    headers: dict = Field(default_factory=dict)
    params: dict = Field(default_factory=dict)
    proxy: Optional[str] = None
    expected_status_code: list = Field(default_factory=lambda: [200])
    method: str = "GET"

    @field_validator("method")
    def method_must_be_valid(cls, method) -> str:
        """check method argument has a valid value"""
        if method not in RestMethod.values():
            raise ValueError(GetDataExceptions.INVALID_METHOD.value)
        return method

    @field_validator("convertor")
    def convertor_must_be_known(cls, convertor: str) -> str:
        """check method argument has a valid value"""
        if convertor not in AllConvertors.names:
            raise ValueError(GetDataExceptions.UNKNOWN_CONVERTOR.value)
        return convertor

    @field_validator("url")
    def url_must_be_valid(cls, url: str) -> str:
        """check if url is valid"""
        if url_is_valid(url):
            return url
        raise ValueError(GetDataExceptions.INVALID_URL.value)

    def format_params(self) -> dict:
        """
        Method to return params in right format to be used for getdata.
        Usage:
            params = GetDataParams(**all_api_arguments)
            get_data_response = DataFromAPIorURL().data(**params.format_params)
        """
        query_params = self.model_dump()
        convertor = query_params.pop("convertor")
        return {"query_params": query_params, "convertor": convertor}
