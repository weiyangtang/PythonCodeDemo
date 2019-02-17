# encoding: utf-8
'''
@author: weiyang_tang
@contact: weiyang_tang@126.com
@file: HoHaiUrpSpider.py
@time: 2019-02-17 14:59
@desc: 基于百度OCR的API识别验证码,河海大学教务系统爬虫
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
# 1662810330
SNO = '1663710324'  # 学号
pwd = '1663710324'  # 密码
SName=''#学生姓名不用写
capurl = "http://jwurp.hhuc.edu.cn/validateCodeAction.do"  # 验证码地址
loginUrl = "http://jwurp.hhuc.edu.cn/loginAction.do"  # 登陆地址

cookie_jar = http.cookiejar.CookieJar()
cookie_jar_handler = urllib.request.HTTPCookieProcessor(cookiejar=cookie_jar)
opener = urllib.request.build_opener(cookie_jar_handler)


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
    request = urllib.request.Request(loginUrl, data, headers)
    try:
        response = opener.open(request)
        html = response.read().decode('gb2312')
        print(html)
    except urllib.error.HTTPError as e:
        print(e.code)


def AutomaticLogin():  # 利用百度ocr识别验证码,为了弥补识别可能出错的缺陷,识别错误多次识别,若多次识别仍是错误,则认为是学号和密码不符

    picture = opener.open(capurl).read()
    local = open('D:/image.jpg', 'wb')  # 验证码写入本地project目录下验证码
    local.write(picture)  # 显示验证码
    local.close()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        'Host': 'jwurp.hhuc.edu.cn',
        'Origin': 'http://jwurp.hhuc.edu.cn',
        'Referer': 'http://jwurp.hhuc.edu.cn/loginAction.do'
    }
    code = getVcode()
    print(code)
    postdatas = {'zjh': SNO, 'mm': pwd, 'v_yzm': code}
    # 模拟登陆教务处
    data = urllib.parse.urlencode(postdatas).encode(encoding='gb2312')
    request = urllib.request.Request(loginUrl, data, headers)
    try:
        response = opener.open(request)
        html = response.read().decode('gb2312')
        # print(html)
        soup = BeautifulSoup(html, 'lxml')
        print(soup.title.string)
        title = soup.title.string
        if (title.__contains__('错误信息')):
            print('登录失败')
            AutomaticLogin()
        else:
            print('登录成功')
    except urllib.error.HTTPError as e:
        print(e.code)


def getGrades():
    scoreList = []  # 存放成绩的
    AutomaticLogin()
    # 获取成绩
    # http://jwurp.hhuc.edu.cn/bxqcjcxAction.do
    # http://jwurp.hhuc.edu.cn/gradeLnAllAction.do?type=ln&oper=qbinfo
    gradeUrl = 'http://jwurp.hhuc.edu.cn/bxqcjcxAction.do'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
    }
    gradeRequest = urllib.request.Request(gradeUrl)
    responseGrade = opener.open(gradeRequest).read().decode('gb2312')
    # print(responseGrade)
    soup = BeautifulSoup(responseGrade, 'lxml')
    if (soup.title.string != None):
        title = soup.title.string
        if (title.__contains__('错误信息')):
            getGrades()
            return None
    # print(soup.title.string)
    old_excel = xlrd.open_workbook('data/' + SNO +'_'+SName+ '.xls', formatting_info=True)
    new_excel = copy(old_excel)
    ws = new_excel.add_sheet('本学期成绩')
    rowIndex = 0
    colIndex = 0

    for th in soup.find_all(name='th'):
        ws.write(rowIndex, colIndex, th.string.strip())
        colIndex = colIndex + 1
        print('%-60s' % th.string.strip(), end=' ')
    print()
    rowIndex = 1
    for tr in soup.find_all(class_='odd'):
        scoreList.append([])
        colIndex = 0
        for td in tr.find_all(name='td'):
            scoreList[rowIndex - 1].append(td.string.strip())
            ws.write(rowIndex, colIndex, td.string.strip())
            colIndex = colIndex + 1
            print('%-60s' % td.string.strip(), end=' ')
        rowIndex = rowIndex + 1
        print()
    gpa = getGPA(scoreList)
    ws.write(rowIndex + 2, colIndex, '本学期平均绩点为' + str(gpa))
    print(scoreList)
    new_excel.save('data/' + SNO +'_'+SName+ '.xls')


def getPersonalInfo():
    personalInfo=[]
    AutomaticLogin()
    personalInfoUrl = 'http://jwurp.hhuc.edu.cn/xjInfoAction.do?oper=xjxx'  # 个人信息的url
    gradeRequest = urllib.request.Request(personalInfoUrl)
    responseGrade = opener.open(gradeRequest).read().decode('gb2312')
    # print(responseGrade)
    myWorkbook = xlwt.Workbook()
    mySheet = myWorkbook.add_sheet('个人信息')
    rowIndex = 0
    soup = BeautifulSoup(responseGrade, 'lxml')
    if (soup.title.string != None):
        title = soup.title.string
        if (title.__contains__('错误信息')):
            getPersonalInfo()
            return None
    for table in soup.find_all(id='tblView'):
        for tr in table.find_all(name='tr'):
            personalInfo.append([])
            colIndex = 0
            for td in tr.find_all(name='td'):
                if td.string != None:
                    personalInfo[rowIndex].append(td.string.strip())
                    mySheet.write(rowIndex, colIndex, td.string.strip())
                    colIndex = colIndex + 1
                    print(td.string.strip(), end='')
            rowIndex = rowIndex + 1
        print()
    global SName
    SName=personalInfo[0][3]
    myWorkbook.save('data/' + SNO +'_'+SName+ '.xls')


'''
计算本学期的平均绩点
'''


def getGPA(scoreList):
    sumCredit = 0
    sumPA = 0.0
    for rowIndex in range(len(scoreList)):
        if scoreList[rowIndex][5] == '必修':
            sumCredit = sumCredit + float(scoreList[rowIndex][4])
            sumPA = sumPA + getPA(scoreList[rowIndex][9]) * float(scoreList[rowIndex][4])
    avgPA = sumPA / sumCredit
    print('本学期平均绩点为' + str(avgPA))
    return avgPA


def getPA(score):
    if score == "优秀": return 5.0
    if score == "良好": return 4.5
    if score == "中等": return 3.5
    if score == "及格": return 2.5
    if score == "不及格": return 0.0
    if float(score) >= 90 and float(score) <= 100: return 5.0
    if float(score) >= 85 and float(score) <= 89: return 4.5
    if float(score) >= 80 and float(score) <= 84: return 4.0
    if float(score) >= 75 and float(score) <= 79: return 3.5
    if float(score) >= 70 and float(score) <= 74: return 3.0
    if float(score) >= 65 and float(score) <= 69: return 2.5
    if float(score) >= 60 and float(score) <= 65: return 2.0
    if float(score) <= 59: return 0.0


if __name__ == '__main__':
    # ManualLogin()
    AutomaticLogin()
    getPersonalInfo()
    getGrades()
