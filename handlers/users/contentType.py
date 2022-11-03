from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

@dp.message_handler(content_types='photo')
async def photo_handler(msg: types.Message):
    await msg.answer('Nima rasm bu?')

@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def photo_handler(msg: types.Message):
    await msg.answer('Kim bu?')

@dp.message_handler(content_types='sticker')
# @dp.message_handler(content_types=types.ContentTypes.STICKER)
async def emoji_handler(msg: types.Message):
    await msg.answer('😀')

@dp.message_handler(content_types='contact')
# @dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def contact_handler(msg: types.Message):
    await msg.answer('Kim bu')

@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def audio_handler(msg: types.Message):
    await msg.answer('Yaxshi eshitmadim, yozib yubor')