import asyncio


## asyncio.wait()
##

class ApiError(Exception):
    pass



async def api_call(message, result=1000, delay=3, raise_exception = False):
    print(message)
    await asyncio.sleep(delay)
    if raise_exception:
        raise ApiError
    else:
        return result


async def main():

    task_1 =  asyncio.create_task(api_call("__1__ Api is being called....", result=1, delay=1))
    task_2 =  asyncio.create_task(api_call("__2__ Api is being called....", result=2, delay=2))
    task_3 =  asyncio.create_task(api_call("__3__ Api is being called....", result=3, delay=3))


    pending = (task_1, task_2, task_3)

    while pending:
        done, pending = await asyncio.wait(pending, return_when=asyncio.ALL_COMPLETED)
        result = done.pop().result()
        print(result)




asyncio.run(main())