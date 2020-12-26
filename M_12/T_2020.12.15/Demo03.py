import re

content1='2016-12-15 12:00'
content2='54aK54ur5oiR54ix5L2g'
pattern=re.compile('\d{2}:\d{2}')
result=re.sub(pattern,'',content1)
content2=re.sub('\d+','',content2)#将匹配到的数据用' '替代
print(content2)
print(result)