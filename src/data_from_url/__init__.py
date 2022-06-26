"""
Module Get Data
Retrieving data from a URL or API via a basic set of parameters.

Main usage:

    >>> from get_data.retrieve import DataFromAPIorURL
    >>> result = DataFromAPIorURL.data(query_params, convertor)
    >>> result.is_valid
    True
    >>> result.data
    {... result data ...}

where
    - result: object of type GetDataResponse that represents the result of the
              the data retrieval (both in case of succes and error)
    - query_params: dict describing the api or html page from where to retrieve
                    the data. Both how and from which api/html page to retrieve
                    the data
    - convertor: defines how a succesfull response needs to be converted. A
                 custom Converter Class can be provided but there also a number
                 of default convertors that can be used.


result
~~~~~~
The result object is of type GetDataResponse (named Tuple)
and has the following attributes:
    - response (requests.Response):
        contains the response from the request made to the HTML page / API
    - is_valid (boolean):
        true if
            * response is compliant with expected status code
            * and required data conversion was succesfull
    - data (dict or str):
        contains the converted data from the response object. The conversion
        should always turn the data into a dictionary or string. See section
        convertors for more details.
    - error_msg (list of ErrorCode)
        all errors that were received during the request and dataconversion.
        See error section for more details and description of the Error class.

query_params
~~~~~~~~~~~~
Query_params defining the request
    - url (str): describes the url to be retrieved
    - headers (dict): headers to be send with the request. If not provided
                      a default Header will be send with the request
    - params (dict): request params to be send with the request
    - data (dict): body to be send with POST request
    - method (str): request method, defaults to GET
    - expected_status_code (list[int]): status codes allowed for the response
    - proxy (str): Indicate which proxy service needs to be used. See proxy
                   section. Defaults to using no proxy

Convertor parameters
    - convertor_params (dict): set of parameters used to instruct the convertor
                               class on how to run the conversion. Not all
                               convertors need convertor_params. See convertor
                               section

Query_params specific to the use of the Retry class in the requests module. For
more details see requests module documentation
    - status_forcelist (set): Set of response codes that will trigger a retry.
                              Defaults to (500, 502, 504)
    - backoff_factor (float): backoff_factor defaults to 0.3
    - retries (in): max number of retries defaults to 3

all needed parameters should be added to a single dict to be provided as
query_params argument to the DataFromAPIorURL.data method

convertors
~~~~~~~~~
The Get Data module by default provides the following set of convertors
    CSV, XML, JSON, JSON_FROM_HTML, TEXT

    XML
    ~~~
    Converts a XML response into a dict format. No convertor_params needed.

    JSON
    ~~~
    Converts a JSON response into a dict format. No convertor_params needed.

    TEXT
    ~~~
    Returns the response text. No convertor_params needed.

    CSV
    ~~~
    Converts a CSV response into a list of dicts. For each row a dict is
    created. First row of CSV response defines the keys of all dicts
    is used to define the keys of the dict.
        convertor_params fields:
            - delimiter (str): delimiter to be used for processing the CSV

    JSON_FROM_HTML
    ~~~~~~~~~~~~~~
    Extracts a JSON data set from the html. The location of the data set is
    given in the convertor_params :
        - json_begin (str) :
            location after which the json string starts. This paramenter needs
            to be exact and exlcuding the first position of the json str
        - json_end (str) :
            location before which the json string ends. This paramenter needs
            to be exact and exlcuding the last position of the json str
        - json_within_quotes (bool): defaults to False
            if set to True the json string will be retrieved between the first
            " after json_begin and the last " before json_end. If set to True
            json_begin and json_end do not need to be exact
        - escaped_quotes (bool): default to False
            if True will repalce any escaped " in the json string retrieved
            from the html
        - replace (dict):
            this dict with key value pairs of type str or bytes is used
            to make replacements in the retrieved json string. Each key
            will be replaced by its value

"""
from .convertors.csv_convertor import CSVConvertor
from .convertors.json_convertor import JSONConvertor
from .convertors.json_from_html_convertor import JSONFromHTMLConvertor
from .convertors.text_convertor import TextConvertor
from .convertors.xml_convertor import XMLConvertor
