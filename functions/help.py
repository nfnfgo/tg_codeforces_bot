import asyncio
import time

from telebot.types import Message, InlineKeyboardMarkup, CallbackQuery
from telebot.async_telebot import AsyncTeleBot

from services import button
from services.bot_command import send_to
from functions import guide_doc
from functions import deeplink
import config
from services.user import UserStatus


# ----------------------------------------------------------------
# 初始化主动发送消息部分


# 定义Introduction消息
info_text = f'''<strong>Aria工具小人</strong>
<strong>版本：</strong>0.1.0 <em>Beta</em>
<strong>简介：</strong> 一个可以帮助你订阅番剧，远程操作Aira2的拥有各种奇奇怪怪功能的好用Bot~
<strong>通知/反馈频道：</strong> @{config.bot.channel_username}
'''


# 发送help信息
async def help(message: Message, bot: AsyncTeleBot):
    if (message.text != '/help') and (message.text != '/start'):
        if message.text.startswith('/start'):
            # 此时说明收到的消息应该是deeplink，将消息传给deeplink处理中心
            await deeplink.home(message, bot)
            return
    if message.chat.type != 'private':
        await bot.reply_to(message, '请私聊机器人查看帮助信息')
    await send_to(message, bot, info_text, reply_markup=gen_help_home_markup(), disable_web_page_preview=True)


# help信息按钮
def gen_help_home_markup():
    # 定义各个按钮的信息
    help_get_use_guide_info = {'button': 'help_get_use_guide'}
    return button.gen_markup([['获取使用帮助', help_get_use_guide_info]])


# -------------------------------------------------------------------
# 接受Guide消息并处理


# 定义guide通用的不同类型指令切换查看的按钮
def gen_guide_button(is_admin: bool = False):
    help_guide_bot_info = {'button': 'help_guide_bot'}
    help_guide_func_info = {'button': 'help_guide_func'}
    help_guide_user_info = {'button': 'help_guide_user'}
    help_guide_other_info = {'button': 'help_guide_other'}
    return button.gen_markup([
        ['基本指令', help_guide_bot_info],
        ['功能设置', help_guide_func_info],
        ['用户设置', help_guide_user_info],
        ['其他指令', help_guide_other_info]])


# Callback 获取使用帮助
async def help_get_use_guide(cbq: CallbackQuery, bot: AsyncTeleBot, data_dict: dict):
    user_status = UserStatus(cbq)
    # 如果用户直接用命令呼出
    if isinstance(cbq, Message):
        message: Message = cbq
        # 判断对话类型
        if message.chat.type != 'private':
            await bot.reply_to(message, '请私聊机器人进行进一步操作')
        await send_to(cbq, bot, guide_doc.home, reply_markup=gen_guide_button(),disable_web_page_preview=True)
        return
    # 如果用户使用callback形式调用
    await bot.answer_callback_query(cbq.id, '')
    if data_dict['button'] == 'help_get_use_guide' or isinstance(cbq, Message):
        await send_to(cbq, bot, guide_doc.home, reply_markup=gen_guide_button(), disable_web_page_preview=True)
    # --- 通过 if 实现不同按钮内容切换
    if data_dict['button'] == 'help_guide_bot':
        await bot.edit_message_text(guide_doc.home, cbq.from_user.id, cbq.message.message_id, reply_markup=gen_guide_button(), disable_web_page_preview=True)
    elif data_dict['button'] == 'help_guide_func':
        await bot.edit_message_text(guide_doc.func, cbq.from_user.id, cbq.message.message_id, reply_markup=gen_guide_button())
    elif data_dict['button'] == 'help_guide_user':
        await bot.edit_message_text(guide_doc.user, cbq.from_user.id, cbq.message.message_id, reply_markup=gen_guide_button())
    elif data_dict['button'] == 'help_guide_other':
        await bot.edit_message_text(guide_doc.other, cbq.from_user.id, cbq.message.message_id, reply_markup=gen_guide_button())
