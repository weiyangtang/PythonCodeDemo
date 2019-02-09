# encoding: utf-8
'''
@author: weiyang_tang
@contact: weiyang_tang@126.com
@file: URP_spider4.py
@time: 2019-02-09 15:13
@desc:  基于百度OCR的验证码识别技术的URP教务系统的爬虫技术
'''

import urllib.request, urllib.parse, urllib.error
import http.cookiejar
from BaiduOcr import getVcode
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageEnhance, ImageFilter
import os
import xlwt
import xlrd
from xlutils.copy import copy

name = '1663710324'
capurl = "http://jwurp.hhuc.edu.cn/validateCodeAction.do"  # 验证码地址
posturl = "http://jwurp.hhuc.edu.cn/loginAction.do"  # 登陆地址

cookie_jar = http.cookiejar.CookieJar()
cookie_jar_handler = urllib.request.HTTPCookieProcessor(cookiejar=cookie_jar)
opener = urllib.request.build_opener(cookie_jar_handler)

picture = opener.open(capurl).read()
local = open('D:/image.jpg', 'wb')  # 验证码写入本地project目录下验证码
local.write(picture)  # 显示验证码
local.close()


def ManualLogin():  # 1. 人工识别验证码
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
    zjh = input("请输入学号：")
    mm = input("请输入密码：")
    img = Image.open('D:/image.jpg')
    img.show()
    code = input('请输入验证码：')
    # os.remove('D:/image.jpg')
    postdatas = {'zjh': zjh, 'mm': mm, 'v_yzm': code}
    # 模拟登陆教务处
    data = urllib.parse.urlencode(postdatas).encode(encoding='gb2312')
    request = urllib.request.Request(posturl, data, headers)
    try:
        response = opener.open(request)
        html = response.read().decode('gb2312')
        print(html)
    except urllib.error.HTTPError as e:
        print(e.code)


def AutomaticLogin():  # 2. 机器识别验证码，存在一定失败率
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        # 'Cookie': 'JSESSIONID=cbdzdu9dDqIEFaicXamJw',
        'Host': 'jwurp.hhuc.edu.cn',
        'Origin': 'http://jwurp.hhuc.edu.cn',
        'Referer': 'http://jwurp.hhuc.edu.cn/loginAction.do'
    }
    code = getVcode()
    print(code)
    postdatas = {'zjh': '1663710324', 'mm': '1663710324', 'v_yzm': code}
    # 模拟登陆教务处
    data = urllib.parse.urlencode(postdatas).encode(encoding='gb2312')
    request = urllib.request.Request(posturl, data, headers)
    try:
        response = opener.open(request)
        html = response.read().decode('gb2312')
        print(html)
    except urllib.error.HTTPError as e:
        print(e.code)


def getGrades():
    # 获取成绩
    # http://jwurp.hhuc.edu.cn/bxqcjcxAction.do
    # http://jwurp.hhuc.edu.cn/gradeLnAllAction.do?type=ln&oper=qbinfo
    gradeUrl = 'http://jwurp.hhuc.edu.cn/bxqcjcxAction.do'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        'Cookie': 'JSESSIONID=cbdzdu9dDqIEFaicXamJw'
        # 'Host': 'jwurp.hhuc.edu.cn',
        # 'Origin': 'http://jwurp.hhuc.edu.cn',
        # 'Referer': 'http://jwurp.hhuc.edu.cn/loginAction.do'
    }
    gradeRequest = urllib.request.Request(gradeUrl)
    responseGrade = opener.open(gradeRequest).read().decode('gb2312')
    print(responseGrade)
    soup = BeautifulSoup(responseGrade, 'lxml')

    old_excel = xlrd.open_workbook('data/' + name + '.xls', formatting_info=True)
    new_excel = copy(old_excel)
    ws = new_excel.add_sheet('本学期成绩')
    rowIndex = 0
    colIndex = 0
    for th in soup.find_all(name='th'):
        ws.write(rowIndex, colIndex, th.string.strip())
        colIndex = colIndex + 1
        print('%-60s' % th.string.strip(), end=' ')
    print()
    colIndex = 0
    rowIndex = 1
    for tr in soup.find_all(class_='odd'):
        colIndex = 0
        for td in tr.find_all(name='td'):
            ws.write(rowIndex, colIndex, td.string.strip())
            colIndex = colIndex + 1
            print('%-60s' % td.string.strip(), end=' ')
        rowIndex = rowIndex + 1

        print()
    new_excel.save('data/' + name + '.xls')


def getPersonalInfo():
    global name
    personalInfoUrl = 'http://jwurp.hhuc.edu.cn/xjInfoAction.do?oper=xjxx'
    gradeRequest = urllib.request.Request(personalInfoUrl)
    responseGrade = opener.open(gradeRequest).read().decode('gb2312')
    print(responseGrade)
    myWorkbook = xlwt.Workbook()
    # 3. 添加Excel工作表
    mySheet = myWorkbook.add_sheet('个人信息')
    rowIndex = 0
    colIndex = 0
    soup = BeautifulSoup(responseGrade, 'lxml')
    for table in soup.find_all(id='tblView'):
        for tr in table.find_all(name='tr'):
            colIndex=0
            for td in tr.find_all(name='td'):
                if td.string != None:
                    mySheet.write(rowIndex, colIndex, td.string.strip())
                    colIndex = colIndex + 1
                    print(td.string, end='')
            rowIndex = rowIndex + 1
        print()
    myWorkbook.save('data/' + name + '.xls')


if __name__ == '__main__':
    # ManualLogin()
    AutomaticLogin()
    getPersonalInfo()
    getGrades()

# getCET()
