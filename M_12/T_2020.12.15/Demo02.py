import requests
from bs4 import BeautifulSoup
import re
kv = {"user-agent": "Mozilla/5.0"}
cookie = {
"cisession":"19dfd70a27ec0eecf1fe3fc2e48b7f91c7c83c60",
"CNZZDATA100020196":"1815846425-1478580135-https%253A%252F%252Fwww.baidu.com%252F%7C1483922031",
"Hm_lvt_f805f7762a9a237a0deac37015e9f6d9":"1482722012,1483926313",
"Hm_lpvt_f805f7762a9a237a0deac37015e9f6d9":"1483926368"
}
url = 'https://www.amazon.cn/dp/B07MKK9D4H/ref=sr_1_1?dchild=1&keywords=flexispot&qid=1607996432&sr=8-1'
response = requests.get(url,cookies=cookie,headers=kv)
#response.encoding = response.apparent_encoding
#pattern=re.compile('a-size-base-plus a-color-base a-text-normal(.*?)</span>',re.S)
#titles=re.findall(pattern,r.text)
#print(titles)
print(response.text)
soup = BeautifulSoup(response.text, 'lxml')


