# encoding: utf-8
'''
@author: weiyang_tang
@contact: weiyang_tang@126.com
@file: URPspider.py
@time: 2019-02-07 15:41
@desc:  爬教务系统的成绩
'''
# coding=utf-8
import urllib, urllib.request
import urllib.parse

# hosturl用于获取cookies, posturl是登陆请求的URL
hosturl = 'http://bksjw.chd.edu.cn/'
posturl = 'http://bksjw.chd.edu.cn/loginAction.do'

# 获取cookies
# cj = cookielib.LWPCookieJar()
# cookie_support = urllib2.HTTPCookieProcessor(cj)
# opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
# urllib2.install_opener(opener)
# h = urllib2.urlopen(hosturl)

# 伪装成浏览器，反“反爬虫”——虽然我们学校的URP好像没有做反爬虫
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)',
    'Referer': 'http://bksjw.chd.edu.cn/'}
# 构造POST数据 用户名和密码，，自行修改啊，，别乱来啊。
postData = {
    'dllx': 'dldl',
    'zjh': 'xxxx',
    'mm': 'xxxx'}
postData = urllib.parse.urlencode(postData)
# 构造请求
request = urllib.request.urlopen(posturl, postData, headers)
# 登陆
urllib.urlopen(request)
