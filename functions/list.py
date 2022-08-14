import asyncio
import time

from telebot.types import Message, InlineKeyboardMarkup, CallbackQuery
from telebot.async_telebot import AsyncTeleBot

from services import cf
from services.bot_command import send_to,reply

async def home(message:Message,bot:AsyncTeleBot):
    await reply():