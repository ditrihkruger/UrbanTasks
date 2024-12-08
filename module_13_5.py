from aiogram import  Bot,Dispatcher,executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.dispatcher import FSMContext

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

token: str
with open(".token") as f:
    token = f.read()

bot = Bot(token)
dp = Dispatcher(bot=bot,storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
calculate_calories_button = KeyboardButton(text="Рассчитать")
info_button = KeyboardButton(text='Информация')
kb.add(calculate_calories_button)
kb.add(info_button)

@dp.message_handler(text = "Рассчитать")
async def set_age(message:types.Message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: State):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: State):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_growth(message: types.Message, state: State):
    await state.update_data(weight = message.text)
    data: dict = await state.get_data()
    a,g,w = map(int,data.values())
    await message.answer("Ваша норма калорий " + str(10*w+6.25*g-5*a+5))
    state.finish()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler()
async def start(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)