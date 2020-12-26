html = """
<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
 <body>
  <p class="title" name="dromouse">
   <b>
    The Dormouse's story
   </b>
  </p>
  <p class="story">
   Once upon a time there were three little sisters;and their names were
   <a class="sister" href="http://example.com/elsie" id="link1">
   </a>
   <span>
    Elsie
   </span>
   <a class="sister" href="http://example.com/lacie" id="link2">
    Lacie
   </a>
   <a href="http://example.com/tillie class=" id="link3" sister="">
    Tillie
   </a>
   and they lived at the bottom of a well.
  </p>
  <p class="story">
   ...
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
#print(soup.prettify())
# print(soup.p.string)
# print(soup.p.contents)
print(soup.p.children)
for i,child in enumerate(soup.p.children):
    print(i,child)