# encoding: utf-8
'''
@author: weiyang_tang
@contact: weiyang_tang@126.com
@file: baiduAiOCR.py
@time: 2019-02-09 14:53
@desc: 基于百度AI的OCR
'''

# -*- coding: UTF-8 -*-

from aip import AipOcr
import json

# 定义常量
APP_ID = '9851066'
API_KEY = 'LUGBatgyRGoerR9FZbV4SQYk'
SECRET_KEY = 'fB2MNz1c2UHLTximFlC4laXPg7CVfyjV'

# 初始化AipFace对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
filePath = "D:/image.jpg"


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 定义参数变量
options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}

# 调用通用文字识别接口
result = aipOcr.basicGeneral(get_file_content(filePath), options)
print(json.dumps(result))
keyWord = result["words_result"][0]['words'].replace(' ', '')
print(keyWord)
