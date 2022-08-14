'''plain.py

All message without any specific command should be pass through this file, 
this file take in charge of deal and distribute the input message to 
proper function which should be deal it.

uncommanded messages are often sent by the user that already in some status, 
so the read status operation may be done in this file so that the function 
can clear this message should be distribute to where

About Timeout: since different functions have different acquire to time, 
we suppose DO NOT deal with anything about timeout in this file. Time limit 
should be dealed in separate function files
'''

import asyncio
import time

from telebot.types import Message, InlineKeyboardMarkup, CallbackQuery
from telebot.async_telebot import AsyncTeleBot

from services import button
from services import sql
from services.user import UserStatus
from services.bot_command import send_to
from functions import add_channel
from functions import del_channel
from functions import log
from functions import category
import config


# 私人信息的统一handler
async def private_text_master(message:Message,bot:AsyncTeleBot):
    # 初始化用户并读取其状态
    user_status=UserStatus(message)
    
    if user_status.status_info=={}:
        print('用户无任何状态，不进行操作')
        await log.log_user(message)
        return
    
    # 若用户存在状态，则开始读取并做出处理（分配到对应函数或做出处理
    try:
        status=user_status.get_status_info(key='status')
        if status[0]=='add_channel':
            await add_channel.add(message,bot)
        if status[0]=='del_channel':
            await del_channel.del_ch(message,bot)

        # 标签设定_输入标签名称
        if status[0]=='category_manage_tag_enter_tag_name':
            await category.enter_tag_name(message,bot)
        # 标签设定_录入新频道
        if status[0]=='category_manage_tag_enter_new_ch':
            await category.enter_new_ch(message,bot)
        # 标签设定_设置分流
        if status[0]=='category_set_tag_bypass_enter_target_chat':
            await category.set_bypass(message,bot)
        if status[0]=='category_add_ch_to_tag':
            await category.add_ch_to_tag_text(message,bot)
        if status[0]=='category_del_ch_from_tag':
            await category.del_ch_from_tag_text(message,bot)
    except Exception as e:
        print('用户状态不为空，但无法读取status键的信息:',e)