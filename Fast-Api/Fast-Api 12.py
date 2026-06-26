from fastapi import FastAPI
import httpx
import uvicorn
app = FastAPI()
url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
@app.get("/")
async def money():
    async with httpx.AsyncClient() as client:
        response=await client.get(url)
        data=response.json()
        for i in data:
            if i["cc"] == "USD":
                return {"currency": "USD in UAH", "rate": i["rate"]}
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5476)

