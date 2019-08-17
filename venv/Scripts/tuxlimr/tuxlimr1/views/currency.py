from django.shortcuts import render
from django.shortcuts import HttpResponse
import datetime
import requests
import json

cuurency_url = requests.get('https://api.ratesapi.io/api/latest')
cuurency_url_2015 = requests.get('https://api.ratesapi.io/api/2015-01-1')
cuurency_url_2010 = requests.get('https://api.ratesapi.io/api/2010-01-1')

def currency(request):
    try:

        currency = json.loads(cuurency_url.text)
        currency_2015 = json.loads(cuurency_url_2015.text)
        currency_2010 = json.loads(cuurency_url_2010.text)
        GBP = str(currency['rates']['GBP'])
        HKD = str(currency['rates']['HKD'])
        INR = str(currency['rates']['INR'])
        SGD = str(currency['rates']['SGD'])
        CNY = str(currency['rates']['CNY'])
        USD = str(currency['rates']['USD'])
        AUD = str(currency['rates']['AUD'])
        CAD = str(currency['rates']['CAD'])
        MYR = str(currency['rates']['MYR'])
        BGN = str(currency['rates']['BGN'])
        THB = str(currency['rates']['THB'])
        PHP = str(currency['rates']['PHP'])
        RUB = str(currency['rates']['RUB'])
        GBP_2015 = str(currency_2015['rates']['GBP'])
        INR_2015 = str(currency_2015['rates']['INR'])
        SGD_2015 = str(currency_2015['rates']['SGD'])
        USD_2015 = str(currency_2015['rates']['USD'])
        AUD_2015 = str(currency_2015['rates']['AUD'])
        CAD_2015 = str(currency_2015['rates']['CAD'])
        RUB_2015 = str(currency_2015['rates']['RUB'])
        GBP_2010 = str(currency_2010['rates']['GBP'])
        INR_2010 = str(currency_2010['rates']['INR'])
        SGD_2010 = str(currency_2010['rates']['SGD'])
        USD_2010 = str(currency_2010['rates']['USD'])
        AUD_2010 = str(currency_2010['rates']['AUD'])
        CAD_2010 = str(currency_2010['rates']['CAD'])
        RUB_2010 = str(currency_2010['rates']['RUB'])

        INR_USD = round((1 / float(INR) * float(USD)), 4)
        INR_GBP = round((1 / float(INR) * float(GBP)), 4)
        INR_HKD = round((1 / float(INR) * float(HKD)), 4)
        INR_SGD = round((1 / float(INR) * float(SGD)), 4)
        INR_AUD = round((1 / float(INR) * float(AUD)), 4)
        INR_CAD = round((1 / float(INR) * float(CAD)), 4)
        INR_RUB = round((1 / float(INR) * float(RUB)), 4)
        INR_USD_2010 = round((1 / float(INR_2010) * float(USD_2010)), 4)
        INR_GBP_2010 = round((1 / float(INR_2010) * float(GBP_2010)), 4)
        INR_SGD_2010 = round((1 / float(INR_2010) * float(SGD_2010)), 4)
        INR_AUD_2010 = round((1 / float(INR_2010) * float(AUD_2010)), 4)
        INR_CAD_2010 = round((1 / float(INR_2010) * float(CAD_2010)), 4)
        INR_RUB_2010 = round((1 / float(INR_2010) * float(RUB_2010)), 4)
        INR_USD_2015 = round((1 / float(INR_2015) * float(USD_2015)), 4)
        INR_GBP_2015 = round((1 / float(INR_2015) * float(GBP_2015)), 4)
        INR_SGD_2015 = round((1 / float(INR_2015) * float(SGD_2015)), 4)
        INR_AUD_2015 = round((1 / float(INR_2015) * float(AUD_2015)), 4)
        INR_CAD_2015 = round((1 / float(INR_2015) * float(CAD_2015)), 4)
        INR_RUB_2015 = round((1 / float(INR_2015) * float(RUB_2015)), 4)

        USD_INR = round((1 / float(USD) * float(INR)), 4)
        USD_USD = round((1 / float(USD) * float(USD)), 4)
        USD_GBP = round((1 / float(USD) * float(GBP)), 4)
        USD_SGD = round((1 / float(USD) * float(SGD)), 4)
        USD_AUD = round((1 / float(USD) * float(AUD)), 4)
        USD_CAD = round((1 / float(USD) * float(CAD)), 4)
        USD_RUB = round((1 / float(USD) * float(RUB)), 4)
        USD_INR_2015 = round((1 / float(USD_2015) * float(INR_2015)), 4)
        USD_USD_2015 = round((1 / float(USD_2015) * float(USD_2015)), 4)
        USD_GBP_2015 = round((1 / float(USD_2015) * float(GBP_2015)), 4)
        USD_SGD_2015 = round((1 / float(USD_2015) * float(SGD_2015)), 4)
        USD_AUD_2015 = round((1 / float(USD_2015) * float(AUD_2015)), 4)
        USD_CAD_2015 = round((1 / float(USD_2015) * float(CAD_2015)), 4)
        USD_RUB_2015 = round((1 / float(USD_2015) * float(RUB_2015)), 4)
        USD_INR_2010 = round((1 / float(USD_2010) * float(INR_2010)), 4)
        USD_USD_2010 = round((1 / float(USD_2010) * float(USD_2010)), 4)
        USD_GBP_2010 = round((1 / float(USD_2010) * float(GBP_2010)), 4)
        USD_SGD_2010 = round((1 / float(USD_2010) * float(SGD_2010)), 4)
        USD_AUD_2010 = round((1 / float(USD_2010) * float(AUD_2010)), 4)
        USD_CAD_2010 = round((1 / float(USD_2010) * float(CAD_2010)), 4)
        USD_RUB_2010 = round((1 / float(USD_2010) * float(RUB_2010)), 4)

        return render(request, 'currency.html',
                      {'GBP': GBP, "HKD": HKD, "INR": INR, "SGD": SGD, "CNY": CNY, "USD": USD, "AUD": AUD, "CAD": CAD,
                       "MYR": MYR,
                       "BGN": BGN, "THB": THB, "PHP": PHP, "RUB": RUB, "INR_USD": INR_USD,
                       "INR_GBP": INR_GBP, "INR_SGD": INR_SGD, "INR_AUD": INR_AUD, "INR_CAD": INR_CAD,
                       "INR_RUB": INR_RUB,
                       "USD_INR": USD_INR, "USD_USD": USD_USD, "USD_GBP": USD_GBP, "USD_SGD": USD_SGD,
                       "USD_AUD": USD_AUD, "USD_CAD": USD_CAD, "USD_RUB": USD_RUB,

                       'GBP_2010': GBP_2010, "INR_2010": INR_2010, "SGD_2010": SGD_2010
                          , "USD_2010": USD_2010, "AUD_2010": AUD_2010, "CAD_2010": CAD_2010,
                       "RUB_2010": RUB_2010, "INR_USD_2010": INR_USD_2010, "INR_GBP_2010": INR_GBP_2010,
                       "INR_SGD_2010": INR_SGD_2010, "INR_AUD_2010": INR_AUD_2010,
                       "INR_CAD_2010": INR_CAD_2010, "INR_RUB_2010": INR_RUB_2010, "USD_INR_2010": USD_INR_2010,
                       "USD_USD_2010": USD_USD_2010, "USD_GBP_2010": USD_GBP_2010,
                       "USD_SGD_2010": USD_SGD_2010, "USD_AUD_2010": USD_AUD_2010, "USD_CAD_2010": USD_CAD_2010,
                       "USD_RUB_2010": USD_RUB_2010,

                       'GBP_2015': GBP_2015, "INR_2015": INR_2015, "SGD_2015": SGD_2015,
                       "USD_2015": USD_2015, "AUD_2015": AUD_2015, "CAD_2015": CAD_2015,
                       "RUB_2015": RUB_2015, "INR_USD_2015": INR_USD_2015,
                       "INR_GBP_2015": INR_GBP_2015, "INR_SGD_2015": INR_SGD_2015, "INR_AUD_2015": INR_AUD_2015,
                       "INR_CAD_2015": INR_CAD_2015, "INR_RUB_2015": INR_RUB_2015, "USD_INR_2015": USD_INR_2015,
                       "USD_USD_2015": USD_USD_2015, "USD_GBP_2015": USD_GBP_2015,
                       "USD_SGD_2015": USD_SGD_2015, "USD_AUD_2015": USD_AUD_2015, "USD_CAD_2015": USD_CAD_2015,
                       "USD_RUB_2015": USD_RUB_2015,
                       })

    except:
        return HttpResponse(" We are trying to fetch currency rates")





