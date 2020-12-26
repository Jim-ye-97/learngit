import urllib.request

data = bytes(urllib.parse.urlencode({'word': 'hello'}),encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post',data=data)
print(response.read().decode('utf-8'))
# print(type(response))
# print(response.status)响应状态码
# print(response.getheaders())#响应头部信息
# print(response.getheader('Server'))#获取头部信息中的server值
# print(response.getheader('Connection'))
