import requests
try:
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    data = response.json()
    fact = data['fact']
    length = len(fact)
    print("_" * length)
    print(f"{data['fact']}")
    print("_" * length)
except Exception as e:
    print(f"Happend a problem {e}")
