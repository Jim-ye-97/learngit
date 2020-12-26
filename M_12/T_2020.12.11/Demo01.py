from urllib.parse import  urlparse
from urllib.parse import urlencode
from urllib.parse import quote
from urllib.parse import unquote
result =urlparse('www.baidu.com/index.html;user?id=5#comment',scheme='https')
# print(result)

params={
    'name' : 'germey',
    'age' : '22'
}
base_url='http://www.baidu.com?'
url=base_url+urlencode(params)
# print(url)

keyword='壁纸'
url='https://www.baidu.com/s?wd=' +quote(keyword)
# print(url)

url='https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))

