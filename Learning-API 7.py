import requests
try:
    url = "https://catfact.ninja/fact"
    with requests.Session() as session:
        for i in range(5):
            data = session.get(url).json()
            length = len(data['fact'])
            print("_" * length)
            print(data['fact'])
            print("_" * length)
except Exception as e:
    print(e)