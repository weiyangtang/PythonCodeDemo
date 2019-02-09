# encoding: utf-8
'''
@author: weiyang_tang
@contact: weiyang_tang@126.com
@file: excel_write.py
@time: 2019-02-06 22:58
@desc: excel表格的写入保存
'''

import xlwt

def write_excel():
    # 2. 创建Excel工作薄
    myWorkbook = xlwt.Workbook()
    # 3. 添加Excel工作表
    mySheet = myWorkbook.add_sheet('A Test Sheet')
    # 4. 写入数据
    myStyle = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')  # 数据格式
    #mySheet.write(i, j, 1234.56, myStyle)
    mySheet.write(2, 0, 1)  # 写入A3，数值等于1
    mySheet.write(2, 1, 1)  # 写入B3，数值等于1
    mySheet.write(2, 2, xlwt.Formula("A3+B3"))  # 写入C3，数值等于2（A3+B3）
    # 5. 保存
    myWorkbook.save('data/demo.xls')


if __name__ == '__main__':
    # 写入Excel
    write_excel();
    print('写入成功')