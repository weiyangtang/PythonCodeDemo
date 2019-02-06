# encoding: utf-8
'''
@author: weiyang_tang
@contact: weiyang_tang@126.com
@file: autoSendWeixin_Linux.py
@time: 2019-02-04 22:05
@desc: 定时给微信好友发送消息，在Linux运行
'''

import itchat
import xlwt
import xlrd
from xlutils.copy import copy


def getFriends():
    itchat.auto_login(hotReload=True)
    # itchat.run()
    friendList = itchat.get_friends()
    i = 0
    for each in friendList:
        if len(each['RemarkName']) < 2:  # 如果 备注名为空,则用微信昵称
            print(i)
            print(each['NickName'])
            execlWrite(i, 0, each['NickName'])
        else:
            print(i)
            print(each['RemarkName'])
            execlWrite(i, 0, each['RemarkName'])
        i = i + 1


def sendMessage(name, message):
    itchat.auto_login(hotReload=True)
    sender = itchat.search_friends(name)[0]['UserName']
    itchat.send(message, toUserName=sender)
    itchat.send(message, toUserName='filehelper')


def execlWrite(row, col, content):
    old_excel = xlrd.open_workbook('excelFile.xls', formatting_info=True)
    # 将操作文件对象拷贝，变成可写的workbook对象
    new_excel = copy(old_excel)
    # 获得第一个sheet的对象
    ws = new_excel.get_sheet(0)
    # 写入数据
    ws.write(row, col, content)
    new_excel.save('excelFile.xls')
    # 另存为excel文件，并将文件命名
    # new_excel.save('new_fileName.xls')


def excelRead():
    # 文件位置

    ExcelFile = xlrd.open_workbook('excelFile.xls')

    print(ExcelFile.sheet_names())

    sheet = ExcelFile.sheet_by_index(0)

    # sheet = ExcelFile.sheet_by_name('Sheet1')

    # 打印sheet的名称，行数，列数

    print(sheet.name, sheet.nrows, sheet.ncols)
    for i in range(0, sheet.nrows - 1):
        if len(sheet.cell(i, 1).value) > 0:
            print(sheet.cell(i, 0).value + "\t" + sheet.cell(i, 1).value + " 已经发送了")
        # else:
        #     print(sheet.cell(i, 0).value+"is null")
        # print(sheet.cell(i, 1).value)
        # print(sheet.cell(i, 0).value)
        # name = sheet.cell(i, 0).value
        # message = sheet.cell(i, 1).value
        # sendMessage(name, message)
    # print(sheet.cell_value(1, 0))
    # print(sheet.row(1)[0].value)


if __name__ == '__main__':

    # friendList.excelRead()
    getFriends()
    # excelRead()
