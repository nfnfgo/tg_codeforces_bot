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


async def get_contests():
    data_dict: dict = await cd_request('contest.list?gym=false')
        # If API request Failed
    if data_dict['status'] != 'OK':
        return '数据请求失败'
    else:
        result_list = data_dict['result']
    # Read data
    phase_text_dict = {'BEFORE': '❎未开始', 'FINISHED': '⏹️已结束'}
    # Construct text
    re_text = '<b>赛事列表</b>\n'
    # Iterate Some Contests
    counter = 1
    for contest_dict in result_list:
        if counter > 10:
            break
        try:
            phase_text = phase_text_dict[contest_dict['phase']]
        except:
            phase_text = contest_dict['phase']
        single_re_text = ''
        single_re_text += f'''赛事:<b>{contest_dict['name']}</b> (<code>{contest_dict['id']}</code>)
赛事状态: <b>{phase_text}</b>
赛事类型: <b>{contest_dict['type']}</b>

'''
        re_text += single_re_text
        counter += 1
    return re_text


async def get_user_info(handle: str, rating_info: bool = True):
    # 检测输入是否合法
    if handle == '':
        return '用户Handle不能为空'
    # 开始获取信息
