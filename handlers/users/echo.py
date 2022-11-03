from aiogram import types
import wikipedia
from loader import dp

wikipedia.set_lang("uz")

# # Echo bot
# @dp.message_handler(state=None)
# async def bot_echo(message: types.Message):
#     await message.answer(message.text)

@dp.message_handler()
async def sendWiki(msg: types.Message):
    print(msg.chat.id)
    try:
        respond = wikipedia.summary(msg.text)
        await msg.answer(respond)
    except:
        await msg.answer("Bu mavzuga oid ma'lumot topilmadi")
