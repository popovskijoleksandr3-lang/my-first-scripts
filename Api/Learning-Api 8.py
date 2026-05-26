import  requests
url = "https://catfact.ninja/fact"
with requests.Session() as session:
    for i in range (5):
        data = session.get(url).json()
        print(data["fact"])
