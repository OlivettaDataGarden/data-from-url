"""
Module to define JSONConvertor class for the get_data module
"""
from xml.parsers.expat import ExpatError

import xmltodict
from errors.error import ListErrors

from ..settings.dataclass import GetDataResponse
from .abstract_convertor import AbstractConvertor, AllConvertors


class XMLConvertor(AbstractConvertor):
    """Class to add XML as a dict to the GetDataResponse tuple
    """

    convertor_name = 'XML'

    @classmethod
    def _result_with_data_field(cls, result, _=None):
        """
        Extracts the JSON from the response and adds it to the results data
        field. If no proper JSON can be retrieved from response object in
        `result` argument the status of result is set to invalid and an error
        code is added.

        Args:
            result (GetDataResponse): result from API call

        Returns:
            [GetDataResponse]: new GetDataResponse with data field or status
                               and error field updated
        """
        response = result.response
        try:
            xml_text = response.content
            xml_dict = xmltodict.parse(xml_text)
            return GetDataResponse(
                response=response, is_valid=True, error_msg=[], data=xml_dict,
                io_time=result.io_time)

        except ExpatError:
            return GetDataResponse(
                response=response, is_valid=False, data=None,
                error_msg=[ListErrors.INVALID_XML_IN_RESPONSE],
                io_time=result.io_time)


AllConvertors.register_convertor(XMLConvertor)
