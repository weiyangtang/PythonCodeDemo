# encoding: utf-8
'''
@author: weiyang_tang
@contact: weiyang_tang@126.com
@file: datetime_timeStamp_str.py
@time: 2019-02-06 11:44
@desc: 时间日期、时间戳、字符串互转、日期差
'''

import time
import datetime
#获取当前日期
now_dateTime=datetime.datetime.now() #获取当前日期 格式：2019-02-06 11:47:36.406318
print("获取当前日期:",now_dateTime)

#将datetime类型转成str类型
#strftime("%Y-%m-%d %H:%M:%S") datetime->str
now_str=now_dateTime.strftime("%Y-%m-%d %H:%M:%S")
print("将datetime类型->str类型",now_str)

#str->dateTime 字符串转成日期datetime
#strptime(str,format)
oneDay_str="2019-2-6 12:1:0"
oneDay_datetime=datetime.datetime.strptime(oneDay_str,"%Y-%m-%d %H:%M:%S")
print("字符串转成日期datetime",oneDay_datetime)



# 获取当前时间时间戳
now_timestamp=time.time()
print("获取当前时间的时间戳",now_timestamp)

#字符串转成时间戳str->timestamp
oneDay_str="2019-2-6 12:1:0"
oneDay_timestamp=time.mktime(time.strptime(oneDay_str,"%Y-%m-%d %H:%M:%S"))
print("字符串转时间戳:",oneDay_timestamp)

#时间戳转成日期 timestamp->datetime
#now_dateTime=datetime.datetime.strptime()
now_dateTime=datetime.datetime.fromtimestamp(now_timestamp)
print("时间戳转成日期:",now_dateTime)


#两个日期差
oneDay_str="2019-2-6 20:30:0"
now_timestamp=time.time()
oneDay_timestamp=time.mktime(time.strptime(oneDay_str,"%Y-%m-%d %H:%M:%S"))
difTime=now_timestamp-oneDay_timestamp
print("时间间隔为:",difTime,"秒")



