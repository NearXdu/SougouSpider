# -*- encoding:utf8 -*-
from config.Settings import *
from datetime import datetime
import sys
from log.UtilLogger import UtilLogger

reload(sys)
sys.setdefaultencoding('utf8')
from network.Network import *
from bs4 import BeautifulSoup
from utils.Utils import Utils
from utils.NoUse import NoUse
from utils.RedisUtil import RedisUtil
from utils.DataHolder import DataHolder
from utils.MysqlUtil import *
from models.SougouList import SougouList

sys.path.append(PROJECT_PATH)


class Spider(object):

    def __init__(self, urls=SOUGOU_START_URLS):
        self.urls = urls
        # self.log=UtilLogger('SougouSpider',os.path.join(PROJECT_LOG_PATH,'SougouSpider')) # TO FILE
        self.log = UtilLogger('SougouSpider') # to STDOUT

    def get_sougou_list(self):
        NoUse.__no_use__()
        ru = RedisUtil()
        dh = DataHolder()
        self.log.log('开始爬取列表页')
        for url in self.urls:
            self.log.log('正在解析页面 {}'.format(url))
            html = get_html_text(url)
            soup = BeautifulSoup(html, 'lxml')
            tmps = soup.find('div', {'id': 'dict_page_list'})
            pages = map(int, [tmp.get_text() for tmp in tmps.find_all('a')
                              if tmp.get_text().isdigit()])
            page = max(pages)
            self.log.log('页面 {} 一共 {}页'.format(url, page))
            for i in range(1, page + 1):
                listUrl = url + "/default/" + str(i)
                self.log.log('开始解析第{}页-{}'.format(i, listUrl))
                html = get_html_text(listUrl)
                soup = BeautifulSoup(html, 'lxml')
                divs = soup.find_all('div', class_='dict_detail_block')
                self.log.log('解析完成 {}'.format(listUrl))
                session = build_session()
                for data in divs:
                    NoUse.__no_use__()
                    tmpUrl=SOUGOU_BASE_URL + data.find('div', class_='detail_title').a['href']
                    hash = Utils.hash(tmpUrl)
                    if (ru.hget('SougouListHash', dh.set(hash))):
                        self.log.log('url: {} 已经存在！'.format(tmpUrl),'warning')
                        continue
                    ru.hset('SougouListHash', dh.get(), 1)
                    result = {
                        'filename': data.find('div', class_='detail_title').a.text,
                        'url':tmpUrl,
                        'create_time': datetime.strptime(data.find_all('div', class_='show_content')[2].text,
                                                         '%Y-%m-%d %H:%M:%S'),
                        'update_time': datetime.strptime(data.find_all('div', class_='show_content')[2].text,
                                                         '%Y-%m-%d %H:%M:%S'),
                        'hash': hash
                    }
                    models = SougouList(**result)
                    session.add(models)
                    session.commit()
                    self.log.log('正在写入数据 {}-{}'.format(result['url'], result['filename']))
                session.close()


if __name__ == '__main__':
    sp = Spider()
    sp.get_sougou_list()
