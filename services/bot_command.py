from ast import Call
import asyncio

from telebot.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from telebot.async_telebot import AsyncTeleBot


async def send_to(info: Message | CallbackQuery, bot: AsyncTeleBot, text, reply_markup='', disable_web_page_preview=None):
    '''
    A more convenient way to send message (without reply) as a alter of in-built 
    send_message method.

    Notice, this function determine the chat by using from_user, so DO NOT use 
    this function to send a message which should to group, supergroup or other 
    places

    Paras:
    info: Message of CallbackQuery type. program will identify it's type autoly
    text: The text you want to send to the user
    reply_markup='': If appointed, will send message with a InlineKeyBoardMarkup
    '''
    if isinstance(info, Message):
        user_id = info.from_user.id
    elif isinstance(info, CallbackQuery):
        user_id = info.from_user.id
    elif (isinstance(info, int)) or (isinstance(info, str)):
        user_id = int(info)
    else:
        raise Exception('bot_command.py: Failed to get user_id from input info')
        return
    return_msg = await bot.send_message(user_id, text, reply_markup=reply_markup, disable_web_page_preview=disable_web_page_preview)
    return return_msg
