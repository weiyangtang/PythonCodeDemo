# encoding: utf-8
'''
@author: weiyang_tang
@contact: weiyang_tang@126.com
@file: blogMorePopular4.py
@time: 2019-02-15 11:23
@desc: 对自己所有的csdn博客刷阅读量
'''

import urllib.request
import http.cookiejar
from bs4 import BeautifulSoup
import time
import _thread
import random

# 博客目录页
blogHomeUrl = 'https://blog.csdn.net/weiyang_tang/article/list/'

# 所有博客的url
urls = {}

cookie_jar = http.cookiejar.CookieJar()
cookie_jar_handler = urllib.request.HTTPCookieProcessor(cookiejar=cookie_jar)
opener = urllib.request.build_opener(cookie_jar_handler)

'''
获取所有博客的url
'''


def getAllBlogUrl():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        'cookie': 'smidV2=2018110122420574a75242eb25b7366046ed6cc8b032810009dd6415d6407b0; UN=weiyang_tang; UM_distinctid=16720e4e1936cd-0711e0e334616d-594d2a16-144000-16720e4e195351; uuid_tt_dd=10_37456615810-1544251857479-974541; ARK_ID=JSb9b31053dc13e3138b3a55a8671c6a13b9b3; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=1788*1*PC_VC!5744*1*weiyang_tang; dc_session_id=10_1549667091034.243364; hasSub=true; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1550151196,1550151213,1550152582,1550201178; tipShow=true; yidun_tocken=9ca17ae2e6ffcda170e2e6ee9acf728e89b7bbe9598ca88ba7d84e968a8fbbf33c8da6baa9ef52a6a684d1cf2af0feaec3b92aa2b88d8fed4fbc95a68bef5f939e9ab7c15b8aada9adfc3d91a987adcf6687a7ee9e; aliyun_webUmidToken=TECD1EE0967A2765DAE4030B4D00C86258B8E8EF92267F2826C70E45307; aliyun_UAToken=115#1HkbN11O1TNysxX3TCCb1CsoE51GBJA11g2mOCkwJ1OcAzhC+O0XC5tuKX7GyzeATsfyOt/8y+CFi/JJhUU4AkNca8pAurPQOSfyetT8ukZQgQkRhEPCOSgaCY9XuzFZASAyeKT8ukNQiFMJhUU4AWNcaB6fyzFQgSRlTRDv5Fh8kcX5H6F65jeQSFAFFKjH17Qffq4xHYqjMxk+fhVsEEQ1dvn0u5OVsMlbs07+2qJTfPgJOC9mIqtPNxqAauLX4hp/p8h6OGbibParSl9ST6FaaX9/lDS0BNdUeJdqhKJTR7qfC6wpSXHQIipmgl5BqBeYkNe/99UsVHX2e2rno4f6LIxsX3/it6oMLh0wp1vwEdRlBXRe/BNjnMEkMYMf8chCn1tnkugnv6BqjE9EIiOFYlM2xqnCITP4/LJAdlwkDL/uYV/nLE8mPsAPf4OxaxlSpuSQ0S8YOJLG6AGvR/ALAPxfkY2E1YNY9yLoKvPHfiSE+rZzHLY5bQQBdtg2OwKyyHNHDbLDLDF6LaNqY0wdbalPbM5NNTcdMAxiwKn8Z0iy4ZC067aj; SESSION=34249b3d-d4b3-4b06-b26c-6b757e2b0c9e; UserName=weiyang_tang; UserInfo=17e04c90995c4ad18c64a2ef57315f3a; UserToken=17e04c90995c4ad18c64a2ef57315f3a; UserNick=weiyang_tang; AU=FC8; BT=1550202289040; dc_tos=pmy7sq; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1550202363'
    }
    links = []
    for i in range(1, 10):
        url = blogHomeUrl + str(i) + '?'
        request = urllib.request.Request(url=url, headers=headers)
        response = opener.open(request)
        html = response.read().decode('utf-8')
        # print(html)
        soup = BeautifulSoup(html, 'lxml')
        for each in soup.find_all(class_="content"):
            for link in each.find_all('a'):
                if str(link.attrs['href']).__contains__('weiyang_tang'):
                    links.append(link.attrs['href'])
    return links


def getMorePopular(url):
    index = 1
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        'cookie': 'smidV2=2018110122420574a75242eb25b7366046ed6cc8b032810009dd6415d6407b0; UN=weiyang_tang; UM_distinctid=16720e4e1936cd-0711e0e334616d-594d2a16-144000-16720e4e195351; uuid_tt_dd=10_37456615810-1544251857479-974541; ARK_ID=JSb9b31053dc13e3138b3a55a8671c6a13b9b3; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=1788*1*PC_VC!5744*1*weiyang_tang; dc_session_id=10_1549667091034.243364; hasSub=true; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1550151196,1550151213,1550152582,1550201178; tipShow=true; yidun_tocken=9ca17ae2e6ffcda170e2e6ee9acf728e89b7bbe9598ca88ba7d84e968a8fbbf33c8da6baa9ef52a6a684d1cf2af0feaec3b92aa2b88d8fed4fbc95a68bef5f939e9ab7c15b8aada9adfc3d91a987adcf6687a7ee9e; aliyun_webUmidToken=TECD1EE0967A2765DAE4030B4D00C86258B8E8EF92267F2826C70E45307; aliyun_UAToken=115#1HkbN11O1TNysxX3TCCb1CsoE51GBJA11g2mOCkwJ1OcAzhC+O0XC5tuKX7GyzeATsfyOt/8y+CFi/JJhUU4AkNca8pAurPQOSfyetT8ukZQgQkRhEPCOSgaCY9XuzFZASAyeKT8ukNQiFMJhUU4AWNcaB6fyzFQgSRlTRDv5Fh8kcX5H6F65jeQSFAFFKjH17Qffq4xHYqjMxk+fhVsEEQ1dvn0u5OVsMlbs07+2qJTfPgJOC9mIqtPNxqAauLX4hp/p8h6OGbibParSl9ST6FaaX9/lDS0BNdUeJdqhKJTR7qfC6wpSXHQIipmgl5BqBeYkNe/99UsVHX2e2rno4f6LIxsX3/it6oMLh0wp1vwEdRlBXRe/BNjnMEkMYMf8chCn1tnkugnv6BqjE9EIiOFYlM2xqnCITP4/LJAdlwkDL/uYV/nLE8mPsAPf4OxaxlSpuSQ0S8YOJLG6AGvR/ALAPxfkY2E1YNY9yLoKvPHfiSE+rZzHLY5bQQBdtg2OwKyyHNHDbLDLDF6LaNqY0wdbalPbM5NNTcdMAxiwKn8Z0iy4ZC067aj; SESSION=34249b3d-d4b3-4b06-b26c-6b757e2b0c9e; UserName=weiyang_tang; UserInfo=17e04c90995c4ad18c64a2ef57315f3a; UserToken=17e04c90995c4ad18c64a2ef57315f3a; UserNick=weiyang_tang; AU=FC8; BT=1550202289040; dc_tos=pmy7sq; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1550202363'
    }
    while 1:
        request = urllib.request.Request(url=url, headers=headers)
        response = opener.open(request)
        print(url, '\t', index)
        index = index + 1
        time.sleep(random.randint(30, 40))


if __name__ == '__main__':
    links = getAllBlogUrl()
    links = set(links)
    print(links.__len__())
    for link in links:
        _thread.start_new_thread(getMorePopular, (link,))
    while 1:
        pass
