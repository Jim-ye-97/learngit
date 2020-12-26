import requests

headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac 05 X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/52.0.2743.116 Safari/537.36'
}
r=requests.get('https://www.zhihu.com/explore',headers=headers)
# print(r.text)

data={'name':'germey','age':'22'}
r=requests.post('http://httpbin.org/post',data=data)
# print(r.text)

r=requests.get('http://www.jianshu.com')
exit() if not r.status_code == requests.codes.ok else print("Requests Successfully")