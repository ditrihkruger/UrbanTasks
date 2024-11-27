from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

bot: Bot
with open(".token") as f:
    bot = Bot(f.read())

dp = Dispatcher()

@dp.message(CommandStart())
async def OnStart():
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))