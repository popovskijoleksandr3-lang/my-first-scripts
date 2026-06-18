from fastapi import FastAPI
import httpx
import uvicorn
url = 'https://catfact.ninja/fact'
app = FastAPI()
@app.get("/")
async def fact(): 
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        return {"fact": data['fact']}
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)