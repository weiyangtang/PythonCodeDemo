# encoding: utf-8
'''
@author: weiyang_tang
@contact: weiyang_tang@126.com
@file: urpDemo2.py
@time: 2019-02-08 15:19
@desc:
'''

import urllib.request, urllib.parse, urllib.error
import http.cookiejar
from vcode import getVcode
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageEnhance, ImageFilter
import os

capurl = "http://jwurp.hhuc.edu.cn/validateCodeAction.do"        # 验证码地址
posturl = "http://jwurp.hhuc.edu.cn/loginAction.do"              # 登陆地址

cookie_jar = http.cookiejar.CookieJar()
cookie_jar_handler = urllib.request.HTTPCookieProcessor(cookiejar=cookie_jar)
opener = urllib.request.build_opener(cookie_jar_handler)

picture = opener.open(capurl).read()
local = open('D:/image.jpg','wb') # 验证码写入本地project目录下验证码
local.write(picture)              # 显示验证码
local.close()

def ManualLogin():          # 1. 人工识别验证码
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
    zjh = input("请输入学号：")
    mm = input("请输入密码：")
    img = Image.open('D:/image.jpg')
    img.show()
    code = input('请输入验证码：')
    #os.remove('D:/image.jpg')
    postdatas = {'zjh': zjh, 'mm': mm,'v_yzm':code}
    # 模拟登陆教务处
    data = urllib.parse.urlencode(postdatas).encode(encoding='gb2312')
    request = urllib.request.Request(posturl, data, headers)
    try:
        response = opener.open(request)
        html = response.read().decode('gb2312')
        print(html)
    except urllib.error.HTTPError as e:
        print(e.code)

def AutomaticLogin():       # 2. 机器识别验证码，存在一定失败率
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
    code = getVcode()
    postdatas = {'zjh': 'xxx', 'mm': 'xxx', 'v_yzm': code}
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
    #http://jwurp.hhuc.edu.cn/bxqcjcxAction.do
    #http://jwurp.hhuc.edu.cn/gradeLnAllAction.do?type=ln&oper=qbinfo
    gradeUrl = 'http://jwurp.hhuc.edu.cn/bxqcjcxAction.do'
    gradeRequest = urllib.request.Request(gradeUrl)
    responseGrade = opener.open(gradeRequest).read().decode('gb2312')
    print(responseGrade)
    soup = BeautifulSoup(responseGrade,'lxml')
    for th in soup.find_all(name='th'):
        print('%-60s' % th.string.strip(), end=' ')
    print()
    for tr in soup.find_all(class_='odd'):
        for td in tr.find_all(name='td'):
            print('%-60s' % td.string.strip(), end=' ')
        print()

    raw_names = soup.select('<tr class="odd"')
    raw_credits = soup.select('tr > td:nth-of-type(5)')
    raw_types = soup.select('tr > td:nth-of-type(6)')
    raw_grades = soup.select('td > p')

    namelist = []
    typelist = []
    creditlist = []
    gradelist = []

    for raw_name,raw_type,raw_credit,raw_grade in zip(raw_names,raw_types,raw_credits,raw_grades):
        data = [
            raw_name.get_text().strip(),
            raw_type.get_text().strip(),
            raw_credit.get_text().strip(),
            raw_grade.get_text().strip()
        ]
        if(raw_type.get_text().strip() == "必修"):
            namelist.append(data[0])
            typelist.append(data[1])
            creditlist.append(data[2])
            gradelist.append(data[3])

    # 显示成绩表
    table = PrettyTable(["课程名", "课程属性", "学分", "成绩"])
    table.align["课程名"] = "l"
    table.align["课程属性"] = "m"
    table.align["学分"] = "m"
    table.align["成绩"] = "m"
    table.padding_width = 1  # One space between column edges and contents (default)
    for everyname, everytype, everycredit, everygrade in zip(namelist, typelist, creditlist, gradelist):
        table.add_row([everyname, everytype, everycredit, everygrade])
    print(table)

    def getjd(score):
        if score=="优秀": return 5.0
        if score=="良好": return 4.5
        if score=="中等": return 3.5
        if score=="及格": return 2.5
        if score=="不及格": return 0.0
        if float(score)>=90 and float(score)<=100: return 5.0
        if float(score)>=85 and float(score)<=89: return 4.5
        if float(score)>=80 and float(score)<=84: return 4.0
        if float(score)>=75 and float(score)<=79: return 3.5
        if float(score)>=70 and float(score)<=74: return 3.0
        if float(score)>=65 and float(score)<=69: return 2.5
        if float(score)>=60 and float(score)<=65: return 2.0
        if float(score)<=59: return 0.0

    sum_sum = 0.0
    sum_credit = 0.0
    for everygrade,everycredit in zip (gradelist,creditlist):
        sum_credit = sum_credit + float(everycredit)
        sum_sum = sum_sum + getjd(everygrade)*float(everycredit)
    print("总绩点为：",end="")
    print(sum_sum/sum_credit)


if __name__ == '__main__':
    ManualLogin()
    getGrades()
   # getCET()