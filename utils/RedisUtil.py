# -*- encoding:utf-8 -*-

from redis import Redis
from config import Settings

class RedisUtil(Redis):
    def __init__(self):
        super(RedisUtil,self).__init__(Settings.REDIS_CONFIG['host'],
                                       Settings.REDIS_CONFIG['port'])


class DataHolder(object):
    def __init__(self,value=None):self.value=value
    def set(self,value):self.value=value;return value
    def get(self):return self.value

if __name__ == '__main__':
    ru=RedisUtil()
    data=DataHolder()

    if data.set(ru.get('zx')):
        print data.get()
    else:
        print('asdf')
   
