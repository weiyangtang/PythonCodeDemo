# encoding: utf-8
'''
@author: weiyang_tang
@contact: weiyang_tang@126.com
@file: ShenyanLigongURP_spider.py
@time: 2019-02-09 20:54
@desc: 沈阳理工大学教务系统爬虫
'''
import urllib.request, urllib.parse, urllib.error
import http.cookiejar
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageEnhance, ImageFilter
import os
import xlwt
import xlrd
from xlutils.copy import copy

# 登陆地址
posturl = "http://218.25.35.27:8080/(xdliqoi3m2dawiaufemdmlmh)/default2.aspx"

# 课表的url
courseList = 'http://218.25.35.27:8080/(xdliqoi3m2dawiaufemdmlmh)/xskbcx.aspx?xh=1605010203&xm=%C1%F5%C4%DD&gnmkdm=N121603'

#
__VIEWSTATE = 'dDwxMDk3ODU4ODU4O3Q8O2w8aTwxPjs+O2w8dDw7bDxpPDE+O2k8Mj47aTw0PjtpPDc+O2k8OT47aTwxMT47aTwxMz47aTwxNT47aTwyMT47aTwyMz47aTwyNT47aTwyNz47aTwyOT47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8XGU7Pj47Pjs7Pjt0PHQ8cDxwPGw8RGF0YVRleHRGaWVsZDtEYXRhVmFsdWVGaWVsZDs+O2w8eG47eG47Pj47Pjt0PGk8Mz47QDwyMDE4LTIwMTk7MjAxNy0yMDE4OzIwMTYtMjAxNzs+O0A8MjAxOC0yMDE5OzIwMTctMjAxODsyMDE2LTIwMTc7Pj47bDxpPDA+Oz4+Ozs+O3Q8dDw7O2w8aTwwPjs+Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWtpuWPt++8mjE2MDUwMTAyMDM7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWnk+WQje+8muWImOWmrjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85a2m6Zmi77ya5p2Q5paZ56eR5a2m5LiO5bel56iL5a2m6ZmiOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkuJPkuJrvvJrmnZDmlpnmiJDlnovlj4rmjqfliLblt6XnqIs7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOihjOaUv+ePre+8mjE2MDUwMTAyOz4+Oz47Oz47dDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+PjtsPGk8MT47PjtsPHQ8QDA8Ozs7Ozs7Ozs7Oz47Oz47Pj47dDxAMDxwPHA8bDxQYWdlQ291bnQ7XyFJdGVtQ291bnQ7XyFEYXRhU291cmNlSXRlbUNvdW50O0RhdGFLZXlzOz47bDxpPDE+O2k8MD47aTwwPjtsPD47Pj47Pjs7Ozs7Ozs7Ozs+Ozs+O3Q8QDA8cDxwPGw8UGFnZUNvdW50O18hSXRlbUNvdW50O18hRGF0YVNvdXJjZUl0ZW1Db3VudDtEYXRhS2V5czs+O2w8aTwxPjtpPDE+O2k8MT47bDw+Oz4+Oz47Ozs7Ozs7Ozs7PjtsPGk8MD47PjtsPHQ8O2w8aTwxPjs+O2w8dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47aTw1Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDzlt6XnqIvlspfkvY3lrp7ot7U7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOmprOaYji/mnZzmmZPmmI47Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDEwLjAwOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwwMS0yMDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Jm5ic3BcOzs+Pjs+Ozs+Oz4+Oz4+Oz4+O3Q8QDA8cDxwPGw8UGFnZUNvdW50O18hSXRlbUNvdW50O18hRGF0YVNvdXJjZUl0ZW1Db3VudDtEYXRhS2V5czs+O2w8aTwxPjtpPDA+O2k8MD47bDw+Oz4+Oz47Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPHA8cDxsPFBhZ2VDb3VudDtfIUl0ZW1Db3VudDtfIURhdGFTb3VyY2VJdGVtQ291bnQ7RGF0YUtleXM7PjtsPGk8MT47aTwyPjtpPDI+O2w8Pjs+Pjs+Ozs7Ozs7Ozs7Oz47bDxpPDA+Oz47bDx0PDtsPGk8MT47aTwyPjs+O2w8dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8MjAxOC0yMDE5Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwxOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzmnLrmorDorr7orqFC6K++56iL6K6+6K6hOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzotbXmu6HlubMv546L6ZOB5YabOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDw0LjA7Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDwyMDE4LTIwMTk7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDE7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOW3peeoi+Wyl+S9jeWunui3tTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86ams5piOL+adnOaZk+aYjjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MTAuMDA7Pj47Pjs7Pjs+Pjs+Pjs+Pjs+Pjs+Pjs+IbBrMxUjkUtOrAdiwRlXQ05AStg='

# 教务成绩的url
scoreUrl = 'http://218.25.35.27:8080/(xdliqoi3m2dawiaufemdmlmh)/xscjcx.aspx?xh=1605010203&xm=%C1%F5%C4%DD&gnmkdm=N121605'

cookie_jar = http.cookiejar.CookieJar()
cookie_jar_handler = urllib.request.HTTPCookieProcessor(cookiejar=cookie_jar)
opener = urllib.request.build_opener(cookie_jar_handler)
score__VIEWSTATE = 'demo'


def login():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
    userId = '1605010203'
    password = 'ni012627'
    postdatas = {
        '__VIEWSTATE': 'dDwxODI0OTM5NjI1Ozs+ErNwwEBfve9YGjMA8xEN6zdawEw=',
        'TextBox1': userId,
        'TextBox2': password,
        'RadioButtonList1': '(unable to decode value)',
        'Button1': '',
        'lbLanguage': ''
    }
    # 模拟登陆教务处
    data = urllib.parse.urlencode(postdatas).encode(encoding='gb2312')
    request = urllib.request.Request(posturl, data, headers)
    try:
        response = opener.open(request)
        html = response.read().decode('gb2312')
        # print(html)
    except urllib.error.HTTPError as e:
        print(e.code)


def getCourseList():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        'Referer': 'http://218.25.35.27:8080/(xdliqoi3m2dawiaufemdmlmh)/default2.aspx'
    }
    courseUrl = 'http://218.25.35.27:8080/(xdliqoi3m2dawiaufemdmlmh)/xskbcx.aspx?xh=1605010203&xm=%C1%F5%C4%DD&gnmkdm=N121603'

    # 学年和学期
    postdatas = {
        '__EVENTTARGET': 'xqd',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': __VIEWSTATE,
        'xnd': '2018-2019',
        'xqd': '2'
    }
    data = urllib.parse.urlencode(postdatas).encode(encoding='gb2312')
    coureseRequest = urllib.request.Request(courseUrl, data, headers=headers)
    responseGrade = opener.open(coureseRequest).read().decode('gb2312')
    print(responseGrade)
    responseGrade = (responseGrade.replace('<br>', '')).replace('<br/>', '')
    soup = BeautifulSoup(responseGrade, 'lxml')

    myWorkbook = xlwt.Workbook()
    mySheet = myWorkbook.add_sheet('沈阳理工大学课表')
    rowIndex = 0
    colIndex = 0

    for tables in soup.find_all(id='Table1'):
        for tr in tables.find_all(name='tr'):
            colIndex = 0
            for td in tr.find_all(name='td'):
                if td.string != None:
                    mySheet.write(rowIndex, colIndex, td.string.strip())
                    colIndex = colIndex + 1
                    print(td.string.strip(), end='')
            rowIndex = rowIndex + 1
            print()
    myWorkbook.save('data/沈阳理工大学1605010203课表.xls')


def get__VIEWSTATE():
    global score__VIEWSTATE
    print(score__VIEWSTATE)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        'Referer': 'http://218.25.35.27:8080/(xdliqoi3m2dawiaufemdmlmh)/default2.aspx'
    }
    coureseRequest = urllib.request.Request(scoreUrl, headers=headers)
    responseGrade = opener.open(coureseRequest).read().decode('gb2312')
    # print(responseGrade)
    soup = BeautifulSoup(responseGrade, 'lxml')
    value = soup.find('input', {'name': '__VIEWSTATE'}).get('value')
    print(value)


if __name__ == '__main__':
    login()
    getCourseList()
    # get__VIEWSTATE()
