import httpx
from fastapi import FastAPI
import uvicorn
url = 'https://catfact.ninja/fact'
url2 = 'http://api.open-notify.org/astros.json'
app = FastAPI()
@app.get("/")
def Hello():
    return {"message": "Hello! if you want to read cat fact print higher /fact if you want to read a information about austronaust print /space"}
@app.get("/fact")
async def fact1():
    try:
        async with httpx.AsyncClient() as session:
            response = await session.get(url)
            data = response.json()
        return {"Fact": f"{data['fact']}"}
    except Exception as e:
        return {f"Error: {e}"}
@app.get("/space")
async def fact2():
    try:
        async with httpx.AsyncClient() as session:
            response = await session.get(url)
            dat = response.json()
        all_people = [f"{p['name']} on {p['craft']}" for p in dat['people']]
        return {"People": all_people}
    except Exception as e:
        return {f"Error: {e}"}

if __name__ =="__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


