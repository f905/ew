import random
import string
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = "7421250830:AAF4PERcdNmBZDv0DlOKF5dzJYSTZwJfhpc"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# متغير لتخزين السيشن
session = None

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome! Click a button to proceed.", reply_markup=main_menu())

def main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("إضافة حساب"))
    keyboard.add(types.KeyboardButton("بداية الفحص"))
    return keyboard

@dp.message_handler(lambda message: message.text == "إضافة حساب")
async def add_account(message: types.Message):
    global session
    await message.reply("يرجى إدخال السيشن الخاص بك.")
    dp.register_message_handler(save_session, state='*')

async def save_session(message: types.Message):
    global session
    session = message.text
    await message.reply("تم إضافة السيشن بنجاح!")

@dp.message_handler(lambda message: message.text == "بداية الفحص")
async def start_checking(message: types.Message):
    if session is None:
        await message.reply("يرجى إضافة حساب أولاً!")
        return

    await message.reply("بدأ الفحص...")
    available_users = await check_users()
    
    if available_users:
        for user in available_users:
            await message.reply(f"تم حفظ يوزر رباعي: @{user}")
    else:
        await message.reply("لا توجد يوزرات متاحة.")

async def check_users():
    available_users = []
    charset = "qwertyuiopasdfghjklzxcvbnm1234567890"
    
    for _ in range(2000):  # عدد المحاولات، يمكنك تغييره
        user = ''.join(random.choice(charset) for _ in range(4))
        if is_username_available(user):
            available_users.append(user)
    
    return available_users

def is_username_available(username):
    # هنا يمكنك وضع المنطق للتحقق من توافر اليوزر في تيك توك.
    # يمكن استخدام API تيك توك أو طرق أخرى حسب الحاجة.
    # نحن هنا نعيد True كمثال.
    return True

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
