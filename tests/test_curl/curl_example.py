DECODE_TEST_CASES = [
    (r"\u0048\u0065\u006C\u006C\u006F", "Hello"),  # Decoding "Hello"
    (r"\u0057\u006F\u0072\u006C\u0064", "World"),  # Decoding "World"
    (r"\u0031\u0032\u0033\u0034\u0035", "12345"),  # Decoding "12345"
    (r"\u263A", "☺"),  # Decoding a smiley face
    (r"plain_text", "plain_text"),  # No decoding needed
]

HEADER_STR_EX1 = "$'cookie: SSLB=1; rnumber=2985268576; cookie-consent={%22date%22:%2220240521%22%2C%22version%22:%223.4%22%2C%22gtmContainerVersion%22:%221193%22%2C%22consent%22:%22no%22%2C%22social%22:null%2C%22ad%22:null%2C%22host%22:%22www.ah.nl%22}; RCC=P1-8814fecb-7ce5-4043-a6b6-940aa0203501; SSOC=741697040d64c492cd9a95480aee9c4e1081fcebbca5f1a13483aa432460ea23; _csrf=v-ArE_JoVYysXzyb6nI5gm4H; Ahonlnl-Prd-01-DigitalDev-F1=\u0021rET7bvy1hmhR+TgJVEE3/lwfQrEqwUm4KpZ/paQmhriBuO6N+bJ96xtnvdEiMBIoQr1I1bxpRUo9INM=; jsessionid_myah=P1-8814fecb-7ce5-4043-a6b6-T; i18next=nl-nl; _ga=GA1.2.424226990.1718342701; _gid=GA1.2.287080927.1718618521; ASC=P1-4d43e665-3c2a-495b-bd6e-7688b578bfb6; bm_sz=441CA1438A90A1B6564870D6C6702D14~YAAQPhjdWAJHYgWQAQAA/pRTKhiyVK3Nz9mApfAtT4ZTEEFPfkvoFikVPj4y4ET92xWVgfwbBPDn3HUnYtBJ9hm2X07E4ZevQWnx2ZzgsiozBw4a4vofwcS168ws2WfJevHCRB0yPReJHObdVPkv6JU0hQI/zhW/U+JJdXg5RwlK+1e8hxEyqgiPFmcm3HZmHQE2z4yAov5wH88Zaey67/yAZtk6YO4GZKnv2jnARKmyFOUcmB6tSmBW3e1POpvFLs+jdu9mOSkyorWQf0HBszpln8VeH8xxvylQttXnqBrSHaET4ZkTe3ySRigBKCDQ/j2CEeTn+u6Mtea6hNCDrd7qbKRyz9b86csZjH/UyKVpyqFPGA==~4340025~3294278; _abck=07C6979AEEFDB4D291A6B314664EBE1E~-1~YAAQPhjdWN2oYgWQAQAAR89aKgzlwEyVxOpNzuyLRYIpICK+ne6bAq8jFIyy/+dqS73+VZFbN2nbIdWFwhMgv8yKF20Y9sTc3tul+/QYasgZnvKDgROMEg8mC/SPrBCpPHXAszvN1Pj/jX79IjP9E1hQ+QUE8wsTPab0OGgEW5PoQbsnYLCnEx1zvrBEnVZyGzIkiv0bmrOjmGTg1RUxeGI8O2jn9+risV039HRmdZtM59AZbVl16wSJQSX8PKOwe/PX3Hb+bhzv2pMfzzHASW1yMBRhjVX4gAjnaNavvjDzX4veFgdYoZ8VwlQIrdiczqwUTHReWh0XSgkdtg4UxHAH/5QkSKZllJnGyj5FYxWlHcF1cpkxlM9EwtydxNgspdB0Vr431pHY~-1~-1~-1; SSSC=4.G7371390380887019228.14|2786.53881:2859.54348:2971.55902:2982.56035:2983.56041:2992.56070:2997.56098:3005.56159:3009.56178; SSOD=ADXAAAAAWgCxwQAAAQAAABfpZ2YX6WdmAABQpAAABQAAABrpZ2ZMhGxmAAC_egAABgAAAHLpZ2ZjPXFmAADqkwAAAQAAAIE8cWaBPHFmAADRgwAAAQAAAMw9cWbMPXFmAAAAAA; bm_mi=E91AFE0604D3281AA4E249C6B7854651~YAAQFDdlXxocYSWQAQAAg2bUKhi2o305xORCSOxSW/AKFNiZo7CtN0bNQ3EPwqbzDvLV4c4EDbqUzW0t3/OTc1otWsgrag3G5ws7wNLgZrVhksNkNh/U0T7DLkoGoqkKYAFgKNGTz3B2wiPG0T0QqTbjzVIzKFodB9XtPp+PgSjdp4gCVbLeo8qhaYDHr9qdRD4NjyaVpTNKq85HbM4N1S5Z56wXybgc3zw2e/qyUxJrHc7uXXGvzV5KS1JbyapbvxRH+bEQJkOJz9uEzs42UV3KiaZKUSPaZ4DEqsVEzQfDyRv1ugy1mSkhna4C03AyiyI7s0WD0UrqKGSdHi9+FjCwahQ8ZWI=~1; Ahonlnl-Prd-01-DigitalDev-B2=\u0021duCKjzHNlqhEbsBR9ETymWDU0ydZsTTbc9i7Pun3AwWUXoTxkrASx3ixoAVd8udS1wkIXr9Uws3KWQ==; _gat_UA-89331604-2=1; SSID=CQBifB1-ABgAAAB_cExm3I6AAX9wTGYOAAAAAAAlUSpqR11xZgBUmr0LAANf2wAA-ehnZgsAtQsAAyLbAAD56GdmCwCmCwAB49oAAEddcWYBALALAAEG2wAAR11xZgEA4goAAXnSAABHXXFmAQCbCwADXtoAALM4ZGYMAMELAAFy2wAAR11xZgEAKwsAAUzUAABHXXFmAQCnCwAB6doAAEddcWYBAJALAABzCwAAmgsAAIkLAAB0CwAAngsAAA; ak_bmsc=2FDD7C5165058C07E33BA7C0BF4266E7~000000000000000000000000000000~YAAQFDdlXzgcYSWQAQAAh2nUKhjNU7fuTFUfMopHJRzPW2OTPV26JXeQ24d017kU/qRXYtQhk2UZ8z/K0xh5ALgtsMlNLuxMmU/x0pW/Mn9cCgf0wMLVAQ+SZwgDxE1Lq9pQGICxM5wVjqKzi6hL2ptpznUTzCdJeA2wLeRETdT0iKQuxUHsJS8lXNtlNn7pr7LtVm3pBht0rFoI2DjjNXcvbo7hED9rptC90aWwNJ04KsCYtbxMvW4Va5TMPRPBC54O6I7noaBC+cO3jGXRoR6oessAbMPteceOSxJvh6zL0TXBeFcbsKyItIBWVZNf3UGjblWnYB6SR9uq/XWboXqX7fhfip48ynJAa62RX3TCPXRdSRL+Jyy5twxBxlkEAfIzpANeAgUKyCNPG77/SxEWMePFlCI4h9Xd7Ak5H830/+szbgAqZHIaiqMk6ye1LB51ahI/eUN7teZc2sFKmCgC8OU9HMIajdUFv8CCd85T15/94kxGfx6CuWjb58xPA5T5fi7mGg==; ah_cid_cs=%7B%22sct%22%3A10%2C%22cid%22%3A%22ah.1.1716285569156.2772571753%22%2C%22cid_t%22%3A1716285569156%2C%22sid%22%3A1718697039183%2C%22sid_t%22%3A1718705485829%2C%22pct%22%3A24%2C%22seg%22%3A1%7D; SSRT=YV1xZgIDAA; SSPV=P9IAAAAAAAAAVwAAAAAAAAAAAAQAAAAAAAAAAAAA; bm_sv=CF634E1C5CE838D58329ADDBA217025F~YAAQFDdlXwYhYSWQAQAAZMjUKhiBZ4iMiOC2Q4++N6UQ2hZIID3p6LTYPtWC8Ka90sy22Z+bh39GA0vya5+TC6Ba7XZey0smEUy+c3V826R3QJKPS8A6H6a2cfm8LriOONUmUyvh2Ths6/MlYW8fl3HT0rTYwfBg92xuPyG3pme/Q3tVVPY+UlD1djuLMUT9UAHB5fIZtE7JF0xvr4fh/DCFlPeCDH3ZHYPMNJl12nvrZXYMdyqJUS9D1HCEl+6X~1'"
HEADER_STR_EX2 = "'priority: u=1, i'"

ENCODED_URL = "$'https://maps.googleapis.com/maps/vt?pb=\u00211m5\u00211m4\u00211i12\u00212i2099\u00213i1347\u00214i256\u00212m3\u00211e0\u00212sm\u00213i696443073\u00213m17\u00212snl-NL\u00213sUS\u00215e18\u002112m4\u00211e68\u00212m2\u00211sset\u00212sRoadmap\u002112m3\u00211e37\u00212m1\u00211ssmartmaps\u002112m4\u00211e26\u00212m2\u00211sstyles\u00212zcy5lOmwudC5mfHAuYzojNTY0MzM3LHMudDoxN3xzLmU6Zy5zfHAuYzojOWE4ZTg3LHMudDoxOXxzLmU6bC50LmZ8cC5jOiM3ZjgwODB8cC52Om9uLHMudDoyMHxzLmU6bC50LmZ8cC5jOiM5YThlODd8cC52Om9uLHMudDo1fHMuZTpnfHAuYzojZjBlY2U2LHMudDoyfHAudjpvZmYscy50OjM3fHAudjpzaW1wbGlmaWVkLHMudDozN3xzLmU6Zy5mfHAuYzojZDhkNWQwLHMudDozN3xzLmU6bHxwLnY6b2ZmLHMudDo0MHxwLmM6I2E1ZDdiNnxwLnY6b24scy50OjQwfHMuZTpnfHAuYzojODdjYTllLHMudDo0MHxzLmU6bC50LmZ8cC5jOiM5YThlODd8cC52OnNpbXBsaWZpZWQscy50OjQwfHMuZTpsLnQuc3xwLnY6b2ZmLHMudDo0OXxzLmU6Z3xwLmM6I2ZhYzc1YXxwLnY6c2ltcGxpZmllZCxzLnQ6NjV8cC5jOiNkNGM4Yjl8cC52OnNpbXBsaWZpZWQscy50OjZ8cy5lOmd8cC5jOiNiMWQ5ZjM\u00214e0\u00215m1\u00211e3\u002123i1376099\u002123i1379903\u002123i56565656\u002123i97569357&key=AIzaSyCK0hegoFuRoTg0Hx2MiSJfRaVZuAcje70&token=77256'"

SIMPLE_GET_CURL_SINGLE_URL_QUERY_PARAM = """
curl 'https://test.nl?test=1' \
  -H 'accept: */* ' \
"""

SIMPLE_GET_CURL = """
curl 'https://test.nl?test=1&other=test' \
  -H 'accept: */* ' \
"""


AH = """
curl 'https://www.ah.nl/gql' \
  -H 'accept: */*' \
  -H 'accept-language: nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'batch: true' \
  -H 'content-type: application/json' \
  -H 'cookie': 'Ahonlnl-Prd-01-DigitalDev-B2=!5INtuf5sdGu6AFRR9ETymWDU0ydZsc/8S1i7OxX8BTAd7JqoLEWNxmYOZ5Svw1OXAPLX5LUszwQDug==; Ahonlnl-Prd-01-DigitalDev-F1=!ZiSmrQkl2B0yFTyC4EE6mVR2Y8swkr5VXNdn64u/GHI1pGVGlDHwvu4HzFfWyM6r4y5ynxWN9+uxliY=; SSID=CQDFOx2MABgAAAB_cExm3I6AAX9wTGYQAAAAAAAlUSpqy55xZgBUmrALAAEF2wAAy55xZgEAwQsAAXPbAADLnnFmAQC9CwADX9sAAPnoZ2YNAHULAAH31wAAy55xZgEApwsAAeraAADLnnFmAQC1CwADItsAAPnoZ2YNAJsLAANe2gAAszhkZg4A4goAAXnSAADLnnFmAQArCwABTNQAAMuecWYBAKYLAAHj2gAAy55xZgEAkAsAAHMLAACaCwAAiQsAAHQLAACeCwAA; SSLB=1; SSOD=ADXAAAAAWgCxwQAAAQAAABfpZ2YX6WdmAABQpAAABQAAABrpZ2ZMhGxmAAC_egAABgAAAHLpZ2ZjPXFmAADqkwAAAQAAAIE8cWaBPHFmAADRgwAAAQAAAMw9cWbMPXFmAAAAAA; SSPV=U-kAAAAAAAAAFAAAAAAAAAAAAAEAAAAAAAAAAAAA; SSRT=HqJxZgADAA; SSSC=4.G7371390380887019228.16|2786.53881:2859.54348:2933.55287:2971.55902:2982.56035:2983.56042:2992.56069:2997.56098:3005.56159:3009.56179; _abck=C6BD9FEFF8CA077A081B0CA73B501558~-1~YAAQDRjdWAVG1yGQAQAAjkjhKwxHBwtl1FN+BcJBADTrX6H80mrpIHP0GTo2XsVBOzL0fb1F2HefmfWkxVmHkQS75G7xLU67cJqpTO4NCrBxALBnNSjcGEdndcOxl4sI9eI2l210Gcf+xAaErGSG9UQL59YyXpLPUDfOU6CKP6Kzy47Geb5gKyQywmko3YFvl8ZGzY72azwjHDrunitfZB+iUHBly3IR0AxuEx8ihw+DbdLDzd3iKUDQL4+/7r5lNo9i3M8UMm/iiJDK53O7Dq3rl873J2DdsF1NyDj5gMBP3heVhCmWy0lnDoHyWebrOBC87AuiEE4/wER3TpHBHgLpK4HZvYIYXvMDTOuwPw==~-1~-1~-1; ak_bmsc=829532B63901E35A1DA1FD51C3131BD3~000000000000000000000000000000~YAAQDRjdWAZG1yGQAQAAjkjhKxhoks+NFEe2ZVmUy9NVbDmXJ1vdgjgXhrvhWpPUBsdkZDzZnHR/4gbFE2WxZ57vZMmbssAmUy3AV1NRJN3uCD7kYmiWzS3+svHM/3qn/NRy8FZF8je+kBbD61r5kADwoYm3MNSbaF0ueWK4jShogBki8X8WD9p/P446WnXBXNG2ma3IhwyGGFyEADH0jN4wQWLsSrWoflW29rMpNVj38a0T7CrLf/0pCJtg+palMYyOV+I4EQFSrdF6+iWU/zjmE5vikacLx8vYLyvDrJ7kodACgz3IC7augyv15CKE36QfJsXWpPmzL0SgM0TpXxjzhTE+tEe4b9TwgiRvnGkEJVJxFTpFzAbW; bm_sz=C6756065F5262123957F4FEBE464C110~YAAQtxjdWJ6TbCmQAQAA4WIjKxjBIl/kbmr1RRm9v015j2Cko5TAi0EzfjiSQKA3MLkQRJQqohDhxl+oSKYR7gEbt7blegnXXc3Ri/kiNUtxBddntPWIpmeiPXw1VFOHtYhDdxa9k53Hi9b2sm1gMb6TVlGABDkWJVuAbH1kSjY/alxKxAjdxXXFv4TmGFfhdVjMbl4FdPfNJQIu6v6GAg5W5KgwiV4Rg25CHuq8VtMnVpIR1xe9EmuT8Ym0R6e9XsPeI+0+j+j8p23IJAGWKcdj+a3vvFYhMqpDbHNjRUo1YSNF1EVzWwEMRxcT2pNmNnMVHdJoJoDHouHwE5I3kDhrp4qwXZ5KCGJJE+eoOvQL2cljrDf0q2rriq2YiQ0XZZLFs9ZO9bHSSfWLlw==~3359024~3749427' \
  -H 'origin: https://www.ah.nl' \
  -H 'priority: u=1, i' \
  -H 'referer: https://www.ah.nl/winkels' \
  -H 'sec-ch-ua: "Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36' \
  -H 'x-client-name: ah-store' \
  -H 'x-client-version: 0.31.3' \
  --data-raw '[{"operationName":"storesListResults","variables":{"limit":10,"filter":{"cityStartsWith":null,"location":{"latitude":51.3578078,"longitude":5.3159125},"openingHours":null,"postalCode":null,"services":null,"storeType":null},"start":0},"query":"query storesListResults($filter: StoresFilterInput, $limit: Int, $start: Int) {\n  storesSearch(filter: $filter, limit: $limit, start: $start) {\n    result {\n      ...storesListResults\n      __typename\n    }\n    pageInfo {\n      hasNextPage\n      total\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment storesListResults on Stores {\n  id\n  storeType\n  address {\n    ...address\n    __typename\n  }\n  openingDays {\n    ...storesOpeningDay\n    __typename\n  }\n  distance\n  __typename\n}\n\nfragment address on StoresAddress {\n  city\n  countryCode\n  houseNumber\n  houseNumberExtra\n  postalCode\n  street\n  __typename\n}\n\nfragment storesOpeningDay on StoresOpeningDay {\n  date\n  dayName\n  openingHour {\n    ...storesOpeningHour\n    __typename\n  }\n  type\n  __typename\n}\n\nfragment storesOpeningHour on StoresOpeningHour {\n  openFrom\n  openUntil\n  __typename\n}"},{"operationName":"storesMapResults","variables":{"filter":{"cityStartsWith":null,"location":{"latitude":51.3578078,"longitude":5.3159125},"openingHours":null,"postalCode":null,"services":null,"storeType":null}},"query":"query storesMapResults($filter: StoresFilterInput) {\n  storesSearch(filter: $filter, start: 0, limit: 5000) {\n    result {\n      ...storesMapResults\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment storesMapResults on Stores {\n  id\n  geoLocation {\n    latitude\n    longitude\n    __typename\n  }\n  storeType\n  __typename\n}"}]'
"""



AUDI = """
curl 'https://dealer-graphql.apps.emea.vwapps.io/' \
  -H 'accept: */*' \
  -H 'accept-language: nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'alwaysreturnpartner: true' \
  -H 'clientid: d7sfqwrxzu' \
  -H 'content-type: application/json' \
  -H 'origin: https://www.audi.nl' \
  -H 'priority: u=1, i' \
  -H 'referer: https://www.audi.nl/' \
  -H 'sec-ch-ua: "Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: cross-site' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36' \
  --data-raw $'{"operationName":"Dealer","variables":{"lat":52.3873878,"lng":4.6462194,"radius":10,"country":"NLD"},"query":"query Dealer($lat: Float\u0021, $lng: Float\u0021, $userLat: Float, $userLng: Float, $radius: Int, $country: String, $services: String) {\\n  dealersByGeoLocation(\\n    lat: $lat\\n    lng: $lng\\n    userLat: $userLat\\n    userLng: $userLng\\n    radius: $radius\\n    limit: 20\\n    country: $country\\n    serviceFilter: $services\\n  ) {\\n    dealers {\\n      ...FragmentDealerFields\\n      __typename\\n    }\\n    meta {\\n      resultCount\\n      searchRadius\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\\nfragment FragmentDealerFields on Dealer {\\n  dealerId\\n  matPrimaryCode\\n  kvpsPartnerKey\\n  name\\n  address\\n  latitude\\n  longitude\\n  services\\n  distance\\n  phone\\n  additionalData {\\n    displayName\\n    locationName\\n    __typename\\n  }\\n  openingHours {\\n    departments {\\n      id\\n      departmentName\\n      openingHours {\\n        id\\n        open\\n        timeRanges {\\n          openTime\\n          closeTime\\n          __typename\\n        }\\n        __typename\\n      }\\n      __typename\\n    }\\n    __typename\\n  }\\n  __typename\\n}\\n"}'
  """

ADIDAS = """
curl 'https://www.adidas.nl/api/stores?latitude=52.3873878&longitude=4.6462194&type=4' \
  -H 'accept: */*' \
  -H 'accept-language: nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'content-type: application/json' \
  -H 'cookie: geo_ip=62.45.111.34; geo_country=NL; onesite_country=NL; geo_coordinates=lat=52.35, long=4.92; AKA_A2=A; sbsd_ss=ab8e18ef4e; akacd_generic_prod_grayling_adidas=3896158914~rv=39~id=344ffc9608a68145c17d94d71235ec32; akacd_plp_prod_adidas_grayling=3896158914~rv=16~id=fd36ea6d919d507b2e48300401d13826; x-original-host=adidas.co.uk; x-site-locale=en_GB; mt.v=2.801697556.1718706116795; mt.v=2.801697556.1718706116795; wishlist=%5B%5D; ab_qm=b; ak_bmsc=CC58A24C4A585DAFF2F900751806C205~000000000000000000000000000000~YAAQNTdlX/UtUvGPAQAAPBreKhjgQJDx1keflfn2mADZ6kbs2UBHsnLMPVCFtIrk6DlUKo5gpwn895rdIKcBP8lfXSMpWd1PStVec4oiFegkeCS6his+w5Rt98ccpfjAcr2IpcAFQ+j2+23Gf6vAyW6LBYHcjeODOEoKrKGRjYUB0cOQHtgJt5QGpJOl/WltsStPfsEzP0VdKJ/EDhupRNkVHBSftD337zl4gWClFG9W3UTsmFYWfp2NqcFJFCRPAo8+zSemDB4SuW4WayLjBpgJb/n0IVEUAksJuJyD0Al2Q+9kbLTjVdfuZqkcFRbkoGGv2pceqRmSYMrFKORQRjq1/Dv9KuAb4gPLNSAuNO4rTzN5DcOIU85iht4CehkoNfj/pBFX7dg=; AMCVS_7ADA401053CCF9130A490D4C%40AdobeOrg=1; mt.sc=%7B%22i%22%3A1718706117310%2C%22d%22%3A%5B%5D%7D; AMCV_7ADA401053CCF9130A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19893%7CMCMID%7C31588401634022121850357314672477940861%7CMCAAMLH-1719310917%7C6%7CMCAAMB-1719310917%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1718713317s%7CNONE%7CMCAID%7CNONE; s_cc=true; wishlist=%5B%5D; notice_preferences=%5B0%2C1%2C2%5D; paidMediaIntent=true; _gcl_au=1.1.521322231.1718706120; _gid=GA1.2.294042054.1718706120; _fbp=fb.1.1718706119985.762780214637320721; _pin_unauth=dWlkPU5EWTJOVFZoT0dJdFkyRXhNaTAwT1RsaExXRmxaRFl0WWpFMU5HVmtNR0V3Wm1OaQ; _gat_tealium_0=1; _scid=1f54461b-c325-4e94-921d-89e86b7e67a1; _scid_r=1f54461b-c325-4e94-921d-89e86b7e67a1; tfpsi=72ab1a3d-b96e-4bc5-a33a-192ea638c532; _uetsid=991eb9902d5c11ef919b63a2e4f0b8f0|zqw9dk|2|fmq|0|1630; _uetvid=991f51e02d5c11efa78e0f37bc6fe4af|49xjj1|1718706120637|1|1|bat.bing.com/p/insights/c/h; QSI_SI_0evq2NrkQkQaBb7_intercept=true; QuantumMetricSessionID=eee491f3efa1b1279b6ba0f253a43af1; QuantumMetricUserID=1b34285e2140871b4e383ea6a04dea8f; bm_sz=E7BB09FCEA1D2533E3235C429FBC096B~YAAQNTdlX2IvUvGPAQAAK1PeKhjP+4I/o7G1Xko1BVOCOjoF3KEzlmrajC5TKPlxQkWx4rQfTctgHpyo8MBImqeLS8KpL8qrTvkOikZ7ALvg1fPT+L7m2N3yDxZBexhrx9jCYlFZBJFJOHN2/fRnzY957QVv39bE4It9LfJhVh2kC6Kbs2MHWoqSwoVTuM4oup0NNeUWeorE4ZBXiSqLleAAeZvEAlhLrnu8PdEPHp1Xuko4Bd8GAbFXXLqf71A2RYTQZEFbmPZHoNmjBTseqz8yKa4tFsN77d6P0x+mFD4L13vGhnL0xucILJPxHi+wHMpk6vhXLNolwNw88BcwozKYCv3jw5wgBPcAx1Bgv0lXc9GGFeW/NrZNxVgC8eptFx4C6ehWoFNlgbHJx+qj0XWpg/kI+gkVmM5BecXq30xx4F4=~4535620~3682616; RT="z=1&dm=www.adidas.nl&si=ccfdc9e2-679c-4dd4-9153-c593cba4d213&ss=lxk98u9q&sl=1&tt=38f&bcn=%2F%2F684dd32e.akstat.io%2F&ld=39g&nu=4zbk6u3c&cl=c16&hd=cjl"; x-commerce-next-id=6fdf7aaf-355b-4fbb-9a85-d72e1916888d; sbsd=sCBO7dC+2npwclC49K0gHM7Ritubp11DLNpjip/v1lXD0s5CvneFKx0cOD/ZaMumT4HmutbTswCQlZj5qkNjqk8h+ntV/7MILE+taV/RKRcQoJi0kk12HuOi9m3I65elWeLsOvatqaF6Pa3sA8jqPu9pukn5g+NIy5kqXHt4OYhlEMVejltNcrlYex7lzWwal; UserSignUpAndSave=1; persistentBasketCount=0; userBasketCount=0; newsletterShownOnVisit=false; pagecontext_cookies=; pagecontext_secure_cookies=; s_sess=%5B%5BB%5D%5D; s_pers=%20s_vnum%3D1719784800145%2526vn%253D1%7C1719784800145%3B%20pn%3D1%7C1721298134041%3B%20s_invisit%3Dtrue%7C1718707934051%3B; utag_main=v_id:01902ade18f1001d0665f86561be05075001606d01c88$_sn:1$_se:10%3Bexp-session$_ss:0%3Bexp-session$_st:1718707934048%3Bexp-session$ses_id:1718706116849%3Bexp-session$_pn:2%3Bexp-session$_vpn:2%3Bexp-session$_prevpage:STOREFINDER%7CSTORE%20LISTING%3Bexp-1718709734035$ttdsyncran:1%3Bexp-session$dcsyncran:1%3Bexp-session$dc_visit:1$dc_event:2%3Bexp-session$ab_dc:CONTROL%3Bexp-1723890134010; _rdt_uuid=1718706120038.53eeb053-1a46-4d28-9c7c-5dc9e75e6d6a; _ga_4DGGV4HV95=GS1.1.1718706117.1.1.1718706134.45.0.0; _ga=GA1.1.2022014837.1718706117; _abck=0CB35479A5DE52F4CA21EB529A853155~-1~YAAQNTdlX+owUvGPAQAAQLneKgwKQOhhbTEhwhiZ5CLrTQw/lC4DlHU3jPyUXgQwTgHrUMGLb/I+OWekyA7Wax6VtMSDttJc2TDR1o6/AhnX/L9A6kHpTl12apGQm285+Pl+A01MSit1kbURqR0h474iTD8I6tTAYzHWVY2ZG/7zL5Pv3bQ5nWtIerm07+RIgePTivb6r3JjtZyg/OR8NIQqfJjImNH3LIFBOEBiHxqPBO+H8dMn5Bd/szvrM9e2lDWL8BfhkXR3UXXi0gjM3wLa+B/qD2OrRQpPjjcnn9rPWdqdmwb89D7yWVawb4WtXYO26CeUj27QB70YOleK44KrkjS5ca4+9HjH9UadpfyVAhUKC69eWLQD93U+3ZMMCEeOMzK5k0ne6tkcfDAmuX5S2xeuL83uJMQyuxIdcuouEp6k+TkQRDSxk+YBauNBLeZSuyfx2meXg0lta4nBM4Avst7wLeQKmUELyXGo6V/0NUeBnMWgIsYBifbR95LGB1ZT44pPGv4=~-1~-1~1718709717' \
  -H 'glassversion: empty' \
  -H 'priority: u=1, i' \
  -H 'referer: https://www.adidas.nl/stores' \
  -H 'sec-ch-ua: "Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36' \
  -H 'x-instana-l: 1,correlationType=web;correlationId=afe4fdf7ec32c0cf' \
  -H 'x-instana-s: afe4fdf7ec32c0cf' \
  -H 'x-instana-t: afe4fdf7ec32c0cf'
"""
