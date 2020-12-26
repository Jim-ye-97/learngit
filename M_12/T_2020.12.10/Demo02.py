#Cookies
import http.cookiejar,urllib.request

# cookie=http.cookiejar.CookieJar()
# handle=urllib.request.HTTPCookieProcessor(cookie)
# opener=urllib.request.build_opener(handle)
# response=opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name+"="+item.value)

filename= 'cookies.txt'
cookie=http.cookiejar.MozillaCookieJar(filename)
handle=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handle)
response=opener.open('https://www.liepin.com/zhaopin/?sfrom=click-pc_homepage-centre_searchbox-search_new&d_sfrom=search_fp&key=python')
#cookie.save(ignore_discard=True,ignore_expires=True)
print(response.read().decode('utf-8'))

