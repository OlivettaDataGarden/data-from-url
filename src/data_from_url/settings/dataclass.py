"""
Module to define dataclasses for get_data module
"""

from typing import Any, List, Optional, Union

from pydantic import BaseModel, field_validator

from .enumerator import GetDataExceptions, RestMethod
from .settings import ALLOWED_EXPECTED_STATUS_CODES, DEFAULT_HEADER


class GetDataResponse(BaseModel):
    response: Any
    is_valid: Optional[bool]
    error_msg: Any
    data: Any
    io_time: float = 0


class QueryParams(BaseModel):
    """data class to define QueryParams for get_data module"""

    url: str
    headers: dict = DEFAULT_HEADER
    method: str = "GET"
    expected_status_code: List[int]
    # data (body) object can also be string in order to allow for complex
    # GraphQL queries to be provided as string
    data: Optional[Union[dict, str]] = None
    params: Optional[dict] = None
    proxy: Optional[str] = None
    status_forcelist: set = {500, 502, 504}
    backoff_factor: float = 0.3
    retries: int = 3

    @field_validator("method")
    def method_must_be_valid(cls, value):
        """check method argument has a valid value"""
        if value not in RestMethod.values():
            raise ValueError(GetDataExceptions.INVALID_METHOD.value)
        return value

    @field_validator("expected_status_code", mode="before")
    def status_code_to_list(cls, value):
        """status code should be list[int]
        this method makes a list from it when int is provided
        """
        if isinstance(value, int):
            return [value]
        return value

    @field_validator("expected_status_code")
    def check_expected_status_code(cls, status_codes: list[int]):
        """method to check if expected status codes are allowed"""
        incorrect_status_codes = [
            status_code
            for status_code in status_codes
            if status_code not in ALLOWED_EXPECTED_STATUS_CODES
        ]
        if incorrect_status_codes:
            raise ValueError(f"Status codes {incorrect_status_codes} not allowed.")

        return status_codes
