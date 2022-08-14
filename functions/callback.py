import asyncio
import base64

from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
from telebot.async_telebot import AsyncTeleBot

from functions import help


async def cbq_master(cbq: CallbackQuery, bot: AsyncTeleBot):
    '''
    Use to get all CallbackQuery Info and pre-deal it, distribute it to the proper function
    '''
    # 从cbq中提取data_dict
    data_dict = cbq.data
    data_dict = eval(data_dict)

    # 读取按钮类型
    bt_type:str = data_dict['button']
    if bt_type == 'help_get_use_guide':  # 获取使用文档
        await help.help_get_use_guide(cbq, bot, data_dict)

    elif bt_type.startswith('help_guide_'):  # 所有的使用文档共用这个按钮
        await help.help_get_use_guide(cbq, bot, data_dict)

    else:
        await bot.answer_callback_query(cbq.id, '服务已关闭或还未开放')
