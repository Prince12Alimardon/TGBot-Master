from keyboards.default.ReplyKeyboard import menustart
from loader import dp
from aiogram.types import Message


@dp.message_handler(text="Kurslar")
async def kurslar(msg: Message):
    await msg.answer(f"Kursni tanlang", reply_markup=menustart)
