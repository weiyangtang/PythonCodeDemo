# encoding: utf-8
'''
@author: weiyang_tang
@contact: weiyang_tang@126.com
@file: dateTime_Str.py
@time: 2019-02-05 21:35
@desc:datetime和字符串互转
'''

import datetime
import time

sendTime='2019-2-6 12:33:0'
times=datetime.datetime.strptime(sendTime,"%Y-%m-%d %H:%M:%S")
print(times)
print("2.把字符串转成datetime: ", datetime.datetime.strptime(sendTime, "%Y-%m-%d %H:%M:%S"))
now=datetime.datetime.now()
print(now)
sendTimeStamp = times.timestamp()
nowStamp=time.time()
delayTime=sendTimeStamp-nowStamp
print(delayTime)


