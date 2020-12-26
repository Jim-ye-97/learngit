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
url = 'https://www.amazon.com/s?k=flexispot'
response = requests.get(url,cookies=cookie,headers=kv)
print(response.text)