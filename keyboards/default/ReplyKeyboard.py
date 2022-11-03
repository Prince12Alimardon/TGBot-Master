from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging

menustart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kurslar"),
            KeyboardButton(text="Biz Haqimizda")
        ]
    ], resize_keyboard=True
)