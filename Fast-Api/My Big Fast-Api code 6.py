import requests
from fastapi import FastAPI
import uvicorn
url = 'https://catfact.ninja/fact'
url2 = 'http://api.open-notify.org/astros.json'
app = FastAPI()
@app.get("/")
def Hello():
    return {"message": "Hello! if you want to read cat fact print higher /fact if you want to read a information about austronaust print /space"}
@app.get("/fact")
def fact():
    try:
        with requests.Session() as session:
            data = session.get(url).json()
        return {"Fact": f"{data['fact']}"}
    except Exception as e:
        return {"Error": f"{e}"}
@app.get("/space")
def fact2():
    try:
        with requests.Session() as session:
            dat = session.get(url2).json()
        all_people = [f"{p['name']} on {p['craft']}" for p in dat['people']]
        return {"Astronauts": all_people}
    except Exception as e:
        return {"Error": f"{e}"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


