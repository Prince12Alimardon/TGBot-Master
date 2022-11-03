import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from utils.misc import subscribtion
from keyboards.inline.subscription import check_btn
from data.config import CHANNELS
from loader import dp, bot
import re


@dp.message_handler(CommandStart(deep_link='kunuz'))
async def bot_start(message: types.Message):
    args = message.get_args()
    text = f"Salom,{message.from_user.full_name}!\n"
    text += f"Sizni {args} tavsiya qildi"
    await message.answer(text)


@dp.message_handler(CommandStart(deep_link='foydaliLink'))
async def bot_start(message: types.Message):
    args = message.get_args()
    text = f"Salom,{message.from_user.full_name}!\n"
    text += f"Sizni {args} tavsiya qildi"
    await message.answer(text)


@dp.message_handler(CommandStart(deep_link=re.compile("[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+")))
async def bot_start(message: types.Message):
    args = message.get_args()
    text = f"Salom,{message.from_user.full_name}!\n"
    text += f"Siz {args} saytidan keldingiz"
    await message.answer(text)


# @dp.message_handler(commands='start')
# @dp.message_handler(text="/start")
# @dp.message_handler(CommandStart())
# @dp.edited_message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f"Salom, {message.from_user.full_name}!")

@dp.message_handler(commands="start")
async def show_channels(msg: types.Message):
    channel_format = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        # logging.info(invite_link)
        channel_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"

    await msg.answer(f"Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling: \n"
                     f"{channel_format}", reply_markup=check_btn,
                     disable_web_page_preview=True)


@dp.callback_query_handler(text="chek_subs")
async def checker(call: types.CallbackQuery):

    await call.answer()
    result = str()
    for channel in CHANNELS:
        status = await subscribtion.check(user_id=call.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f"✅<b>{channel.title}</b> kanaliga obuna bo'lgansiz!\n\n"
        else:
            invite_link = await channel.export_invite_link()
            result += (f"❌<b>{channel.title}</b> kanaliga obuna bo'lmagansiz. "
                       f"<a href='{invite_link}'>Obuna bo'ling</a>\n\n")
    await call.message.answer(result, disable_web_page_preview=True)
