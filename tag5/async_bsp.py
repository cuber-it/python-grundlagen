import asyncio

async def timer(seconds):
    for i in range(1, seconds + 1):
        await asyncio.sleep(1)
        print(f"[TIMER] {i} second(s) passed")

async def do_something():
    for i in range(3):
        await asyncio.sleep(2)
        print(f"[TASK] Work chunk {i + 1} done")

async def main():
    t1 = asyncio.create_task(timer(6))
    t2 = asyncio.create_task(do_something())
    await t1
    await t2

asyncio.run(main())
