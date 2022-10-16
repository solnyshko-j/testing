import urllib.request
import json
import io
from unittest.mock import patch
import unittest

API_URL = "http://worldclockapi.com/api/json/utc/now"

YMD_SEP = "-"
YMD_SEP_INDEX = 4
YMD_YEAR_SLICE = slice(None, YMD_SEP_INDEX)

DMY_SEP = "."
DMY_SEP_INDEX = 5
DMY_YEAR_SLICE = slice(DMY_SEP_INDEX + 1, DMY_SEP_INDEX + 5)


def what_is_year_now() -> int:
    """
    Получает текущее время из API-worldclock и извлекает из поля
            'currentDateTime' год

    Предположим, что currentDateTime может быть в двух форматах:
      * YYYY-MM-DD - 2019-03-01
      * DD.MM.YYYY - 01.03.2019
    """
    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)

    datetime_str = resp_json["currentDateTime"]
    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError("Invalid format")

    return int(year_str)


#
# def test_year_first():
#     with patch("requests.get") as mock_value:
#         mock_value.return_value.json = "2019-03-01"
#         assert what_is_year_now() == 2019


class Test_what_is_year_now(unittest.TestCase):
    def test_year_first(self):
        with patch.object(
            urllib.request,
            "urlopen",
            return_value=io.StringIO('{"currentDateTime": "2019-03-01"}'),
        ):
            assert what_is_year_now() == 2019

    def test_year_last(self):
        with patch.object(
            urllib.request,
            "urlopen",
            return_value=io.StringIO('{"currentDateTime": "01.03.2019"}'),
        ):
            assert what_is_year_now() == 2019

    def test_year_error(self):
        with patch.object(
            urllib.request,
            "urlopen",
            return_value=io.StringIO('{"currentDateTime": "2019:03:01"}'),
        ):
            with self.assertRaises(ValueError):
                assert what_is_year_now()


if __name__ == "__main__":
    pass
