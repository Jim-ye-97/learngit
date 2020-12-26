# -*- coding: utf-8 -*-
import xlwt
import json


# 创建excel工作表
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet1')

# 设置表头
worksheet.write(0, 0, label='NAME')
worksheet.write(0, 1, label='LEN')


# 读取json文件
# FILE_OBJECT= open('good.json','r', encoding='UTF-8')
with open('good.json', 'r',encoding='UTF-8') as f:
 data = json.load(f)

# 将json字典写入excel
# 变量用来循环时控制写入单元格，感觉有更好的表达方式
val1 = 1
val2 = 1

for list_item in data:
 for key, value in list_item.items():
  if key == "NAME":
   worksheet.write(val1, 0, value)
   val1 += 1
  elif key == "LEN":
   worksheet.write(val2, 1, value)
   val2 += 1
  else:
   pass

# 保存
workbook.save('OK1.xls')

