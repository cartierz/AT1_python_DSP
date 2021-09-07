import sys
from api import call_api, format_latest_url
from currency import CURRENCIES, check_valid_currency, extract_api_result


def main():
    """
    Function that will check if there are enough input arguments provided.
    If so it will return the formatted result from the Frankfurter app.
    If not it will return an error message

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    if the length of input arguments is not 2
    display [ERROR] You haven't provided 2 currency codes.
    return [ERROR] You haven't provided 2 currency codes.
    else 
    if from currency and to currency is in CURRENCIES list
    assign first input as from_currency
    assign second input as to_currency
    return formatted result

    Returns
    -------
    str
    Formatted API result or error message
    """
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print ("[ERROR] You haven't provided 2 currency codes.")
        return "[ERROR] You haven't provided 2 currency codes."
    else:
        if sys.argv[1] and sys.argv[2] in CURRENCIES:
            from_currency = sys.argv[1]
            to_currency = sys.argv[2]
            return get_rate(from_currency, to_currency)

def get_rate(from_currency: str, to_currency: str):
    """
    Function that will check if provided currency codes are valid otherwise it will return error message.
    If both are valid, it will format the API url, make a request to it and format the result

    Parameters
    ----------
    from_currency : str
    Currency code to be converted from
    to_currency : str
    Currency code to be converted to

    Pseudo-code
    ----------
    if from_currency and to_currency are in CURRENCIES list
    format the URL to the latest endpoint using from_currency and to_currency
    use formatted URl to call the specified API endpoint and return the response
    retrieve API result as dictionary
    formatted dictionary result
    else 
    display system argument is not a valid option
    return system argument is not a valid option

    Returns
    -------
    str
    Formatted API result or error message
    """
    if check_valid_currency(from_currency) and check_valid_currency(to_currency):
        url = format_latest_url(from_currency, to_currency)
        result = call_api(url)
        dict_result = result.text
        formatted_result = extract_api_result(dict_result)
        return formatted_result
    else:
        print(f"{sys.argv} is not a valid option")
        return f"{sys.argv} is not a valid option"

if __name__ == "__main__":
    main()