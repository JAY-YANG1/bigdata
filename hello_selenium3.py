# jtbc 뉴스홈 속보 사이트에서
# 헤드라인, 뉴스요약, 기자명, 송고시간 등을 추출함

# 미션1 : 지정한 날짜 모든 뉴스 페이지의 내용 추출 (url, 반복문)
# 미션2 : 날짜별로 검색해서 추출가능하도록 프로그래밍 (url, 재조정)

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

url = 'https://news.jtbc.joins.com/section/list.aspx'
url = 'https://news.jtbc.joins.com/section/list.aspx?pgi=2'

executables = '/usr/local/bin/chromedriver'

# headless 를 위한 설정
options = Options()
options.add_argument('--headless')

# webdriver 실행
chrome = webdriver.Chrome(executable_path=executables, options=options)

# 지정한 url 로 접속
chrome.get(url)

# 응답으로 받은 웹페이지 소스를 변수에 저장
res = chrome.page_source

# 작업종료를 위해 브라우져 닫음
chrome.close()

# 응답으로 받은 웹페이지 소스를 출력
# print(res)

# 읽어들인 웹페이지 소스를 BeautifulSoup 으로 피싱
html = BeautifulSoup(res, 'lxml')

newshds = []
newsdescs = []
writers = []
nwsdates = []

# 뉴스 헤드라인 추출
for newshd in html.select('dt.title_cr'):
    newshds.append(newshd.text.strip())

print(newshds)

# 뉴스 요약 추출
for newsdesc in html.select('dd.desc a'):
    newsdescs.append(newsdesc.text.strip())

print(newsdescs)

# 뉴스 기자 추출
for writer in html.select('dd.info span.writer'):
    writers.append(writer.text.strip())

print(writers)

# 뉴스 송고시간 추출
for nwsdate in html.select('dd.info span.date'):
    nwsdates.append(nwsdate.text.strip())

print(nwsdates)

# 추출 갯수 확인
print(len(newshds), len(newsdescs), len(writers), len(nwsdates))

# 미션 1 : 맨 마지막 페이지 알아내기
pages = html.select('.num')
print(len(pages))

print(pages[-1].text)

# 반복문을 이용해서 나머지 기사도 추출
nums = int(pages[-1].text)

baseurl = 'https://news.jtbc.joins.com/section/list.aspx?pgi='
for i in range(1, nums+1):
    url = baseurl + str(i)
    print(url)
    # 헤드라인, 요약, 기자명, 송고시간을 추출하는 코드 작성

# 미션2 : 날짜별로 검색해서 추출가능하도록 프로그래밍
pdate = input('크롤링할 날짜는?')
pgi = input('크롤링할 뉴스의 페이지 번호는?')
baseurl = 'https://news.jtbc.joins.com/section/list.aspx'
params = '?pdate=' + pdate + '&pgi=' + pgi
url = baseurl + params

print(url)
