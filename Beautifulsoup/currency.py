import requests
import json

# def currency1(a):
cuurency_url = requests.get('https://api.ratesapi.io/api/latest')
currency12 = json.loads(cuurency_url.text)
GBP = str(currency12['rates']['GBP'])
HKD = str(currency12['rates']['HKD'])
INR = str(currency12['rates']['INR'])
SGD = str(currency12['rates']['SGD'])
CNY = str(currency12['rates']['CNY'])
USD = str(currency12['rates']['USD'])
AUD = str(currency12['rates']['AUD'])
CAD = str(currency12['rates']['CAD'])
print(GBP)
if __name__ == "__main__":
    print(INR)
    print(SGD)
    print(AUD)
    print(USD)





