import requests
from requests.exceptions import RequestException
import re
import json

from multiprocessing import Pool  #多线程

def get_one_page(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except RequestException: #弄一个错误的总类就好，子类太多这里不考虑
        return None

def parse_one_page(html):
    pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                       +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                       +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)  #这鬼东西要仔细
    items=re.findall(pattern,html)
    #print(items)
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3].strip()[3:],
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]
        }    #注意，字典是无序的，所以看到返回结果不要方

def write_to_file(content):
    with open('result.text','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()

def main(offset):
    url='http://maoyan.com/board/4?offset='+str(offset)
    get_one_page(url)
    html=get_one_page(url)
    #parse_one_page(html)
    #print(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__=='__main__':
    #main()
    for i in range(10):
        main(i*10)
    '''pool=Pool()
    pool.map(main,[i*10 for i in range(10)])        多线程'''