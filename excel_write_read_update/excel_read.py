# encoding: utf-8
'''
@author: weiyang_tang
@contact: weiyang_tang@126.com
@file: excel_read.py
@time: 2019-02-06 23:06
@desc: excel文件单元格读取
'''

import xlrd

from datetime import date,datetime

def read_excel():

    #文件位置

    ExcelFile=xlrd.open_workbook('data/weixinFridendList.xls')

    #获取目标EXCEL文件sheet名

    print(ExcelFile.sheet_names())

    #------------------------------------

    #若有多个sheet，则需要指定读取目标sheet例如读取sheet2

    #sheet2_name=ExcelFile.sheet_names()[1]

    #获取sheet内容【1.根据sheet索引2.根据sheet名称】

    sheet=ExcelFile.sheet_by_index(0)

    # sheet=ExcelFile.sheet_by_name('Sheet1')

    #打印sheet的名称，行数，列数

    print(sheet.name,sheet.nrows,sheet.ncols)

    #获取整行或者整列的值

    rows=sheet.row_values(1)#第三行内容

    cols=sheet.col_values(1)#第二列内容

    print(cols,rows)

    #获取单元格内容

    print(sheet.cell(1,0).value)
    print(sheet.cell_value(1,0))
    print(sheet.row(1)[0].value)


if __name__ =='__main__':
    read_excel()