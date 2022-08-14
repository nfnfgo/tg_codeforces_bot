import asyncio
import time

from telebot.types import Message, InlineKeyboardMarkup, CallbackQuery, Chat
from telebot.async_telebot import AsyncTeleBot

from services.bot_command import send_to


async def home(message: Message, bot: AsyncTeleBot,no_bot=False):
    '''Timestamp便民小功能'''
    text = message.text
    # 删除掉用户信息中的指令部分
    if '/ts' in message.text:
        text = text.replace('/ts ', '')
    if '/timestamp ' in message.text:
        text = text.replace('/timestamp ', '')
    # 确认输入的是时间戳还是时间格式
    if text.startswith('d'):
        text = text.replace('d','')
        local = time.strptime(text, '%Y%m%d%H%M%S')
        timestamp = time.mktime(local)
        await send_to(message, bot, str(int(timestamp)))
    else:
        timestamp = int(text)
        local = time.localtime(timestamp)
        time_read = time.strftime('%Y-%m-%d %H:%M:%S', local)
        await send_to(message, bot, time_read)