# PYTelegrambotApi https://pytba.readthedocs.io/en/latest/index.html

import asyncio
import multiprocessing
import time
import os
from multiprocessing import Process, Pipe, current_process

from telebot.async_telebot import AsyncTeleBot

from functions import help
from functions import timestamp
from functions import callback
from functions import list
from services import regular_caller
import config

# ------------------------------------------------------------------
# 启动regular_caller


# 获取系统类型
path = os.getcwd().replace('\\', '/')
print(path)


# -----------------------------------------------------------------


bot = AsyncTeleBot(config.bot.token, parse_mode='HTML')

# 通过 /help /start 处理用户帮助信息请求
bot.register_message_handler(help.help, commands=['help', 'start'], pass_bot=True)

# 通过/timestamp 或者 /ts 来进行时间戳的一些转换
bot.register_message_handler(timestamp.home, commands=['timestamp', 'ts'], pass_bot=True)

# Use /list or /l to Check CodeForces Contest Digest
bot.register_message_handler(list.home, commands=['list', 'l'], pass_bot=True)

bot.register_callback_query_handler(callback.cbq_master, func=lambda query: True, pass_bot=True)


# -----------------------------------------------------------------
# 启动Bot

if __name__ == '__main__':
    p = multiprocessing.Process(target=regular_caller.main(path))
    p.start()
    asyncio.run(bot.infinity_polling())
