import asyncio
async def cook(dish,time):
    print(f"Починаю готувати {dish}")
    await asyncio.sleep(time)
    print(f"{dish} готова")


async def main():
    results = await asyncio.gather(
        cook("Піца",3),
        cook("Бургер",1),
        cook("Салат",2)
    )

asyncio.run(main())
