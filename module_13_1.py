import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1,5):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял шар номер {i}')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    tasks = []
    for strong_man, power in {'one':1, 'two':2, 'three':3}.items():
        tasks.append(asyncio.create_task(start_strongman(strong_man, power)))
    for task in tasks:
        await task

asyncio.run(start_tournament())
