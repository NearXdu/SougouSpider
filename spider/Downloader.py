# -*- encoding:utf8 -*-
import time

from log.UtilLogger import UtilLogger
from config.Settings import *
import requests
from utils.MysqlUtil import *
from network.Network import *
from datetime import datetime
from models.SougouDetail import SougouDetail

class Downloader(object):
    def __init__(self):
        self.log=UtilLogger('SougouDownloader')

    def save_file(self,content,filename):
        filename=filename+'.scel'
        savePath=os.path.join(SOUGOU_SCELFILE_PATH,filename)
        with open(savePath,'wb') as f:
            f.write(content)
            self.log.log(u'词库文件保存完毕 {}'.format(filename))

    def strip_wd(self, s):
        kwd = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
               '(', ')', '.', '/', '|', '>', '<', '\\', '*', '"', '“', ]
        ans = ''
        for i in s:
            if i not in kwd:
                ans += i
        return ans

    def run(self):
        session=build_session()
        dt=datetime(2017,12,31).strftime('%Y-%m-%d %H:%M:%S')
        result=session.query(SougouDetail).filter(SougouDetail.update_time>=dt).all()
        self.log.log(u'一共 {} 条数据等待下载'.format(len(result)))
        #exit(-1)
        for row in result:
            filename = self.strip_wd(row.filename)
            self.log.log(u'正在下载 {}-{}'.format(row.url,filename))
            content=download_binary_file(row.url)

            tryTime=1
            flag=0
            while content==-1:
                time.sleep(3)
                tryTime=tryTime+1
                self.log.log(u'下载失败正在重试 {}-{}'.format(row.url, filename), 'error')
                if tryTime>3:
                    flag=1
                    break
            if flag:
                self.log.log(u'下载失败 {}-{} '.format(row.url, filename), 'error')
                continue
            self.log.log(u'下载完成正在保存 {}-{}'.format(row.url, filename))
            self.save_file(content,filename)
            self.log.log(u'保存文件完成 {}-{}'.format(row.url,filename))
            time.sleep(1)

if __name__=='__main__':
    d=Downloader()
    d.run()
