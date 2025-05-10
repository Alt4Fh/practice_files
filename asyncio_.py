import asyncio
import time

async def call_api(message, result=100, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result



async def main():
    start_time = time.perf_counter()
    price = await call_api("This is the message one ----..", 300)
    print(price)
    price = await call_api("This is the message one ----..", 400)
    print(price)

    end_time = time.perf_counter()

    print(f"Time elapsed: {end_time - start_time:.3f}")


asyncio.run(main())