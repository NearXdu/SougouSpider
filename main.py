# -*- encoding:utf8 -*-
from threading import Thread
import os
from config.Settings import *

from parse.Parse import *
from queue import Queue
import time
from time import gmtime,strftime
from pypinyin import lazy_pinyin
from utils.MysqlUtil import *
from models.SougouKeyword import *

def run():
    for word in transform(SOUGOU_SCELFILE_PATH):
        print (word)

if __name__ == '__main__':
    run()
