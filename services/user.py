import time
import asyncio

from telebot.types import User, Message, CallbackQuery, BotCommand



# 用户类
class UserStatus():
    # 关于用户类的全局变量
    users_status_info = {}

    def __init__(self, info: int | str | Message | CallbackQuery):
        '''
        Initialize a user and autoly read status through id, message or callbackquery.

        Notice: self.status_info will be an empty dictionary if user has no available status
        '''
        self.status_info = {}
        # 依次根据下方顺序尝试获取User的ID（唯一识别标记）
        if (isinstance(info, int)) or (isinstance(info, str)):
            self.id = int(info)
        elif (isinstance(info, Message)) or (isinstance(info, CallbackQuery)):
            self.id = info.from_user.id
        else:
            raise Exception('Failed to initialize a user since no available id data')
        # 尝试读取用户目前状态并写入 user_status （如果用户目前存在状态的话）
        self.status_info = self.get_status_info()

    def __await__(self, message: Message = None, id: int | str = None, call: CallbackQuery = None):
        return self.__init().__await__()

    # 提供await方法（虽然一个异步操作都没有）
    async def __init(self, message: Message = None, id: int | str = None, call: CallbackQuery = None):
        # 依次根据下方顺序尝试获取User的ID（唯一识别标记）
        if id is not None:
            self.id = int(id)
        elif message is not None:
            self.id = int(message.from_user.id)
        elif call is not None:
            self.id = int(call.from_user.id)
        else:
            raise Exception('Failed to initialize a user since no available id data')

    # 从列表中读取用户的 status_info （如果存在）并写入实例
    def get_status_info(self, key=None):
        '''
        Get Users Status By reading users_status_info
        Return None when user has no status

        Paras:
        self: a StatusUser class instance
        key: default=None, if None, return whole self.status_info dict, if key is specified, 
        return a list that first item would be the info stored and second is the timestamp 
        when it has been set.
        '''
        try:
            self.status_info = self.users_status_info[self.id]
        except:
            self.status_info = {}

        # 如果用户并没有status，则创建空字典，方便后期写入
        if key is None:
            return self.status_info

        # 如果用户指定了查询某个键的值，对其进行返回
        try:
            value_list = self.status_info[key]
            return value_list
        except:
            raise Exception('user.py: Failed to get status_info value list. Maybe key is invalid')

    def set_status_info(self, dict):
        '''
        Set a user status.
        You can pass a key with empty str or None to delete it, and if it doesn't exist, raise exception

        Paras:
        dict: dict type. key should be the status key, value should be the data info that you want 
        to store. timestamp is not needed since it would be added automatically
        '''
        timestamp = time.time()
        for item in dict.items():
            if (item[1] is None) or (item[1] == ''):
                try:
                    del self.status_info[item[0]]
                except Exception as e:
                    print('service/user.py: Failed to del a status_key.', e)
                continue
            self.status_info[item[0]] = [item[1], time.time()]
        self.users_status_info[self.id] = self.status_info

    def del_status_info(self):
        '''Delete **all** the status of a bot.
        Cautions: This Method doesn't means delete some single keys
        (if you need that please use set_status_info).
        Instead it will delete the whole status_info dictionary 
        of this user, and delete it from users_status_info global list
        '''
        try:
            del self.users_status_info[self.id]
        except Exception as e:
            print('service/user.py Failed to delete a whole user status_info', e)