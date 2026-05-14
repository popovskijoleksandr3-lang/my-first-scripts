import requests
url = "https://catfact.ninja/fact"
try:
    responce = requests.get(url,timeout = 5)
    responce.raise_for_status()

    data = responce.json()
    print(f"interesting fact {data['fact']}")
except requests.exceptions.RequestException as e:
    print(f"Happend a problem {e}")
