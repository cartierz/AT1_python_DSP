import unittest
from api import call_api, format_currencies_url, get_currencies, format_latest_url, _HOST_, _LATEST_, _CURRENCIES_


class TestFormatUrl(unittest.TestCase):
    def setup(self):
        self.format_currencies_url = "https://api.frankfurter.app/currencies"
        self.format_latest_url = "https://api.frankfurter.app/latest?to=GBP,AUD"
    
    def test_function_currencies(self):
        currency_url = _HOST_ + _CURRENCIES_
        self.assertEqual(currency_url, self.format_currencies_url)

    def test_function_latest(self):
        latest_url = _HOST_ + _LATEST_ + "?to=" + "GBP" + "," + "AUD"
        self.assertEqual(latest_url, self.format_latest_url)
    
    def test_function_currencies_str(self):
        currency_url = "test"
        self.assertEqual(currency_url, None)

    def test_function_latest_str(self):
        latest_url = "test"
        self.assertEqual(latest_url, None)

    def test_function_currencies_empty(self):
        currency_url = " "
        self.assertEqual(currency_url, None)

    def test_function_latest_empty(self):
        latest_url = " "
        self.assertEqual(latest_url, None)

    def test_function_currencies_none(self):
        currency_url = None
        self.assertEqual(currency_url, None)

    def test_function_latest_none(self):
        latest_url = None
        self.assertEqual(latest_url, None)

class TestAPI(unittest.TestCase):
    def setup(self):
        self.statuscode = 200
    def test_function_str(self):
        resp = call_api("test")
        self.assertEqual(resp, None)
    
    def test_function_latest(self):
        resp = call_api(_HOST_ + _LATEST_ + "?to=" + "GBP" + "," + "AUD")
        latest_status = resp.status_code
        self.assertEqual(latest_status, self.statuscode)
    
    def test_function_currencies(self):
        resp = call_api(_HOST_ + _CURRENCIES_)
        currencies_status= resp.status_code
        self.assertEqual(currencies_status, self.statuscode)
    
    def test_function_empty(self):
        resp = call_api(" ")
        empty_status= resp.status_code
        self.assertEqual(empty_status, None)

    def test_function_none(self):
        resp = call_api(None)
        empty_status= resp.status_code
        self.assertEqual(empty_status, None)
