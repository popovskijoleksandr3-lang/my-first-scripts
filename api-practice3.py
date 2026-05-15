import requests
try:
    url = "http://api.open-notify.org/astros.json"
    responce = requests.get(url)
    data = responce.json()
    for person in data['people']:
        print(f"{person['name']} is currently on board the {person['craft']}")
except Exception as e:
    print(f"Happend a problem {e}")

