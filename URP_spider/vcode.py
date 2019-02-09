# encoding: utf-8
'''
@author: weiyang_tang
@contact: weiyang_tang@126.com
@file: vcode.py
@time: 2019-02-08 15:22
@desc:
'''

from PIL import Image
from pytesseract import *
# 'O':'0',                           #替换列表
#     'I':'1','L':'1',
#     'Z':'2',
#     'S':'8'
rep={
    }

def initTable(threshold=140):           # 二值化函数
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table
#--------------------------------------------------------------------------------------
def getVcode():
    im = Image.open('D:/image.jpg')     # 1.打开图片
    im.show()
    im = im.convert('L')                                        # 2.将彩色图像转化为灰度图
    binaryImage = im.point(initTable(), '1')                    # 3.降噪，图片二值化
    # binaryImage.show()

    text = image_to_string(binaryImage, config='-psm 7')

    # 4.对于识别结果，常进行一些替换操作
    # for r in rep:
    #     text = text.replace(r,rep[r])
    print(text)
    # 5.返回识别结果
    return text

if __name__ == '__main__':
    getVcode()