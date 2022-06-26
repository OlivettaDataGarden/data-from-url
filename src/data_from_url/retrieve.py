"""Module to the interface to consumers of get_data module

classes:
- DataFromAPIorURL
"""
from typing import Union

from .convertors.abstract_convertor import AbstractConvertor, AllConvertors
from .settings import exceptions
from .settings.dataclass import GetDataResponse


class DataFromAPIorURL():
    """ Class to convert the response from url request into a data dict

    public class methods:
        - data:
            method to return the data as part of a named tuple
            `GetDataResponse` with attributes:
                - response   : holds the response object
                - is_valid   : set to True if response data could converted
                               into correct data dict
                - data       : holds data_dict result, is None when is_valid
                               is False
                - error_msg  : contains list of error codes and mesagges
                               empty when is_valid is True

    the data method is called with a set of query_params and a convertor type.
    The query_params are used to define what URL is called and in what way.

    'query_params': {
        'url': 'www.example.com/api',       # str defining full url
        'headers': settings.API_HEADER,     # dict with header params
        'data': str(payload),               # payload in str format
        'params': params,                   # url params in dict format
        'expected_status_code': 200,        # status code in int format
        'method': 'POST',                   # str defining method to be used
        'convertor_params': CONV_PARAMS},   # dict with convertor parameters
    'convertor': 'JSON'                     # str defining data type convertor
                                              to be used or custom Convertor
    }

    The 'convertor' attribute either contains a string indicating a default
    convertor or a custom convertor class subclassed from AbstractConvertor
    that can be imported from get_data.convertors.abstract_convertor. For some
    convertors additional arguments are needed. These should be provided as a
    dict in the query_params argument with key `convertor_params`.

    Default Convertors (with required/optional convertor_params) can be
    referenced by using the following values for the `convertor` attribute:

    - CSV: coverts a CSV from a url into a list of dicts {'result': [dict]}
        convertor_params arguments
            - delimiter             : Delimiter used in csv data
            - normalize_header      : Will convert header strings into ascii
                                      string. Optional, defaults to True
            - header_in_lower_case  : Will set header strings in lower case.
                                      Optional, defaults to True
            - values_in_lower_case  : Will set all values in lower case.
                                      Optional, defaults to False

    - JSON : coverts a JSON from a url into a dict
        convertor_params arguments
            none

    - TEXT : retrieves returns the plain text from a URL
        convertor_params arguments
            none
    """

    def __new__(cls):
        """ define this class a singleton class """
        return cls

    @classmethod
    def data(cls, query_params: dict,
             convertor: Union[str, AbstractConvertor]) -> GetDataResponse:
        """ dispatch the data request to the required data convertor class """
        convertor_class = None

        if isinstance(convertor, AbstractConvertor):
            convertor_class = convertor

        if isinstance(convertor, str):
            convertor_class = cls._get_convertor_class(convertor)

        if not convertor_class:
            raise exceptions.InvalidConvertorType(convertor)

        return convertor_class.get_data(query_params)

    @classmethod
    def _get_convertor_class(cls, convertor: str) -> AbstractConvertor:
        if convertor not in AllConvertors.names:
            raise exceptions.InvalidConvertorRequested(convertor)

        return getattr(AllConvertors, convertor)
