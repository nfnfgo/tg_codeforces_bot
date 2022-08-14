'''Handle /user /u command'''
import asyncio
import time
import json

from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from telebot.async_telebot import AsyncTeleBot

from services import cf
from services.bot_command import send_to, reply


async def home(message: Message, bot: AsyncTeleBot):
    text = message.text
    try:
        text = text.split(' ', 1)[1]
    except:
        await reply(message, bot, '您并未输入用户参数，请检查输入')
        return
    (photo, caption) = await cf.get_user(text)
    await reply(message, bot, photo=photo, text=caption)
