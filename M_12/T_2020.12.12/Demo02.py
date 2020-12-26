import requests
import  re

headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac 05 X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/52.0.2743.116 Safari/537.36'
}
r=requests.get('https://www.zhihu.com/explore',headers=headers)
# print(r.text)
pattern=re.compile('ExploreSpecialCard-contentTitle.*?answer.*?>(.*?)</a>',re.S)#正则表达式
titles=re.findall(pattern,r.text)
print(titles)