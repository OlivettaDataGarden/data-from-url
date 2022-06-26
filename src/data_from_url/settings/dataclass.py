"""
Module to define dataclasses for get_data module
"""
from collections import namedtuple
from typing import List, Union

from pydantic import BaseModel, validator

from .enumerator import GetDataExceptions, RestMethod
from .settings import ALLOWED_EXPECTED_STATUS_CODES, DEFAULT_HEADER

GetDataResponse = namedtuple(
    'GetDataResponse', 'response is_valid error_msg data io_time')


class QueryParams(BaseModel):
    """data class to define QueryParams for get_data module
    """
    url: str
    headers: dict = DEFAULT_HEADER
    method: str = 'GET'
    expected_status_code: List[int]
    # data (body) object can also be string in order to allow for complex
    # GraphQL queries to be provided as string
    data: Union[dict, str] = None
    params: dict = None
    proxy: str = None
    status_forcelist: set = (500, 502, 504)
    backoff_factor: float = 0.3
    retries: int = 3

    @validator('method')
    def method_must_be_valid(cls, v):
        """ check method argument has a valid value """
        if v not in RestMethod.values():
            raise ValueError(GetDataExceptions.INVALID_METHOD.value)
        return v

    @validator('expected_status_code', pre=True)
    def status_code_to_list(cls, v):
        """ status code should be list[int]
        this method makes a list from it when int is provided
        """
        if isinstance(v, int):
            return [v]
        return v

    @validator('expected_status_code', each_item=True)
    def check_expected_status_code(cls, v):
        """method to check if expected status codes are allowed"""
        assert v in ALLOWED_EXPECTED_STATUS_CODES
        return v
