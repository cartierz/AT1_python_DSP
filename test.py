import sys
from currency import CURRENCIES

currency = "aud"
if currency.upper() in CURRENCIES:
    print(True)
else:
    print(False)


# if len(sys.argv) < 2 or len(sys.argv) > 3:
#     print ("[ERROR] You haven't provided 2 currency codes.")
#      #return "[ERROR] You haven't provided 2 currency codes."
# else:
#      if sys.argv[1] and sys.argv[2] in CURRENCIES:
#          from_currency = sys.argv[1]
#          to_currency = sys.argv[2]
#          print("good")