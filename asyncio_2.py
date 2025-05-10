import asyncio
from asyncio import CancelledError


## canceling the task

async def call_api(message, result=1000, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result



async def main():

    task = asyncio.create_task(
    call_api("This is the message one ----..", result=2000, delay=5)
    )


    elapsed_time = 0

    while not task.done():
        elapsed_time += 1
        await asyncio.sleep(1)
        print("Task has not been completed, Checking after a second...")
        
        if elapsed_time == 3:
            task.cancel()
            break

    
    try: 
        await task
    except CancelledError:
        print('Task has been cancelled')
   
  



asyncio.run(main())