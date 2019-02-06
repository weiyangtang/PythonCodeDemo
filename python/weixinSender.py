# -*- coding: utf-8 -*-
# @Time    : 2018/9/25 11:06
# @Author  : Tangweeiyang
# @File    : weixinSender.py
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QFont
import sys
import datetime
import time
import itchat
import threading
from tkinter import messagebox

class FriendsList(QThread):
    sinOut = pyqtSignal(str)
    # 自定义信号，执行run()函数时，从相关线程发射此信号

    def __init__(self):
        super().__init__()

    def run(self):

        itchat.auto_login(hotReload=True)
        friendList = itchat.get_friends()
        for each in friendList:
            if len(each['RemarkName']) < 2: #如果 备注名为空,则用微信昵称
                self.sinOut.emit(each['NickName'])
            else:
                self.sinOut.emit(each['RemarkName'])

class sendMessage(QThread):

    def __init__(self,message,name,time):
        super().__init__()
        self.message=message
        self.name=name
        self.time=time

    def run(self):
        timer = threading.Timer(self.time,self.send)
        timer.start()

    def send(self):

        itchat.auto_login(hotReload=True)
        sender = itchat.search_friends(self.name)[0]['UserName']
        itchat.send(self.message, toUserName=sender)
        itchat.send(self.message, toUserName='filehelper')
        messagebox.showinfo('消息','发送成功')


class weixinSender(QListWidget):

    def __init__(self):
        super().__init__()
        self.Ui()
        # self.dataProduce()

    def Ui(self):
        self.year_label = QLabel('年')
        self.year=QLineEdit()
        self.month_label=QLabel('月')
        self.month=QLineEdit()
        self.day_label=QLabel('日')
        self.day=QLineEdit()
        self.friendList_lable=QLabel('好友')
        self.friendList=QComboBox()

        self.hour_label = QLabel('时')
        self.hour = QLineEdit()
        self.min_label = QLabel('分')
        self.min = QLineEdit()
        self.second_label = QLabel('秒')
        self.second = QLineEdit()

        self.text=QTextEdit() #文本域
        self.listbt = QPushButton('获取好友列表')
        self.OKbt=QPushButton('定期发送')


        grid = QGridLayout()
        grid.setSpacing(10)  # 创建标签之间的空间

        grid.addWidget(self.year_label,1,1)
        grid.addWidget(self.year,1,0)
        grid.addWidget(self.month_label,1,3)
        grid.addWidget(self.month,1,2)
        grid.addWidget(self.day_label,1,5)
        grid.addWidget(self.day,1,4)
        grid.addWidget(self.friendList_lable,1,6,2,1)
        grid.addWidget(self.friendList,1,7,2,3)

        grid.addWidget(self.hour_label,2,1)
        grid.addWidget(self.hour,2,0)
        grid.addWidget(self.min_label,2,3)
        grid.addWidget(self.min,2,2)
        grid.addWidget(self.second_label,2,5)
        grid.addWidget(self.second,2,4)

        grid.addWidget(self.text,3,0,4,10)
        grid.addWidget(self.listbt,7,5,1,2)
        grid.addWidget(self.OKbt,7,7,1,2)

        self.setLayout(grid)

        self.friendList.addItem('好友1')
        self.friendList.addItem('好友2')

        self.text.setFont(QFont("楷体",12,QFont.Normal))

        self.OKbt.clicked.connect(self.send)
        self.listbt.clicked.connect(self.dataProduce)
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('定时发送消息')
        self.setWindowIcon(QIcon('weixinIcon.jpg'))
        self.show()

    def dataProduce(self):
        now=time.localtime()
        self.year.setText(str(now.tm_year))
        self.month.setText(str(now.tm_mon))
        self.day.setText(str(now.tm_mday))
        self.hour.setText(str(now.tm_hour))
        self.min.setText(str(now.tm_min))
        self.second.setText(str(now.tm_sec))

        self.friendList.clear()
        self.thread=FriendsList()
        self.thread.sinOut.connect(self.slotAdd)
        self.thread.start()

    def slotAdd(self,name):
        self.friendList.addItem(name)

    def send(self):
        self.target = datetime.datetime(int(self.year.text()),int(self.month.text()),int(self.day.text()),int(self.hour.text()),int(self.min.text()),int(self.second.text()))
        self.now = time.time()
        self.delay_time = self.target.timestamp() - self.now
        self.sendThread=sendMessage(self.text.toPlainText(),self.friendList.currentText(),self.delay_time)
        self.sendThread.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = weixinSender()
    sys.exit(app.exec_())
