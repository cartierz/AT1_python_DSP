
import sys
from_currency = sys.argv[1]
to_currency = sys.argv[2]
import requests

_HOST_ = "https://api.frankfurter.app"
_CURRENCIES_ = "/currencies"
_LATEST_ = "/latest"

url= _HOST_ + _CURRENCIES_
resp = requests.get(url)
if resp.status_code == 200:
    print(resp)
else:
    print("There is an error with API call")

# if check_valid_currency(from_currency) and check_valid_currency(to_currency):
#     url = format_latest_url(from_currency, to_currency)
#     result = call_api(url)
#     formatted_result = extract_api_result(result)
#     print(formatted_result)
# #else: 
#     #print(f"{sys.argv} is not a valid option")
#     #return (f"{sys.argv} is not a valid option")