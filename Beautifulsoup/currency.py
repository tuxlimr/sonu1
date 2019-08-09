import requests
import json
r = requests.get('https://api.ratesapi.io/api/latest')

currency = json.loads(r.text)
print("British Pound Currency Rate is equal against one Euro:" + str(currency['rates']['GBP']))
print(currency)