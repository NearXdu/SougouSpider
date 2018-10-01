# -*- encoding:utf8 -*-
import os

db_sougou={
	'sougoudb':{
		'drivername':'mysql',
		'username':'root',
		'password':'nightwatch',
		'database':'sougoudb',
		'host':'localhost',
		'port':3306
	}
}


DATABASE = db_sougou

REDIS_CONFIG={
    'host':'127.0.0.1',
    'port':'6379',
}
SOUGOU_START_URL='https://pinyin.sogou.com/dict/cate/index'
SOUGOU_BASE_URL='http://pinyin.sogou.com'


# 娱乐：电影电视剧、明星、音乐
SOUGOU_START_URLS=["https://pinyin.sogou.com/dict/cate/index/426",
                   "https://pinyin.sogou.com/dict/cate/index/427",
                   "https://pinyin.sogou.com/dict/cate/index/429"];

PROJECT_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_LOG_PATH=os.path.join(PROJECT_PATH,'data/log')