import requests

_HOST_ = "https://api.frankfurter.app"
_CURRENCIES_ = "/currencies"
_LATEST_ = "/latest"

def call_api(url: str) -> requests.models.Response:
    """
    Function that will call the specified API endpoint and return the response

    Parameters
    ----------
    url : str
    URL of the API endpoint to be called

    Pseudo-code
    ----------
    get request to url as resp
    if resp status code is equal to 200
    return resquests.models.Response
    else
    return message "There is an error with API call"

    Returns
    -------
    requests.models.Response
    Response from API request
    """
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp
    else:
        return "There is an error with API call"

def format_currencies_url() -> str:
    """
    Function that will format the URL to the currency endpoint

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    assign host API url with currency endpoint to url 
    return url

    Returns
    -------
    str
    Formatted URL to the currency endpoint
    """
    url = _HOST_ + _CURRENCIES_
    return url

def get_currencies():
    """
    Function that will extract the currency codes available from the Frankfurter app as a list

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    call API formatted to currencies endpoint as currency_response
    extract currency_response as a json, assigned to currency_list
    return currency_list as a list

    Returns
    -------
    list
    Currency codes available from the Frankfurter app
    """
    currency_response = call_api(format_currencies_url())
    currency_list = currency_response.json()
    return list(currency_list)

def format_latest_url(from_currency: str, to_currency: str) -> str:
    """
    Function that will format the URL to the latest endpoint

    Parameters
    ----------
    from_currency : str
    Currency code to be converted from
    to_currency : str
    Currency code to be converted to

    Pseudo-code
    ----------
    format API url to latest endpoint with the first and second input argument
    return the formatted url

    Returns
    -------
    str
    Formatted URL to the latest endpoint
    """
    url = _HOST_ + _LATEST_ + "?from=" + from_currency + "&to=" + to_currency
    return url