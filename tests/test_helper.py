"""
test methods for get_data module helper
"""

import requests
from imports import (
    CONNECTIVITY_ERROR_RESPONSE,
    GetDataResponse,
    ListErrors,
    convert_params_to_url_ext,
    helper,
    make_request_with_method,
    normalize_string,
    requests_retry_session,
    retry_after_connection_error,
)
from requests.exceptions import (
    ChunkedEncodingError,
    ConnectionError,
    ReadTimeout,
    RetryError,
)


def test_convert_params_to_url_ext_with_params_none_returns_empty_str():
    """
    test that convert_params_to_url_ext method returns an empty str when
    params is None
    """
    params = None
    assert convert_params_to_url_ext(params) == ""


def test_convert_params_to_url_ext_with_empty_params_returns_empty_str():
    """
    test that convert_params_to_url_ext method returns an empty str when
    params is None
    """
    params = {}
    assert convert_params_to_url_ext(params) == ""


def test_convert_params_to_url_ext_with_1_key_value():
    """
    test that convert_params_to_url_ext method returns requests params as str
    """
    params = {"key": "value"}
    assert convert_params_to_url_ext(params) == "?key=value"


def test_convert_params_to_url_ext_with_2_key_values():
    """
    test that convert_params_to_url_ext method returns requests params as a
    string seperated by `&`
    """
    params = {"key1": "value1", "key2": "value2"}
    assert convert_params_to_url_ext(params) == "?key1=value1&key2=value2"


def test_retry_after_connection_error():
    """test if decorator calls provide method"""

    @retry_after_connection_error()
    def req_method(*args, **kwargs):
        return "method_was_called"

    assert req_method() == "method_was_called"


def test_retry_after_connection_error_with_connection_error_1():
    """
    test if decorator returns connnectivity error when ConnectionError is
    raised
    """

    @retry_after_connection_error(
        retries=3, waittime=0, return_value_on_fail=CONNECTIVITY_ERROR_RESPONSE
    )
    def req_method(*args, **kwargs):
        raise ConnectionError

    result = req_method()
    assert isinstance(result, GetDataResponse)
    assert not result.is_valid
    assert ListErrors.CONNECTIVITY_ERROR in result.error_msg


def test_retry_after_connection_error_with_connection_error_2():
    """
    test if decorator returns connnectivity error when ChunkedEncodingError is
    raised
    """

    @retry_after_connection_error(
        retries=3, waittime=0, return_value_on_fail=CONNECTIVITY_ERROR_RESPONSE
    )
    def req_method(*args, **kwargs):
        raise ChunkedEncodingError

    assert ListErrors.CONNECTIVITY_ERROR in req_method().error_msg


def test_retry_after_connection_error_with_connection_error_3():
    """
    test if decorator returns connnectivity error when ReadTimeout is
    raised
    """

    @retry_after_connection_error(
        retries=3, waittime=0, return_value_on_fail=CONNECTIVITY_ERROR_RESPONSE
    )
    def req_method(*args, **kwargs):
        raise ReadTimeout

    assert ListErrors.CONNECTIVITY_ERROR in req_method().error_msg


def test_retry_after_connection_error_with_connection_error_4():
    """
    test if decorator returns connnectivity error when RetryError is
    raised
    """

    @retry_after_connection_error(
        retries=3, waittime=0, return_value_on_fail=CONNECTIVITY_ERROR_RESPONSE
    )
    def req_method(*args, **kwargs):
        raise RetryError

    assert ListErrors.CONNECTIVITY_ERROR in req_method().error_msg


def test_requests_retry_session():
    """test requests_retry_session returns a Session object"""
    session_params = {"retries": 3, "backoff_factor": 1, "status_forcelist": (500)}
    assert isinstance(requests_retry_session(**session_params), requests.Session)


def test_requests_retry_session_returns_correct_retry_values():
    """
    test requests_retry_session returns a Session object with correct Retry
    values
    """
    session = requests_retry_session(
        retries=1, backoff_factor=1, status_forcelist=(500)
    )
    retry = session.adapters["https://"].max_retries
    assert retry.total == 1
    assert retry.backoff_factor == 1
    assert retry.status_forcelist == (500)


def test_requests_retry_session_updates_retry_values():
    """
    test requests_retry_session updates a Session object with correct Retry
    values
    """
    session = requests_retry_session(
        retries=1, backoff_factor=1, status_forcelist=(500)
    )
    updated_session = requests_retry_session(
        session=session, retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504)
    )
    retry = updated_session.adapters["https://"].max_retries
    assert retry.total == 3
    assert retry.backoff_factor == 0.3
    assert retry.status_forcelist == (500, 502, 504)


def test_make_request_with_method_calls_retry_session(mocker):
    """
    test make_request_with_method calls requests_retry_session
    """
    mocker.patch("requests.Session.request", return_value="succes")
    request_retry_session_spy = mocker.spy(helper, "requests_retry_session")
    make_request_with_method(url="http://www.google.com", method="GET", headers={})
    assert request_retry_session_spy.called


def test_make_request_with_method_make_a_request(mocker):
    """
    test make_request_with_method calls Sessions.request method
    """
    mocker.patch("requests.Session.request", return_value="succes")
    session_request_spy = mocker.spy(requests.Session, "request")
    result = make_request_with_method(
        url="http://www.google.com", method="GET", headers={}
    )
    assert session_request_spy.called
    assert result == "succes"


def test_normalize_string():
    """
    test normalized strimng method strips the string, removes `"` and converts
    all characters to ASCII
    """
    assert "eabcde" == normalize_string(' éab"cdé ')
