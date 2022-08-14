'''
This file is designed to start with main.py by using python subprocess module.

Args:
[1]: PATH, should be a string of current working path, used to import DIY package
'''


import os
import time
import asyncio
import sys

print('''
----------------------------------------
Notice:
Subprocess 'regular_caller.py' now has been running in the backend.

Aegv Received:''')
print('C:/Users/17561/Documents/GitHub/Channel_Aggregate_Bot')
print('----------------------------------------')
sys.path.append('C:/Users/17561/Documents/GitHub/Channel_Aggregate_Bot')

from functions import push
import services.sql
from services.sql import create_pool

# ---------------------------------------------------------------
# 定时激活器部分


async def main():
    while True:
        await asyncio.sleep(1)
        # 推送频道消息的函数起点
        await push.start_push()
        # 创建线程池
        await create_pool()


asyncio.run(main())

if __name__ == '__main__':
    asyncio.run(main())