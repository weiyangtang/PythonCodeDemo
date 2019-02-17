# encoding: utf-8
'''
@author: weiyang_tang
@contact: weiyang_tang@126.com
@file: BaiduOcr.py
@time: 2019-02-09 15:10
@desc:  基于百度ocr所做的验证码识别
'''
from aip import AipOcr
from PIL import Image

# 定义常量
APP_ID = '15537967'
API_KEY = 'WfwAe7nwLBiLRiEThmQcrsG4'
SECRET_KEY = 'G3kHHD2QhvsfVk3jtLmvlR7O5qASXp5l'

# 初始化AipFace对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
filePath = "D:/image.jpg"


def get_file_content(filePath):
    im = Image.open('D:/image.jpg')  # 1.打开图片
    # im.show()
    with open(filePath, 'rb') as fp:
        return fp.read()


def getVcode():
    # 定义参数变量
    options = {
        'detect_direction': 'true',
        'language_type': 'CHN_ENG',
    }

    # 调用通用文字识别接口
    result = aipOcr.basicGeneral(get_file_content(filePath), options)
    print(result)
    if (result["words_result"][0]['words'] != None):
        keyWord = result["words_result"][0]['words'].replace(' ', '')
    # print(keyWord)
    return keyWord


if __name__ == '__main__':
    code = getVcode()
    print(code)
