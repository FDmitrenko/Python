import sqlite3
from aiogram import Bot, Dispatcher, types, executor

con = sqlite3.connect("main.db")
cur = con.cursor()
cur.execute("CREATE TABLE user_data(id, name, age)")
res = cur.execute("SELECT * FROM user_data")
API_TOKEN = '7857492751:AAGsD_ivlivrkalri1l4T9kqf-1vgIiiqC8'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await message.answer("Привет, я ваш телеграм-бот!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
