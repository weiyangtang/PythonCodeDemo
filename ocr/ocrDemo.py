# encoding: utf-8
'''
@author: weiyang_tang
@contact: weiyang_tang@126.com
@file: ocrDemo.py
@time: 2019-02-08 22:00
@desc:
'''

from PIL import Image
import pytesseract
import cv2 as cv

img_path = 'D:/image.jpg'

# img_path='orgin.jpg'

# img_path='F:/fb/hpop.jpg'

# 依赖opencv
img = cv.imread(img_path)
text = pytesseract.image_to_string(Image.fromarray(img))

# 不依赖opencv写法
# text=pytesseract.image_to_string(Image.open(img_path))


print(text)

