# encoding: utf-8
'''
@author: weiyang_tang
@contact: weiyang_tang@126.com
@file: urllibDemo_01.py
@time: 2019-02-08 14:20
@desc: urllib 模块使用案例
'''
# action:login:
# uid: weiyang_tang
# nodetect: false
# domain: hhu.edu.cn
# password: ln520twy
# locale: zh_CN


import urllib.request
import urllib.parse

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'Host': '210.29.97.17:8001',
    'Cookie': 'ASP.NET_SessionId=mt2k0n20w442dzfu32co32qk'
}
# '__EVENTVALIDATION': 'login',
postData = {
    'tbUserName': '1663710324',
    'tbPassword': '1663710324',
    'btLogin': '登 录'
}
url = 'http://210.29.97.17:8001/'
data = bytes(urllib.parse.urlencode(postData), encoding='utf-8')
req = urllib.request.Request(url=url, data=data, headers=header, method='post')  # 构造一个reqest类
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
