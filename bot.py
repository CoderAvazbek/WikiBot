import logging
import wikipedia

from aiogram import Dispatcher, Bot, executor, types

""" Botni ishlatishiz uchun Token quying """
API_TOKEN = ""

logging.basicConfig(level=logging.INFO)

wikipedia.set_lang("uz")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.reply("Wikipedia Botiga xush kelibsiz")


@dp.message_handler()
async def msg(message: types.Message):
    try:
        natija =wikipedia.summary(message.text)
        await message.answer(natija)
    except:
        await message.reply("Bunaqa malumot topilmadi")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)