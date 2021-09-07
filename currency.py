from dataclasses import dataclass
from api import get_currencies
import sys

CURRENCIES = get_currencies()

def check_valid_currency(currency: str) -> bool:
    """
    Function that will check currency code is amongst the list of available currencies

    Parameters
    ----------
    currency : str
    Currency code to be checked

    Pseudo-code
    ----------
    if the currency parameter as upper case is in CURRENCIES list
    return bool True
    else 
    return bool False

    Returns
    -------
    bool
    True if the currency code is valid otherwise False
    """
    if currency.upper() in CURRENCIES:
        return True
    else:
        return False

@dataclass
class Currency:
    """
    Class that represents a Currency conversion object. 

    Attributes
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    rate : float
        The conversion rate to be applied on the origin amount (origin -> destination)
    inverse_rate : float
        The inverse of the previous rate  (destination -> origin)
    date : str
        Date when the conversion rate was recorded
    """
    from_currency: str = None
    to_currency: str = None
    amount: float = 0
    rate: float = 0
    inverse_rate: float = 0
    date: str = None
    def reverse_rate(self):
        """
        Method that will calculate the inverse rate, round it to 5 decimal places and save it in the attribute inverse_rate

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.inverse_rate = round(1/self.rate, 5)
        return None
    def format_result(self):
        """
        Methods returning the formatted successful message

        Parameters
        ----------
        None

        Returns
        -------
        str
            Formatted successful message
        """
    
        return f"Today's {self.date} conversion rate from GBP to AUD is {self.amount*self.rate}. The inverse rate is {self.amount*self.inverse_rate}"

def extract_api_result(result: dict) -> Currency:
    """
    Function that will extract the relevant fields from API result, instantiate a Currency class accordingly and
    calculate the inverse rate

    Parameters
    ----------
    result : dict
        Results of the API converted as dictionary

    Pseudo-code
    ----------
    instantiate currency class as currency_object
    extract the values from rates key in result dictionary as rates
    extract value from base key of result as from_currency of currency_object class
    extract rates key from rates as to_currency of currency_object class
    extract value from amount key of result as amount of currency_object class
    extract value from rates as amount of currency_object class
    assign reverse_rate of Currency to inverse_rate of currency_object class
    extract date value from results as date of currency_object class
    return currency_object
    
    Returns
    -------
    Currency
        Instantiated Currency
    """
    currency_object = Currency()
    rates = result.get("rates")
    currency_object.from_currency = result.get("base")
    currency_object.to_currency = rates.keys()
    currency_object.amount = result.get("amount")
    currency_object.rate = rates.values()
    currency_object.inverse_rate = Currency.reverse_rate
    currency_object.date = result.get("date")
    return currency_object