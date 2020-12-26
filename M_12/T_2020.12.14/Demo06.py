import requests

try:
    r=requests.get("https://www.taobao.com",timeout=0.01)
    print(r.status_code)
except:
    print("报错啦")
