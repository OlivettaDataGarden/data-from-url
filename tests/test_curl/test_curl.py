from urllib.parse import ParseResult

from pydantic import TypeAdapter

from data_from_url.processor.curl import ConvertCurl, decode_str, is_graph_ql_payload

from .curl_example import (
    AH,
    AUDI,
    DECODE_TEST_CASES,
    ENCODED_URL,
    HEADER_STR_EX1,
    HEADER_STR_EX2,
    SIMPLE_GET_CURL,
    SIMPLE_GET_CURL_SINGLE_URL_QUERY_PARAM,
)

CURL_ENTRIES_TYPE = TypeAdapter(list[str])


def test_convert_curl_class_exists():
    """test that ConvertCurl exists"""
    assert ConvertCurl


def test_instantiantiation_with_curl_str():
    """test that ConvertCurl can be instantiated with curl str"""
    inst = ConvertCurl(AH)
    assert inst._curl_command == AH
    assert inst._payload is not None
    assert inst._payload[0]["operationName"] == "storesListResults"
    assert inst._graph_ql_api
    assert inst._method == "POST"
    assert inst._convertor == "JSON"


def test_instantiantiation_sets_correct_attributes():
    inst = ConvertCurl(SIMPLE_GET_CURL)
    assert CURL_ENTRIES_TYPE.validate_python(inst._curl_entries)
    assert isinstance(inst._url_parse_result, ParseResult)
    assert inst._headers == {"accept": "*/*"}
    assert inst._url_params == {"other": "test", "test": "1"}
    assert inst._payload is None
    assert inst._graph_ql_api is False
    assert inst._method == "GET"


def test_curl_entries_method():
    list_curl_entries = ConvertCurl(SIMPLE_GET_CURL)._get_curl_entries()
    assert CURL_ENTRIES_TYPE.validate_python(list_curl_entries)
    assert len(list_curl_entries) == 4


def test_curl_entries_attribute_is_set():
    inst = ConvertCurl(SIMPLE_GET_CURL)
    assert CURL_ENTRIES_TYPE.validate_python(inst._curl_entries)


def test_header_method():
    header = ConvertCurl(SIMPLE_GET_CURL)._get_header()
    assert header == {"accept": "*/*"}


def test_key_value_from_header_field_ex1():
    key, value = ConvertCurl.key_value_from_header_field(HEADER_STR_EX1)
    assert key == "cookie"
    assert "cookie-consent" in value


def test_key_value_from_header_field_ex2():
    key, value = ConvertCurl.key_value_from_header_field(HEADER_STR_EX2)
    assert key == "priority"
    assert value == "u=1, i"


def test_decode_str():
    for input_str, expected_output in DECODE_TEST_CASES:
        # Check if the function's output matches the expected output
        assert decode_str(input_str) == expected_output, f"Failed on input: {input_str}"


def test_get_url():
    url = ConvertCurl(SIMPLE_GET_CURL)._get_url()
    assert url
    assert url.netloc == "test.nl"
    assert url.scheme == "https"


def test_check_url_method_ex1():
    url = ConvertCurl._check_if_str_is_url("'https://test.nl'")
    assert isinstance(url, ParseResult)


def test_check_url_method_ex2():
    url = ConvertCurl._check_if_str_is_url("https://test.nl")
    assert url
    assert url.netloc == "test.nl"


def test_check_url_method_ex3():
    url = ConvertCurl._check_if_str_is_url("https://test.nl?params=test&other=3")
    assert url
    assert url.query == "params=test&other=3"


def test_ecoded_url():
    url = ConvertCurl._check_if_str_is_url(ENCODED_URL)
    assert url
    assert "pb=!1m5!1m4!1i12!2i2099!" in url.query


def test_get_clean_url():
    inst = ConvertCurl(SIMPLE_GET_CURL)
    clean_url = inst._get_clean_url()
    assert clean_url == "https://test.nl"


def test_invalid_url():
    url = ConvertCurl._check_if_str_is_url("no url")
    assert url is None


def test_get_url_params():
    inst = ConvertCurl(SIMPLE_GET_CURL)
    assert inst._get_url_params() == {"other": "test", "test": "1"}


def test_get_url_params_ex2():
    inst = ConvertCurl(SIMPLE_GET_CURL_SINGLE_URL_QUERY_PARAM)
    assert inst._get_url_params() == {"test": "1"}


def test_get_url_params_no_params():
    inst = ConvertCurl(AH)
    assert inst._get_url_params() == {}


def test_get_payload_for_curl_without_payload():
    inst = ConvertCurl(SIMPLE_GET_CURL)
    assert inst._get_payload() is None


def test_get_payload_for_curl_with_payload():
    inst = ConvertCurl(AUDI)
    payload = inst._get_payload()
    assert payload
    assert payload["operationName"] is not None
    assert payload["variables"] is not None
    assert payload["query"] is not None
    assert inst._graph_ql_api is True


def test_is_graph_ql_payload_true():
    assert is_graph_ql_payload(
        {"operationName": "a", "variables": {"a": 1}, "query": "a"}
    )


def test_is_graph_ql_payload_false():
    assert (
        is_graph_ql_payload(
            {"operationName": "a", "non_correct_key": {"a": 1}, "query": "b"}
        )
        is False
    )

def test_is_graph_ql_payload_false_no_dict():
    assert (
        is_graph_ql_payload("operationName")     # type: ignore
    ) is False

def test_data_for_url_params():
    inst = ConvertCurl(AH)
    
    data_for_url_params = inst.data_for_url_params()
    assert data_for_url_params
    assert data_for_url_params["convertor"] == "JSON"
    assert data_for_url_params["query_params"].url == inst._url

