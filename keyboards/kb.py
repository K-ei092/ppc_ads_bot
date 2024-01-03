from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# Функция для генерации инлайн-клавиатуры
def create_collect_keyboard() -> InlineKeyboardMarkup:
    button_collect_advertising = InlineKeyboardButton(
        text='Реклама',
        callback_data='^collect^1')

    button_collect_seo = InlineKeyboardButton(
        text='SEO',
        callback_data='^collect^2')

    button_collect_all = InlineKeyboardButton(
        text='Реклама + SEO',
        callback_data='^collect^3')

    keyboard_collect = InlineKeyboardMarkup(inline_keyboard=[
        [button_collect_advertising],
        [button_collect_seo],
        [button_collect_all]
    ])
    return keyboard_collect
