# -*- coding: UTF-8 -*-
import requests
def get_html_text(url):
    '''
    请求url的内容

    :param url:
    :return response:
    '''
    try:
        r=requests.get(url,timeout=15,stream=True)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return -1

def download_binary_file(url):
    try:
        r=requests.get('http://'+url,timeout=30,stream=True)
        r.raise_for_status()
        return r.content
    except:
        return -1