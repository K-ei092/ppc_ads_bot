from aiogram import Router
from aiogram.types import Message
from filters.my_filters import IsSubscriber
from lexicon.lexicon import LEXICON

router = Router()

# Этот хэндлер будет реагировать на любые сообщения
# не от подписчиков канала
@router.message(~IsSubscriber())
async def send_echo(message: Message):
    await message.answer(LEXICON['channel_left'])
