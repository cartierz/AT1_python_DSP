import unittest
from currency import check_valid_currency, extract_api_result, Currency
from datetime import datetime

class TestValidCurrency(unittest.TestCase):
    def test_function_false(self):
        from_currency = "AAA"
        to_currency = "BBB"
        from_result = check_valid_currency(from_currency)
        to_result = check_valid_currency(to_currency)
        self.assertEqual(from_result, False)
        self.assertEqual(to_result, False)

    def setup(self):
        self.from_currency = "GBP"
        self.to_currency = "AUD"
        self.amount = 1
        self.rate = 1.87
        self.inverse_rate = 1/1.87
        self.date = datetime.today().strftime("%Y-%m-%d")
    
    def test_function_true(self):
        from_currency = self.from_currency
        to_currency = self.to_currency
        from_result = check_valid_currency(from_currency)
        to_result = check_valid_currency(to_currency)
        self.assertEqual(from_result, True)
        self.assertEqual(to_result, True)

    def test_function_empty(self):
        from_currency = " "
        to_currency = " "
        from_result = check_valid_currency(from_currency)
        to_result = check_valid_currency(to_currency)
        self.assertEqual(from_result, "unknown")
        self.assertEqual(to_result, "unknown")

    def test_function_none(self):
        from_currency = None
        to_currency = None
        from_result = check_valid_currency(from_currency)
        to_result = check_valid_currency(to_currency)
        self.assertEqual(from_result, "unknown")
        self.assertEqual(to_result, "unknown")


class TestExtractApi(unittest.TestCase):
    def test_function_str(self):
        data = "test"
        currency_object = Currency()
        currency_object.from_json(data)
    
        self.assertEqual(currency_object.from_currency, None)
        self.assertEqual(currency_object.to_currency, None)
        self.assertEqual(currency_object.amount, None)
        self.assertEqual(currency_object.rate, None)
        self.assertEqual(currency_object.inverse_rate, None)
        self.assertEqual(currency_object.date, None)
    
    def setup(self):
        self.from_currency = "GBP"
        self.to_currency = "AUD"
        self.amount = 1
        self.rate = 1.87
        self.inverse_rate = 1/1.87
        self.date = datetime.today().strftime("%Y-%m-%d")

    def test_function_setup(self):
        data = {
            "from_currency": self.from_currency,
            "to_currency": self.to_currency,
            "amount": self.amount,
            "rate": self.rate,
            "inverse_rate": self.inverse_rate,
            "date": self.date,
        }
        currency_object = Currency()
        currency_object.from_json(data)
    
        self.assertEqual(currency_object.from_currency, self.from_currency)
        self.assertEqual(currency_object.to_currency, self.to_currency)
        self.assertEqual(currency_object.amount, self.amount)
        self.assertEqual(currency_object.rate, self.rate)
        self.assertEqual(currency_object.inverse_rate, self.inverse_rate)
        self.assertEqual(currency_object.date, self.date)

    def test_function_empty(self):
        data = {
        }   
        currency_object = Currency()
        currency_object.from_json(data)

        self.assertEqual(currency_object.from_currency, None)
        self.assertEqual(currency_object.to_currency, None)
        self.assertEqual(currency_object.amount, None)
        self.assertEqual(currency_object.rate, None)
        self.assertEqual(currency_object.inverse_rate, None)
        self.assertEqual(currency_object.date, None)

    def test_function_none(self):
        data = None
        currency_object = Currency()
        currency_object.from_json(data)

        self.assertEqual(currency_object.from_currency, None)
        self.assertEqual(currency_object.to_currency, None)
        self.assertEqual(currency_object.amount, None)
        self.assertEqual(currency_object.rate, None)
        self.assertEqual(currency_object.inverse_rate, None)
        self.assertEqual(currency_object.date, None)

