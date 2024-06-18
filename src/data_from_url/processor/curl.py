import json
import shlex
from urllib.parse import ParseResult, urlparse, urlunparse

from data_from_url import QueryParams

GRQL_PAYLOAD_KEYS = ["operationName", "variables", "query"]


def decode_str(str_to_decode: str) -> str:
    return bytes(str_to_decode, "utf-8").decode("unicode-escape")


def is_graph_ql_payload(payload: dict | list[dict]) -> bool:
    # payload can be a list of graph QL queries
    if isinstance(payload, list):
        return all([is_graph_ql_payload(graph_ql_item) for graph_ql_item in payload])
    if isinstance(payload, dict):
        return all([key in payload for key in GRQL_PAYLOAD_KEYS])
    return False


class ConvertCurl:
    def __init__(self, curl_command: str) -> None:
        self._curl_command = curl_command
        self._curl_entries = self._get_curl_entries()
        self._url_parse_result: ParseResult | None = self._get_url()
        self._headers = self._get_header()
        self._url = self._get_clean_url()
        self._url_params = self._get_url_params()
        self._payload = self._get_payload()
        self._graph_ql_api = is_graph_ql_payload(self._payload or {})
        self._method = "POST" if self._payload else "GET"
        self._convertor = "JSON"
        self._expected_status_code = [200]

    def data_for_url_params(self) -> dict | None:
        if not self._url:
            return None

        return {
            "query_params": QueryParams(
                url=self._url,
                headers=self._headers,
                method=self._method,
                expected_status_code=self._expected_status_code,
                params=self._url_params,
                data=self._payload,
            ),
            "convertor": self._convertor,
        }

    def _get_curl_entries(self) -> list[str]:
        return shlex.split(self._curl_command)

    def _get_payload(self) -> dict | None:
        for index, curl_entry in enumerate(self._curl_entries):
            if curl_entry in ["--data-raw"]:
                data_field = self._curl_entries[index + 1]
                if data_field[0] == "$":
                    data_field = decode_str(data_field[1:])
                data_field = data_field.replace("\n", " \\n")

                return json.loads(data_field)
        return None

    def _get_url_params(self) -> dict[str, str]:
        if not self._url_parse_result or not self._url_parse_result.query:
            return {}
        url_params_str = self._url_parse_result.query
        return {
            param_item.split("=")[0]: param_item.split("=")[1]
            for param_item in url_params_str.split("&")
        }

    def _get_clean_url(self) -> str | None:
        if not self._url_parse_result:
            return None
        parsed_url = self._url_parse_result
        return urlunparse(
            (parsed_url.scheme, parsed_url.netloc, parsed_url.path, "", "", "")
        )

    def _get_url(self) -> ParseResult | None:
        for curl_entry in self._curl_entries:
            try:
                possible_url_str = curl_entry.replace("'", "")
                result = urlparse(possible_url_str)
                if all([result.scheme, result.netloc]):
                    return result
            except ValueError:
                continue

        return None

    def _get_header(self) -> dict[str, str]:
        header = {}
        for index, curl_entry in enumerate(self._curl_entries):
            if curl_entry == "-H":
                # header field value is in the next entry
                header_field = self._curl_entries[index + 1]
                if header_field[0] == "$":
                    header_field = decode_str(header_field[1:])
                key, value = self.key_value_from_header_field(header_field)
                header.update({key: value})

        return header

    @staticmethod
    def key_value_from_header_field(header_field: str) -> tuple[str, str]:
        if header_field[0] == "$":
            header_field = decode_str(header_field[1:])

        key = header_field.split(":")[0].replace("'", "")
        value = header_field
        value = value.replace(key + ":", "")
        value = value.replace("'", "").strip()

        return (key, value.strip())

    @staticmethod
    def _check_if_str_is_url(url_str) -> ParseResult | None:
        try:
            possible_url_str = url_str.replace("'", "")

            if possible_url_str[0] == "$":
                possible_url_str = decode_str(possible_url_str[1:])

            result = urlparse(possible_url_str)
            if all([result.scheme, result.netloc]):
                return urlparse(possible_url_str)
        except ValueError:
            pass

        return None
