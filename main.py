# -*- encoding:utf8 -*-
from threading import Thread
import os
from config.Settings import *

from parse.Parse import *
from queue import Queue
import time
from time import gmtime, strftime
from pypinyin import lazy_pinyin
from utils.MysqlUtil import *
from models.SougouKeyword import *
from parse.Parse import *
from utils.RedisUtil import RedisUtil
from utils.DataHolder import DataHolder
from multiprocessing import Pool
from utils.Utils import *
from utils.NoUse import NoUse

numOfThreads=3

q = Queue()

def save():
    session = build_session()
    while True:
        result = q.get()
        if result is None:
            break
        session.add(SougouKeyword(**result))
        session.commit()
        q.task_done()
    session.close()


def run():
    threads=[]
    for i in range(numOfThreads):
        t=Thread(target=save)
        t.start()
        threads.append(t)

    ru = RedisUtil()
    dh = DataHolder()
    for file in os.listdir(SOUGOU_SCELFILE_PATH):
        words = process(os.path.join(SOUGOU_SCELFILE_PATH, file))
        for word in words:
            hash = Utils.hash(word)
            if ru.hget('SougouKeywordHash', dh.set(hash)):
                continue
            ru.hset('SougouKeywordHash', dh.get(), 1)
            result = {
                'keyword': word,
                'create_time': strftime("%Y-%m-%d %H:%M:%S", gmtime()),
                'update_time': strftime("%Y-%m-%d %H:%M:%S", gmtime()),
            }
            q.put(result)
    q.join()
    for i in range(numOfThreads):
        q.put(None)
    for t in threads:
        t.join()


if __name__ == '__main__':
    run()
