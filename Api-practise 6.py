import requests

try:
    url = "https://catfact.ninja/fact"
    for i in range(5):
        response = requests.get(url)
        data = response.json()
        fact = data['fact']
        length = len(fact)
        print("_" * length)
        print(fact)
        print("_" * length)
except Exception as a:
    print(a)