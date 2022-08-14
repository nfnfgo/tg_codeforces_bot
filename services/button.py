import asyncio
import base64
import time

import telebot.async_telebot as telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, BotCommand, CallbackQuery


def gen_markup(botton_list, row_width=2):
    '''
    Generate a Telegram botton configure.

    Paras:
    botton_list: A List Type things. eg:[[bt1,cbq_data1],[bt2,cbq_data2]]
    '''
    buttons = []
    markup = InlineKeyboardMarkup(row_width=row_width)
    for i in botton_list:
        data_dict=i[1]
        data_dict['time']=int(time.time())
        i[1]=str(data_dict)
        # i[1]=base64.b64encode(i[1].encode()).decode()
        button = InlineKeyboardButton(i[0], callback_data=i[1])
        buttons.append(button)
    markup.add(*buttons)
    return markup


# delete a markup of a message (unavailable when message is too old)
async def del_botton(call: CallbackQuery, bot):
    await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, '')
