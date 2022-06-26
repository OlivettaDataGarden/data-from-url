"""helper module for get_data module

decorators:
    - retry_after_connection_error

methods:
    - convert_params_to_url_ext
    - requests_retry_session
    - make_request_with_method
"""
import time

import requests
import unidecode
from requests.adapters import HTTPAdapter
from requests.exceptions import ChunkedEncodingError, ConnectionError, \
    ReadTimeout, RetryError
from requests.packages.urllib3.util.retry import Retry


def remove_none_values(input_dict: dict) -> dict:
    """ method to remove none values from input_dict """
    return {k: v for k, v in input_dict.items() if v is not None}


def convert_params_to_url_ext(params: dict) -> str:
    """
    Converts a set of params in a dict to a string that can be added to the
    request url.

    Args:
        params (dict): all params that need to be send with the request

    Returns:
        str: url extension in form of '?param1=a&param2=b...'
    """
    if not params:
        return ''

    url_ext = '?'
    for param, value in params.items():
        if not url_ext == '?':
            url_ext += '&'
        url_ext += param + '=' + str(value)

    return url_ext


def retry_after_connection_error(
        retries=5, waittime=3, return_value_on_fail=None):
    """Decorator method to retry requesy in case of Connection error

    Args:
        retries (int, optional):
            Nr of times the method/request needs to be retried before None is
            returned. Defaults to 5.
        waittime (int, optional):
            Waittime in seconds between two retries. Defaults to 30 seconds.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            """
            wrapper method to catch connection error exceptions
            """
            attempts = 0
            while attempts < retries:
                try:
                    return func(*args, ** kwargs)
                except (ConnectionError, ChunkedEncodingError,
                        ReadTimeout, RetryError):
                    attempts += 1
                    time.sleep(waittime * attempts)
            return return_value_on_fail
        return wrapper
    return decorator


def requests_retry_session(
        retries, backoff_factor, status_forcelist, session=None):
    """method to setup  a requests session

    Args:
        retries (int): Nr of retries.
        backoff_factor (float): Slow down on retry.
        status_forcelist (tuple, optional): Defaults to (500, 502, 504).
        session ([type], optional): Session to be used, Defaults to None.

    Returns:
        requests.Session
    """
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


def make_request_with_method(
        url, method, headers, retries=3, backoff_factor=1, timeout=60,
        status_forcelist=(500, 502, 504), data=None, params=None):

    query_p = {
        'url': url,
        'method': method,
        'headers': headers,
        'timeout': timeout,
        'data': data,
        'params': params
    }
    request_params = {k: v for k, v in query_p.items() if v is not None}

    response = requests_retry_session(
        retries=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist).request(**request_params)

    return response


def normalize_string(accented_string):
    """
    remove special characters form string and make lower case
    """
    unaccented_string = accented_string.replace('"', '')
    unidecoded_string = unidecode.unidecode(unaccented_string)
    return unidecoded_string.strip()
