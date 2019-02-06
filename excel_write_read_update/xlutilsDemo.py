# encoding: utf-8
'''
@author: weiyang_tang
@contact: weiyang_tang@126.com
@file: xlutilsDemo.py
@time: 2019-02-04 23:21
@desc: 对已有的excel文件进行修改
'''

import xlrd
from xlutils.copy import copy

# 打开想要更改的excel文件
old_excel = xlrd.open_workbook('data/weixinFridendList.xls', formatting_info=True)
# 将操作文件对象拷贝，变成可写的workbook对象
new_excel = copy(old_excel)
# 获得第一个sheet的对象
ws = new_excel.get_sheet(0)
# 写入数据
ws.write(0, 0, '第一行，第一列')
ws.write(0, 1, '第一行，第二列')
ws.write(0, 2, '第一行，第三列')
ws.write(1, 0, '第二行，第一列')
ws.write(1, 1, '第二行，第二列')
ws.write(1, 2, '第二行，第三列')
new_excel.save('data/weixinFridendList.xls')
# 另存为excel文件，并将文件命名
new_excel.save('data/new_fileName.xls')
print("excel文件修改完毕")