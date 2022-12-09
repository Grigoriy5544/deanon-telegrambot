import aiogram
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from aiogram import Bot, types, Dispatcher, executor
from time import sleep

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет, я могу пробить информацию по номеру телефона.\nПопробуйте написать /phone +79999999999")

@dp.message_handler(commands=['phone'])
async def echo_message(msg: types.Message):
    phoneNumber = phonenumbers.parse(msg.text)
    Carrier = carrier.name_for_number(phoneNumber, 'ru')
    Region = geocoder.description_for_number(phoneNumber, 'ru')
    timeZone = timezone.time_zones_for_number(phoneNumber)
    valid = phonenumbers.is_valid_number(phoneNumber)
    if valid:
        await bot.send_message(msg.from_user.id, f'Страна: {Region}')
        await bot.send_message(msg.from_user.id, f'Город: {timeZone}')
        await bot.send_message(msg.from_user.id, f'Оператор: {Carrier}')
    else:
        await bot.send_message(msg.from_user.id, 'Номер не существует')

if __name__ == '__main__':
    executor.start_polling(dp)