import asyncio
import httpx
url = 'https://catfact.ninja/fact'
async def catafact():
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data=response.json()
        print(data["fact"])
asyncio.run(catafact())