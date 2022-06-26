"""
Module to define constants for the get_data module
"""

# default headed will be used when no header os provided in the request_params
# for the GetData.result method
DEFAULT_HEADER = {
    'User-Agent': (
        "Mozilla/5.0 (Windows NT 6.1; WOW64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/56.0.2924.76 Safari/537.36"),
    'accept': 'json/application'
    }

SCRAPER_API_NAME = 'SCRAPERAPI'
SCRAPER_API_URL = 'https://api.scraperapi.com'

# these are the status codes that are allowed to be passed in as
# expected_status_codes to the LogicalAPI class. This class will
# check the actual returned status code versus the expected status_code
ALLOWED_EXPECTED_STATUS_CODES = [200, 201]


CONVERTOR_PARAMS_JSON_FROM_HTTP = [
    'json_begin', 'json_end', 'json_within_quotes', 'replace',
    'escaped_quotes']
