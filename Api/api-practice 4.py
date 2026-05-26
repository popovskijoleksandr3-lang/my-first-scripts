import requests
try:
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    data = response.json()
    print(f"interesting fact {data['fact']}")
except Exception as a:
    print(f"error {a}")
