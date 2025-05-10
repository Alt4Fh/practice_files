import asyncio
import time

async def call_api(message, result=100, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result


async def show_message():
    for _ in range(3):
        await asyncio.sleep(1)
        print('Api call in progress.....')


async def main():
    start_time = time.perf_counter()


    message_task = asyncio.create_task(
        show_message()
    )

    task_1 = asyncio.create_task(

    call_api("This is the message one ----..", 300)

    )

    task_2 = asyncio.create_task(
    call_api("This is the message one ----..", 400)
    )
    
    
    price = await task_1
    print(price)

    price = await task_2
    print(price)

    await message_task

    end_time = time.perf_counter()

    print(f"Time elapsed: {end_time - start_time:.3f}")


asyncio.run(main())