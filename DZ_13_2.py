# -*- coding: utf-8 -*-
from pyexpat.errors import messages
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "A"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    print(f'Привет! Я бот помогающий твоему здоровью!')
    #print(f'Запущена команда {message.text}')
    # await message.reply('Привет! Я бот помогающий твоему заданию')

@dp.message_handler(content_types=['text'])
async def all_messages(message):
    print(f'Введите команду /start, чтобы начать общение!')
    #print(f'Введите команду /start, чтобы начать общение! {message.text}')

# @dp.message_handler()
# async def all_messages(message: types.Message):
#     print(f'Введите команду /start, чтобы начать общение {message.text}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
