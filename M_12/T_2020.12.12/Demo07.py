import  requests

headers={
    'Cookie':'Lf_cookied56b699830e77ba53855679cb1d252da=4394c60bb56550c823c49ce7a9c0916c; PHPSESSID=dcmu1013a2lq9tlie6juvskp2r',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}
r=requests.get('http://erp.lfwellness.cn/',headers=headers)
print('打印Cookie')
print(r.cookies)
print('打印headers')
print(r.headers)
print('打印网页')
#print(r.text)
print('打印状态码')
print(r.status_code)