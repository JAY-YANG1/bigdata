# JTBC 뉴스의 속보에 대한 RSS을 추출해서
# json 형식으로 파일에 저장
# 대상 : 제목,링크,뉴스본문,배포일
# 파일명 : jtbc_rss_flash.json

import json
from collections import OrderedDict

from bs4 import BeautifulSoup
import requests

url = 'https://fs.jtbc.joins.com/RSS/newsflash.xml'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

res = requests.get(url, headers=headers)
res.encoding = 'utf-8'
rss = BeautifulSoup(res.content, 'lxml-xml')

newses = []

for news in rss.find_all('item'):
    newOne = OrderedDict()
    newOne['title'] = news.title.text.strip()
    newOne['link'] = news.link.text.strip()
    newOne['description'] = news.description.text.strip()
    newOne['pubDate'] = news.pubDate.text.strip()
    newses.append(newOne)


# 스크래핑한 도서목록을 json 형식으로 재구성
allnews = OrderedDict()
allnews['news'] = newses

# 생성한 json 객체를 파일에 저장함
with open('jtbc_rss_flash.json', 'w', encoding='utf8') as f:
    json.dump(allnews, f, ensure_ascii=False, indent=2)

