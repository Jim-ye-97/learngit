from lxml import etree
test1 = '''
<ul>
<li class="item-0"><a href="link1. html">first item</a><li>
<li class="item-1"><a href="link2.html"> second item</a><li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html'>fourth item</a><li>
<li class="item-0"><a href='link5.html'> fifth item</a>
</ul>
</div>
'''
# #保存test.html数据
# with open('test.html') as file_obj:
#     content = file_obj.read()
#     #print(content)
# html = etree.HTML(content)
#html = etree.parse(content,etree.HTMLParser())
# result= etree.tostring(html)
# 获取网页汇总所有节点
# result = html.xpath('//li')
# print(type(result))
# print(result[0])
# #获取li下的子节点
# result = html.xpath('//li/a')
# print(result)
# #查找父节点
# html1 = etree.parse('test.html',etree.HTMLParser())
# result = html1.xpath('//a[@href="link4.html"]/parent::*/@class')
# print(result)
# #属性匹配
# result = html.xpath('//li[@class="item-0"]')
# print(result)
# #获取item-0下面的内容
# html = etree.parse('test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]//text()')
# print("取内容",result)
# html_text =open('test.html')
# html_text =html_text.read()
# print(html_text)
html = etree.parse('test.html' , etree.HTMLParser())

result1 = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print("寻找父节点", result1)

result2 = html.xpath('//li[@class="item-1"]')
print("属性匹配", result2)

result3 = html.xpath('//li[@class="item-1"]/a/text()')
print("文本获取",result3)

result4 = html.xpath('//li/a/@href')
print("属性获取",result4)

result5 = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print("多属性匹配",result5)

