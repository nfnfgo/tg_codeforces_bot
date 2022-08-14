import asyncio
import base64

from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
from telebot.async_telebot import AsyncTeleBot

from services.bot_command import send_to


async def home(message: Message, bot: AsyncTeleBot):
    '''A Function that deal with ALL Deeplink message. Like Callback.py'''
    if message.chat.type != 'private':
        await bot.send_message(message.chat.id, '请私聊机器人进行后续操作')
    await send_to(message,bot,'您尚未添加任何有关DeepLink的功能')
    await send_to(message, bot, message.text)
