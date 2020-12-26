from urllib import request,error
try:
    response =request.urlopen('https://www.baidu.com/index.hm')
except error.URLError as e:
    print(e.reason)