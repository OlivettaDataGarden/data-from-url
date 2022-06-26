"""
Module to provide the abstract convertor class for the get data module

The convertor class is reponsible for converting the reponse format into a
specific format (usually a dict)

As API's can return response data objects in XML, HTML, csv, JSON etc.
the implementation of this abstract convertor class takes care of converting
the response data into the required data object (usually a dict)
"""
from abc import ABCMeta, abstractmethod

from ..get_data import GetData
from ..settings.dataclass import GetDataResponse
from ..settings.enumerator import GetDataExceptions


class AbstractConvertor(metaclass=ABCMeta):
    """ Abstract Convertor class

    implementations of the AbstractConvertor must implement

    _result_with_data_field()

    which converts adds the data field to the GetDataResponse object if
    that object is valid. If conversion can not be done succesfully the
    status of GetDataResponse should be set to invalid and a proper error
    code should be added to er the errors_msg field

    implementations of the AbstractConvertor can override

    _validate_convertor_params

    by default this validation requires the convertor_params to be None. When
    convertor_params are required override this method with specific validation
    """

    @classmethod
    def get_data(cls, query_params: dict) -> GetDataResponse:
        """ public method to used to retrieve GetDataResponse object """
        convertor_params = query_params.pop('convertor_params', None)
        cls._validate_convertor_params(convertor_params)
        result = GetData.result(query_params)
        if not result.is_valid:
            return result
        return cls._result_with_data_field(result, convertor_params)

    @staticmethod
    @abstractmethod
    def _result_with_data_field() -> GetDataResponse:
        """ private method to do the actual data coversion """

    @staticmethod
    def _validate_convertor_params(convertor_params) -> None:
        """ private method to validate convertor_params argumemt

        by default this format params method checks that no params are
        provided. When actual validation is needed override this method

        args:
            - convertor_params (None or Dict):

        returns:
            - None

        raises:
            - ValueError: if convertor_params is not valid
        """
        if convertor_params is None:
            return

        raise ValueError(GetDataExceptions.INVALID_RESPONSE_CONVERTOR_PARAMS)


class AllConvertors():

    names = []

    @classmethod
    def register_convertor(cls, convertor: AbstractConvertor) -> None:
        """
        Method to register
        """
        name = convertor.convertor_name
        cls.names.append(name)
        setattr(cls, name, convertor)
