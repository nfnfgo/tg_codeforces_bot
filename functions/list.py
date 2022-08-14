import asyncio
import time

from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton,CallbackQuery
from telebot.async_telebot import AsyncTeleBot

from services import cf
from services.bot_command import send_to, reply


async def home(message: Message, bot: AsyncTeleBot):
    text = await cf.get_contests()
    # Generate InlineKeyboard
    markup=InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('查看详细信息',url='https://codeforces.com/contests'))
    await reply(message, bot, text,reply_markup=markup)
