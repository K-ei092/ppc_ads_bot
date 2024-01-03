from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str            # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота
    chat_id: list[int]    # Список чатов для подписки пользователем
    user_id: str          # ID пользователя xmlriver.com
    apy_key: str          # Токен для доступа к xmlriver.com


@dataclass
class Config:
    tg_bot: TgBot


# Создаем функцию, которая будет читать файл .env и возвращать
# экземпляр класса Config с заполненными полями token и admin_ids
def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMIN_IDS'))),
            chat_id=list(map(int, env.list('CHAT_ID'))),
            user_id=env('USER_ID_XMLRIVER'),
            apy_key=env('API_KEY_XMLRIVER')
        )
    )