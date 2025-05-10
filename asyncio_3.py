import asyncio


### wait_for 
async def api_call(message, result=1000, delay=3):
    print(message)

    await asyncio.sleep(delay)

    return result


async def main():

    task =  asyncio.create_task(
        api_call("He.., Api is being called....", result=2000, delay=5)
    )


    MAX_TIMEOUT = 3 # Seconds

    try:
        await asyncio.wait_for(task, MAX_TIMEOUT)
    except TimeoutError:
        print("Task was cancelled due to time out")



asyncio.run(main())