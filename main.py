import sqlite3
import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message


TOKEN = "7857492751:AAGsD_ivlivrkalri1l4T9kqf-1vgIiiqC8"

# Подключение к базе данных
con = sqlite3.connect("main.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS user_data(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

# Инициализация диспетчера
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user_id = message.from_user.id
    user_name = message.from_user.full_name

    # Проверяем, существует ли пользователь в базе данных
    cur.execute("SELECT * FROM user_data WHERE id=?", (user_id,))
    if not cur.fetchone():
        # Если пользователь не найден, добавляем его в базу данных
        cur.execute("INSERT INTO user_data (id, name) VALUES (?, ?)", (user_id, user_name))
        con.commit()

    await message.answer(f"Привет, {html.bold(user_name)}!")



async def main() -> None:
    # Инициализация экземпляра бота с настройками по умолчанию
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # Запуск обработки событий
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    cur.execute("SELECT * FROM user_data")