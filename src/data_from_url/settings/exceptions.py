"""
Module to define customer get_data excpetions

exceptions
- InvalidConvertorRequested
- InvalidConvertorType
"""


class InvalidConvertorRequested(Exception):
    def __init__(self, convertor):
        message = f'Unknown convertor `{convertor}` requested'
        super().__init__(message)


class InvalidConvertorType(Exception):
    def __init__(self, convertor):
        message = ''.join([
            f'Invalid convertor type `{type(convertor)}` given. ',
            'Convertor must be of type `str` or `AbstractConvertor`'
        ])
        super().__init__(message)
