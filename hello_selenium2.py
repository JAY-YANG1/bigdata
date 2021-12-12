# selenium 으로 스크레핑하기
# headless 옵션으로 브라우져를 띄우지 않고 자동화 작업

# hanb.co.kr => store => 전체도서목록
# 브랜드, 도서명, 저자, 발행일, 가격 추출

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

url = 'https://www.hanbit.co.kr/store/books/full_book_list.html'
executables = '/usr/local/bin/chromedriver'

# headless 를 위한 설정
options = Options()
options.add_argument('--headless')

# webdriver 실행
chrome = webdriver.Chrome(executable_path=executables, options=options)

# 지정한 url 로 접속
chrome.get(url)

# 응답으로 받은 웹페이지 소스 출력
# print(chrome.page_source)

# 소스를 변수에 저장
res = chrome.page_source

# 작업종료를 위해 브라우져 닫음
chrome.close()

# 읽어들인 웹페이지 소스를 BeautifulSoup 으로 피싱
html = BeautifulSoup(res, 'lxml')

brands = []
titles = []
authors = []
regdates = []
prices = []

# 브랜드 추출 :
# #container > div.full_book_list_wrap > div.table_area > table > tbody > tr:nth-child(1) > td.brd_m
# //*[@id="container"]/div[2]/div[4]/table/tbody/tr[1]/td[1]
# for brand in html.select('td.brd_m'):
#     brands.append(brand.text.strip())   # 이름기반 요소 선택

for brand in html.select('td:nth-child(1)'):
    brands.append(brand.text.strip())       # 위치기반 요소 선택

# 도서명 추출 :
# #container > div.full_book_list_wrap > div.table_area > table > tbody > tr:nth-child(1) > td:nth-child(2) > a
# for title in html.select('td.left a'):
#     titles.append(title.text.strip())

for title in html.select('td:nth-child(2)'):
    titles.append(title.text.strip())

# 저자 추출
# for author in html.select('td.left'):
#     authors.append(author.text.strip())

for author in html.select('td:nth-child(3)'):
    authors.append(author.text.strip())

# 등록일 추출
for regdate in html.select('td:nth-child(4)'):
    regdates.append(regdate.text.strip())

# 가격 추출
# for price in html.select('td.right'):
#     price = price.text.replace('원', '')
#     price = price.replace(',', '')
#     prices.append(price)

for price in html.select('td:nth-child(5)'):
    price = price.text.replace('원', '')
    price = price.replace(',', '')
    prices.append(price)

# book.csv 에 저장
data = ''
for i in range(len(titles)):
    data += '"' + brands[i] + '",'
    data += '"' + titles[i] + '",'
    data += '"' + authors[i] + '",'
    data += '"' + regdates[i] + '",'
    data += '"' + prices[i] + '"\n'

with open('book.csv', 'w', encoding='UTF-8') as f:
    f.write(data)
