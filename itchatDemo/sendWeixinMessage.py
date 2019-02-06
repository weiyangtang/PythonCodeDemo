# encoding: utf-8
'''
@author: weiyang_tang
@contact: weiyang_tang@126.com
@file: sendWeixinMessage.py
@time: 2019-02-05 16:38
@desc: 获取好友备注或者昵称后，写入excel，在excel后一列的消息，写入所要发送的消息
'''

import threading
import itchat
import xlwt
import xlrd
import time


def TimerSender(time):
    timer = threading.Timer(time, send)
    timer.start()


def send():
    # itchat.auto_login(hotReload=True)
    ExcelFile = xlrd.open_workbook('excelFile.xls')
    print(ExcelFile.sheet_names())
    sheet = ExcelFile.sheet_by_index(0)
    print(sheet.name, sheet.nrows, sheet.ncols)
    for i in range(0, sheet.nrows - 1):
        if len(sheet.cell(i, 1).value) > 0:
            sender = itchat.search_friends(sheet.cell(i, 0).value)[0]['UserName']
            message = sheet.cell(i, 1).value
            itchat.send(message, toUserName=sender)
            itchat.send(message, toUserName='filehelper')
            print(sheet.cell(i, 0).value + "\t" + sheet.cell(i, 1).value + " 已经发送了")


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    TimerSender(10)
