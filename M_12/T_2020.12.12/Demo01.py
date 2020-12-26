import requests
r=requests.get('https://www.liepin.com/')
print(type(r)) #Response类型
print(r.status_code) #状态码
print(type(r.text)) #响应体类型
# print(r.text)  #内容
print(r.cookies)  #cookies

r=requests.post('https://www.liepin.com/')
print(type(r.text))
r=requests.get('http://httpbin.org/get')
print(r.text)

data={
    'name':'germey',
    'age': 22
}
r=requests.get('http://httpbin.org/get',params=data)
print(r.text)

r=requests.get('http://httpbin.org/get')
print(type(r.text))
print(r.json())
print(type(r.json()))

