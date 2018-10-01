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