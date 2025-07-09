import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from itertools import cycle

API_TOKEN = '7768673520:AAHTQe52AOn3m11iAY9Qst4ndxKqO61EpTA'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

forecasts = cycle([
    "⚽ Ман Сити — Реал Мадрид\nСтавка: ТБ(2.5)\nКэф: 1.85",
    "🏀 Лейкерс — Майами\nСтавка: П1\nКэф: 1.70",
    "🎾 Джокович — Надаль\nСтавка: Победа 1\nКэф: 2.10"
])

current_forecast = next(forecasts)

reviews = (
    "👤 Артём, 21 год:\nПоднял 3к с сотки за 2 часа. Бот 🔥",
    "👤 Илья, 17 лет:\nСначала не верил, потом залетело 10к!",
    "👤 Марат, 23 года:\nСтавки не сливают, прогнозы топ."
)

kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎯 Получить прогноз")],
        [KeyboardButton(text="💬 Отзывы"), KeyboardButton(text="🛠 Поддержка")]
    ],
    resize_keyboard=True
)

@dp.message(Command(commands=["start"]))
async def start_handler(message: types.Message):
    await message.answer("Добро пожаловать!\nВыбирай действие:", reply_markup=kb)

@dp.message(Text(text="🎯 Получить прогноз"))
async def forecast_handler(message: types.Message):
    await message.answer(
        f"🔥 Прогноз на сегодня:\n{current_forecast}\n\n"
        "🎁 Регистрируйся и получи бонус до 500%!\n"
        "👉 https://1wdruc.life/?open=register&p=w8k5"
    )

@dp.message(Text(text="💬 Отзывы"))
async def reviews_handler(message: types.Message):
    await message.answer("\n\n".join(reviews))

@dp.message(Text(text="🛠 Поддержка"))
async def support_handler(message: types.Message):
    await message.answer("Если возникли вопросы — пиши: @po1nt1")

async def update_forecast():
    global current_forecast
    while True:
        await asyncio.sleep(43200)  # 12 часов
        current_forecast = next(forecasts)
        logging.info(f"Новый прогноз: {current_forecast}")

async def main():
    asyncio.create_task(update_forecast())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
