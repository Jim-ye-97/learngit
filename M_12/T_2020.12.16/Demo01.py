import requests
import openpyxl
import json

url = 'http://hkf10.eastmoney.com/F9HKStock/GetFinanceAssetData.do?securityCode=01810.HK&comType=127000000606281483&yearList=2018,2017,2016,2015&reportTypeList=1,5,3,6&dateSearchType=1&listedType=0,1&reportTypeInScope=1&reportType=0&rotate=0&seperate=0&order=desc&cashType=1&exchangeValue=1&customSelect=0&CurrencySelect=0'
res = requests.get(url);  # 爬取数据  //返回了json数据
res.encoding = "utf-8"
print(res.text)
jst = json.loads(res.text)
key = jst['resultList']


def ExcelWrite(result):
    mywb = openpyxl.Workbook()
    sheet = mywb.active;  # 获取初始的sheet
    row = 0;  # 单元格的行
    for i in result:
        col = 64;  # 单元格的列 从 'A' 开始
        row += 1;
        for j in i:
            col += 1;
            sheet[chr(col) + str(row)] = i[j];
    mywb.save('负债资产.xls');


ExcelWrite(key);