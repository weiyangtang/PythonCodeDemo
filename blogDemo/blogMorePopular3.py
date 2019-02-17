# encoding: utf-8
'''
@author: weiyang_tang
@contact: weiyang_tang@126.com
@file: blogMorePopular3.py
@time: 2019-02-14 21:49
@desc: 多线程刷博客阅读量
'''

import urllib.request
import http.cookiejar
import time
import _thread
import threading

# 博客地址
url = 'https://blog.csdn.net/weiyang_tang/article/details/86771482'
url2 = 'https://blog.csdn.net/weiyang_tang/article/details/86771228'

cookie_jar = http.cookiejar.CookieJar()
cookie_jar_handler = urllib.request.HTTPCookieProcessor(cookiejar=cookie_jar)
opener = urllib.request.build_opener(cookie_jar_handler)


def blog(url):
    while 1:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
        request = urllib.request.Request(url=url, headers=headers)
        response = opener.open(request)
        html = response.read().decode('utf-8')
        print(url)
        time.sleep(30)


if __name__ == '__main__':
    _thread.start_new_thread(blog, (url,))
    _thread.start_new_thread(blog, (url2,))
    while 1:
        pass
