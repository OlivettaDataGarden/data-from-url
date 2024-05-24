"""
test methods for get_data module proxy
"""
from data.test_data import DEFAULT_GET_DATA_RESPONSE, DEFAULT_QUERY_PARAMS, \
    INVALID_GET_DATA_RESPONSE
from errors.error import ListErrors
from imports import GetDataResponse, LogicalApi
from requests.exceptions import ConnectionError


def test_logical_api_class_exists():
    """ test that LogicalApi exists """
    assert LogicalApi()


def test_result_method_calls_do_request(mocker):
    """ test that LogicalApi result class method call _do_request method """
    mocker.patch('data_from_url.logical_api.LogicalApi._do_request',
                 return_value=DEFAULT_GET_DATA_RESPONSE)
    do_request_spy = mocker.spy(LogicalApi, '_do_request')
    LogicalApi.result(DEFAULT_QUERY_PARAMS.copy())
    assert do_request_spy.called


def test_result_method_calls_check_status_code_when_valid_result(mocker):
    """
    test that LogicalApi result class method calls _check_status_code method
    when result status is_valid
    """
    mocker.patch('data_from_url.logical_api.LogicalApi._do_request',
                 return_value=DEFAULT_GET_DATA_RESPONSE)
    _check_status_code_spy = mocker.spy(LogicalApi, '_check_status_code')
    LogicalApi.result(DEFAULT_QUERY_PARAMS.copy())
    assert _check_status_code_spy.called


def test_does_not_call_check_status_code_when_invalid_result(mocker):
    """
    test that LogicalApi result class method does not calls _check_status_code
    method when result status is_valid
    """
    mocker.patch('data_from_url.logical_api.LogicalApi._do_request',
                 return_value=INVALID_GET_DATA_RESPONSE)
    _check_status_code_spy = mocker.spy(LogicalApi, '_check_status_code')
    LogicalApi.result(DEFAULT_QUERY_PARAMS.copy())
    assert not _check_status_code_spy.called


def test_do_request_returns_get_data_response(mocker):
    """
    test that LogicalAPI method _do_request returns a GetDataResponse object in
    case of succesfull response
    """
    mocker.patch('data_from_url.logical_api.make_request_with_method',
                 return_value='Succes')
    result = LogicalApi._do_request(url='test', method='GET', headers={})
    assert result.response == 'Succes'
    assert isinstance(result, GetDataResponse)


def test_do_request_returns_get_data_response_with_connection_error(mocker):
    """
    test that LogicalAPI method _do_request returns a GetDataResponse object
    also in case of connection error
    """
    mocker.patch('data_from_url.logical_api.make_request_with_method',
                 side_effect=ConnectionError)
    mocker.patch('data_from_url.helper.time.sleep', return_value=None)
    result = LogicalApi._do_request(url='test', method='GET', headers={})
    assert not result.is_valid
    assert ListErrors.CONNECTIVITY_ERROR in result.error_msg
    assert isinstance(result, GetDataResponse)


def test_check_status_code_returns_get_data_response(mocker):
    """
    test that _check_status_code returns GetDataResponse as is when response
    has expected status code
    """
    print(DEFAULT_GET_DATA_RESPONSE.response.status_code)
    result = LogicalApi._check_status_code(
        result=DEFAULT_GET_DATA_RESPONSE, expected_status_code=[200])
    assert result is DEFAULT_GET_DATA_RESPONSE


def test_unexpected_status_code_returns_invalid_get_data_response(mocker):
    """
    test that _check_status_code returns invalidated GetDataResponse when
    response does have a different status code then expected
    """
    result = LogicalApi._check_status_code(
        result=DEFAULT_GET_DATA_RESPONSE, expected_status_code=[201])
    assert not result.is_valid
    assert 'unexpected statuscode 200' in str(result.error_msg)
