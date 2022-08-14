'''Implement Functions About CodeForce API reading'''

import asyncio
import time
import random

import aiohttp


async def cd_request(method_param: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://codeforces.com/api/{method_param}') as res:
            data_dict = await res.json()
    return data_dict


async def get_user_info(handle: str, rating_info: bool = True):
    # 检测输入是否合法
    if handle == '':
        return '用户Handle不能为空'
    # 开始获取信息
