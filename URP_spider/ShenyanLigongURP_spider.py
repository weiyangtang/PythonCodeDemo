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

posturl = "http://jwurp.hhuc.edu.cn/loginAction.do"  # 登陆地址

cookie_jar = http.cookiejar.CookieJar()
cookie_jar_handler = urllib.request.HTTPCookieProcessor(cookiejar=cookie_jar)
opener = urllib.request.build_opener(cookie_jar_handler)

def login():
