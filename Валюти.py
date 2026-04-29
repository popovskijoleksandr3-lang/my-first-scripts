import requests

url = "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5"

response = requests.get(url)
data = response.json()

usd_sale = 0

for currency in data:
    if currency['ccy'] == 'USD':
        usd_sale = float(currency['sale'])
        break

print(f"Актуальний курс USD: {usd_sale} грн")