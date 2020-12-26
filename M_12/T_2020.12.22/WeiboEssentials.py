# https://s.weibo.com/top/summary/
import requests
from bs4 import BeautifulSoup
import datetime

if __name__ == "__main__":
    news = []
    # 新建数组存放热搜榜
    #url='https://s.weibo.com/top/summary/summary?cate=realtimehot' 微博热搜榜
    #url='https://s.weibo.com/top/summary/summary?cate=socialevent' 微博要文榜
    hot_url = 'https://s.weibo.com/top/summary/summary?cate=socialevent'
    # 热搜榜链接
    r = requests.get(hot_url)
    # 向链接发送get请求获得页面
    print(r.text)
    soup = BeautifulSoup(r.text, 'lxml')
    # 解析页面

    urls_titles = soup.select('#pl_top_realtimehot > table > tbody > tr > td.td-02 > a')
    hotness = soup.select('#pl_top_realtimehot > table > tbody > tr > td.td-02 > span')

    for i in range(len(urls_titles)):
        Ess_news = {}
        # 将信息保存到字典中
        Ess_news['title'] = urls_titles[i].get_text()
        # get_text()获得a标签的文本
        Ess_news['url'] = "https://s.weibo.com"+urls_titles[i]['href']
        # 获得热度文本
        news.append(Ess_news)
        # 字典追加到数组中

    print(news)
    print(len(news))



    today = datetime.date.today()
    f = open('./要文榜-%s.csv'%(today), 'w', encoding='utf-8')
    for i in news:
        f.write("标题:"+i['title'] + ',\n' "链接:"+ i['url']+'\n\n' )