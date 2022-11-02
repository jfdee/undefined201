from telebot import TeleBot

from config import settings


def get_bot_connect() -> TeleBot:
    return TeleBot(settings.BOT_SECRET_KEY)


__all__ = (
    'get_bot_connect',
)
