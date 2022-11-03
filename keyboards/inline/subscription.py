from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

check_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Obunani tekshirish", callback_data="chek_subs")
        ]
    ]
)