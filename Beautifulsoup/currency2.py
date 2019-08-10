import requests
import json

# def currency1(a):
cuurency_url = requests.get('https://api.ratesapi.io/api/2015-01-1')
currency12 = json.loads(cuurency_url.text)
GBP = str(currency12['rates']['GBP'])
HKD = str(currency12['rates']['HKD'])
INR = str(currency12['rates']['INR'])
SGD = str(currency12['rates']['SGD'])
CNY = str(currency12['rates']['CNY'])
USD = str(currency12['rates']['USD'])
AUD = str(currency12['rates']['AUD'])
CAD = str(currency12['rates']['CAD'])
RUB = str(currency12['rates']['RUB'])
INR_USD = round((1/float(INR)*float(USD)), 4)
INR_GBP = round((1/float(INR)*float(GBP)), 4)
INR_HKD = round((1/float(INR)*float(HKD)), 4)
INR_SGD = round((1/float(INR)*float(SGD)), 4)
INR_AUD = round((1/float(INR)*float(AUD)), 4)
INR_CAD = round((1/float(INR)*float(CAD)), 4)
INR_RUB = round((1/float(INR)*float(RUB)), 4)


USD_INR = round((1/float(USD)*float(INR)), 4)
USD_USD = round((1/float(USD)*float(USD)), 4)
USD_GBP = round((1/float(USD)*float(GBP)), 4)
USD_HKD = round((1/float(USD)*float(HKD)), 4)
USD_SGD = round((1/float(USD)*float(SGD)), 4)
USD_AUD = round((1/float(USD)*float(AUD)), 4)
USD_CAD = round((1/float(USD)*float(CAD)), 4)
USD_RUB = round((1/float(USD)*float(RUB)), 4)

print(USD_INR)





