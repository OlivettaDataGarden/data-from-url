"""
Module to define TextConvertor class for the get_data module
"""

from ..settings.dataclass import GetDataResponse
from .abstract_convertor import AbstractConvertor, AllConvertors


class TextConvertor(AbstractConvertor):
    """
    Class to add text form response to the data field of the GetDataResponse
    tuple
    """

    convertor_name = "TEXT"

    @classmethod
    def _result_with_data_field(
        cls, result: GetDataResponse, _=None
    ) -> GetDataResponse:
        """
        Extracts the text from the response and adds it to the results data
        field.

        Args:
            result (GetDataResponse): result from API call

        Returns:
            [GetDataResponse]: new GetDataResponse with data field filled
                               with response text
        """
        response = result.response
        text = response.text
        return GetDataResponse(
            response=response,
            is_valid=True,
            error_msg=[],
            data=text,
            io_time=result.io_time,
        )


AllConvertors.register_convertor(TextConvertor)
