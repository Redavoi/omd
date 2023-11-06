import unittest
import json
from unittest.mock import patch
from what_is_year_now import what_is_year_now


class TestWhatIsYearNow(unittest.TestCase):
    def test_dot_format(self):
        with patch('urllib.request.urlopen') as mock_what_is_year_now:
            mock_what_is_year_now.return_value.__enter__.return_value.read.return_value = json.dumps({'currentDateTime': '01.03.2019'}).encode('utf-8')
            assert what_is_year_now() == 2019
            mock_what_is_year_now.assert_called_once()

    def test_dash_format(self):
        with patch('urllib.request.urlopen') as mock_what_is_year_now:
            mock_what_is_year_now.return_value.__enter__.return_value.read.return_value = json.dumps({'currentDateTime': '2019-03-01'}).encode('utf-8')
            assert what_is_year_now() == 2019
            mock_what_is_year_now.assert_called_once()

    def test_invalid_format(self):
        with patch('urllib.request.urlopen') as mock_what_is_year_now:
            mock_what_is_year_now.return_value.__enter__.return_value.read.return_value = json.dumps({'currentDateTime': '2019.03.01'}).encode('utf-8')
            with self.assertRaises(ValueError):
                what_is_year_now()
            mock_what_is_year_now.assert_called_once()
