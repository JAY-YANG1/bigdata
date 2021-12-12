# 한계레, 파이낸스, JTBC 뉴스 RSS를 이용해서
# 전체기사의 제목과 뉴스요약, 송고시간을 추출함
# www.hani.co.kr
# www.fnnews.com
# news.jtbc.joins.com

from urllib.request import urlopen          # 코드가 복잡함
from xml.etree import ElementTree

from bs4 import BeautifulSoup               # 코드가 간단함
import requests

# ssl certificate 오류 해결법
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


url = 'https://fs.jtbc.joins.com/RSS/newsflash.xml'

# 지정한 url 로 rss 컨텐츠 읽어오기
f = urlopen(url)
text = f.read().decode('utf-8')
print(text)

# 뉴스데이터를 파일에 저장
with open('news.xml', 'w', encoding='utf-8') as f:
    f.write(text)

# 파일의 내용을 읽어들여 계층구조로 생성
tree = ElementTree.parse('news.xml')
root = tree.getroot()

# findall 메서드로 요소 추출
for n in root.findall('channel/item'):
    title = n.find('title').text
    desc = n.find('description').text
    pdate = n.find('pubDate').text
    print(title, desc, pdate)

print('================================')

# version2
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

res = requests.get(url, headers=headers)
res.encoding = 'utf-8'

# xml 문서를 parsing 하기 위해 lxml-xml 를 지정
# rss = BeautifulSoup(res.text, 'lxml-xml')
rss = BeautifulSoup(res.content, 'lxml-xml')    # mac 사용자는 요렇게!

for news in rss.find_all('item'):
    titles = news.title.text
    desc = news.description.text
    pdate = news.pubDate.text
    print(titles, desc, pdate)
