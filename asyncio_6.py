import asyncio

from asyncio import Future

### asyncio Future 


async def plan(my_future: Future):
    print('Planning my future...')
    print(f'my future plan is it done? : {my_future.done()} ')
    await asyncio.sleep(1)
    ## setting the result for future obj
    ## before setting result for future_obj.done() will be false 
    my_future.set_result("Bright")




def create() -> Future:
    my_future = Future()

    asyncio.create_task(plan(my_future))

    return my_future

async def main():
    my_future = create()
    result = await my_future
    print(result)


asyncio.run(main())