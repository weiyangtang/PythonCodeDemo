# encoding: utf-8
'''
@author: weiyang_tang
@contact: weiyang_tang@126.com
@file: blogMorePopular.py
@time: 2019-02-13 20:06
@desc: 刷博客的阅读量
'''

import urllib.request
import http.cookiejar
import time
import threading

# 博客地址
url = 'https://blog.csdn.net/weiyang_tang/article/details/86771482'
url2 = 'https://blog.csdn.net/weiyang_tang/article/details/86771228'

cookie_jar = http.cookiejar.CookieJar()
cookie_jar_handler = urllib.request.HTTPCookieProcessor(cookiejar=cookie_jar)
opener = urllib.request.build_opener(cookie_jar_handler)


def loginBolg(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
    request = urllib.request.Request(url=url, headers=headers)
    response = opener.open(request)
    html = response.read().decode('utf-8')
    # print(html)


def blog(url):
    for i in range(0, 10):
        loginBolg(url)
        print(url + '  ', i)
        time.sleep(30)


if __name__ == '__main__':
    for i in range(0, 1000):
        loginBolg(url)
        print(url + '  ', i)
        time.sleep(30)

