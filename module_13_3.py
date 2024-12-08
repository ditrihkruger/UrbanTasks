from aiogram import  Bot,Dispatcher,executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

token: str
with open(".token") as f:
    token = f.read()

bot = Bot(token)
dp = Dispatcher(bot=bot,storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def start(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

