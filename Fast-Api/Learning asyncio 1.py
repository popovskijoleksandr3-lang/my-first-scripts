import asyncio

async def hello():
    print("I need to say hello...")
    await asyncio.sleep(1)
    print("Hello!")

async def main():
    await hello()

asyncio.run(main())