import requests

headers={
    'Cookie':'mjclient=PC; youpindistinct_id=175ab8bd9c2-0017497e803747-1f0e; Hm_lvt_025702dcecee57b18ed6fb366754c1b8=1605784089,1607341434,1607916478; youpin_sessionid=1765fee117d-041e06e9f16a4a-1f0e; Hm_lpvt_025702dcecee57b18ed6fb366754c1b8=1607927207',#
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}

r=requests.get('https://www.xiaomiyoupin.com',headers=headers)
print(r.text)