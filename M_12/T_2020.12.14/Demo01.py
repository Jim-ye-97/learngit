import requests
from bs4  import BeautifulSoup
headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac 05 X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/52.0.2743.116 Safari/537.36',
    #'Cookie':'mjclient=PC; youpindistinct_id=175ab8bd9c2-0017497e803747-1f0e; Hm_lvt_025702dcecee57b18ed6fb366754c1b8=1605784089,1607341434,1607916478; youpin_sessionid=1765fee117d-041e06e9f16a4a-1f0e; Hm_lpvt_025702dcecee57b18ed6fb366754c1b8=1607927207'
}

re=requests.get('https://www.amazon.cn/s?k=flexispot',headers=headers)
print(re.text)
