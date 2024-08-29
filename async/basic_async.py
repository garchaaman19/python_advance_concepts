# import asyncio

# async def  async_square(num):
#     await asyncio.sleep(2)
#     return num*num

# async def main(n):
#     result=await async_square(n)
#     return result

# print(asyncio.run(main(4)))
import asyncio

async def coroutine_1():
    print("Coroutine 1: Started")
    await asyncio.sleep(2)
    print("Coroutine 1: Ended")

async def coroutine_2():
    print("Coroutine 2: Started")
    await asyncio.sleep(1)
    print("Coroutine 2: Ended")

async def main():
    # Run coroutines concurrently
    await asyncio.gather(coroutine_1(), coroutine_2())

# Run the main coroutine
asyncio.run(main())

