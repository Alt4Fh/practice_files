import asyncio


### wait_for and shielding task from being calncelled 
### wrap task in asyncio.shield()
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
        await asyncio.wait_for(asyncio.shield(task), MAX_TIMEOUT) ## wraping task inside shield()
        ## will not be cancelled due to time out
    except TimeoutError:
        print("Task is taking longer than expected will be completed soon.")
        result = await task
        print(result)




asyncio.run(main())