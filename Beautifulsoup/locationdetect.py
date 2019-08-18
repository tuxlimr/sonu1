import requests

url = "https://wft-geo-db.p.rapidapi.com/v1/locale/locales"

headers = {
    'x-rapidapi-host': "wft-geo-db.p.rapidapi.com",
    'x-rapidapi-key': "889e2d28b2mshdd3a171058f2b5ap179914jsn8f3f81a4aee4"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)