import re

ret = re.match(r'\d{5}', '12345678901')
print(ret.group())

ret = re.match(r'\w{4,20}@(163)\.com', 'aaaa@163.com')
print(ret.group(1))

ret = re.findall(r"\d+", "python = 19999, c = 7890, c++ = 12345")
print(ret)  # ['9999', '7890', '12345']