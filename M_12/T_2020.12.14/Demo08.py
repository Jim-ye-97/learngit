from requests import Request,Session

url='http://httpbin.org/post'
data={
    'name':'germey'
}
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}
s=Session()
req=Request('POST',url,data=data,headers=headers) #将url,data,headers添加到request中
prepped=s.prepare_request(req) #构造prepared_request对象
r=s.send(prepped)
print(r.text)