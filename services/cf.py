'''Implement Functions About CodeForce API reading'''

import asyncio
from cgitb import text
import time
import random

import aiohttp


async def cf_request(method_param: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://codeforces.com/api/{method_param}') as res:
            data_dict = await res.json()
    return data_dict


async def get_contests():
    data_dict: dict = await cf_request('contest.list?gym=false')
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
        if (counter > 10) or (contest_dict['phase'] == 'FINISHED'):
            break
        # phase text
        try:
            phase_text = phase_text_dict[contest_dict['phase']]
        except:
            phase_text = contest_dict['phase']
        # starttime
        start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(contest_dict['startTimeSeconds'])))
        # duration
        duration = str(int((contest_dict['durationSeconds']/60)//60))+'小时' + str(int((contest_dict['durationSeconds']/60) % 60))+'分'
        # start to construct single text
        single_re_text = ''
        single_re_text += f'''赛事:<b>{contest_dict['name']}</b> (<code>{contest_dict['id']}</code>)
赛事状态: <b>{phase_text}</b>
赛事类型: <b>{contest_dict['type']}</b>
开始时间: <b>{start_time} UTC</b>
持续时间: <b>{duration}</b>

'''
        re_text += single_re_text
        counter += 1
    return re_text


async def get_user(handle: str, rating_info: bool = True):
    handle = str(handle)
    method_param = f'user.info?handles={handle}'
    # Start to request Info by CF API
    data_dict = await cf_request(method_param=method_param)
    if data_dict['status'] != 'OK':
        return ('error', 'error')
    user_info = data_dict['result'][0]
    # Dump data
    # lastonline
    last_online = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(user_info['lastOnlineTimeSeconds'])))
    # register date
    reg_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(user_info['registrationTimeSeconds'])))
    # rank / phase
    try:
        user_info['rank']
    except:
        user_info['rank'] = '未知'
        user_info['maxRank'] = '未知'
    try:
        user_info['rating']
    except:
        user_info['rating'] = '未知'
        user_info['maxRating'] = '未知'
    # construct Caption
    re_text = ''
    re_text += f'''<b>{user_info['handle']}</b>

注册于: <b>{reg_date}</b>
等级/最高: 
<b>{user_info['rank']}
{user_info['maxRank']}</b>
分数/最高: 
<b>{str(user_info['rating'])}
{str(user_info['maxRating'])}</b>

<a href="https://codeforces.com/profile/{user_info['handle']}">用户档案页面</a>
'''
    return (user_info['titlePhoto'], re_text)
