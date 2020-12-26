html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters;and their names were
<a href="http://example.com/elsie" class="sister" id="link1"></a>
<a href="http://example.com/elsie" class="sister" id="link2">Lacie</a>
<a href="http://example.com/elsie" class="sister" id="link3">Tillie</a>
and they lived at the bottom of a well.</p>
<p class="story">...</p> 
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
print("标题:",soup.title)
print("标题类型:",type(soup.title))
print("标题转成字符串:",soup.title.string)
print("头部:",soup.head)
print(soup.p)
print("p标签的属性",soup.p.attrs)
print("p-title标签的值",soup.p.attrs['class'])
print("p-class标签的属性的值",soup.p.attrs['name'])
print("p的值",soup.p.string)

print("关联选择", soup.p.contents)