# encoding: utf-8
'''
@author: weiyang_tang
@contact: weiyang_tang@126.com
@file: ListDemo.py
@time: 2019-02-17 15:55
@desc: 创建二维数组
'''
nums = []
rows = eval(input("请输入行数："))
columns = eval(input("请输入列数："))

for row in range(rows):
    nums.append([])
    for column in range(columns):
        num = eval(input("请输入数字："))
        nums[row].append(num)
print(nums)
