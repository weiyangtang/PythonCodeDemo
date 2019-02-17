# encoding: utf-8
'''
@author: weiyang_tang
@contact: weiyang_tang@126.com
@file: ThreadDemo.py
@time: 2019-02-14 21:45
@desc: 多线程学习Demo
'''
# !/usr/bin/python3

import _thread
import time


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))


if __name__ == '__main__':

    # 创建两个线程
    try:
        _thread.start_new_thread(print_time, ("Thread-1", 2,))
        _thread.start_new_thread(print_time, ("Thread-2", 4,))
    except:
        print("Error: 无法启动线程")

    while 1:
        pass
