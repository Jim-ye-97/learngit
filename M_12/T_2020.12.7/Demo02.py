#timeout参数
import urllib.request
import socket
import  urllib.error

try:
    response=urllib.request.urlopen('https://www.baidu.com',timeout=0.01)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')