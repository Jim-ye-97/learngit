import requests
from bs4 import BeautifulSoup
import json
import xlsxwriter
import pandas as pd
import openpyxl
import  xlwt
kv = {"user-agent": "Mozilla/5.0"}
cookie = {
"cisession":"19dfd70a27ec0eecf1fe3fc2e48b7f91c7c83c60",
"CNZZDATA100020196":"1815846425-1478580135-https%253A%252F%252Fwww.baidu.com%252F%7C1483922031",
"Hm_lvt_f805f7762a9a237a0deac37015e9f6d9":"1482722012,1483926313",
"Hm_lpvt_f805f7762a9a237a0deac37015e9f6d9":"1483926368"
}
url = 'https://www.amazon.cn/s?k=flexispot'
response = requests.get(url,cookies=cookie,headers=kv)
print(response.status_code)
#print(response.text)
bs4_obj = BeautifulSoup(response.text, 'lxml')
good_alls=bs4_obj.find_all("div",attrs={"class":"a-section a-spacing-none a-spacing-top-small"})
#print(good_alls)
dict1=[]
dict2=[]
for good_all in good_alls:
    good_name = good_all.find("span",attrs={"class":"a-size-base-plus a-color-base a-text-normal"})
    # good_price = good_all.find("span",attrs={"class":"a-offscreen"})
    if good_name:
        good_price = good_all.find("span", attrs={"class": "a-offscreen"})
        print(good_name.text)
        # dict1.append(good_name.text)

for good_all in good_alls:
    #good_name = good_all.find("span",attrs={"a-size-base-plus a-color-base a-text-normal"})
    good_price = good_all.find("span",attrs={"a-offscreen"})
    try:
        print(good_price.text)
        dict2.append(good_price.text)
    except:
        print()
# good_detal=dict(zip(dict1,dict2))
# print(good_detal)
#print(type(good_detal))
#json_new=json.dumps(good_detal, ensure_ascii=False )
#print(json_new)

# #转成json文件
# with open('good1.json','w',encoding='utf-8') as file_obj:
#     json.dump(json_new,file_obj,ensure_ascii=False)
