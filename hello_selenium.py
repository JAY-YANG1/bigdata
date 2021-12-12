# selenium 으로 스크레핑 하기
# 웹브라우저를 이용한 작업들을
# 자동화할 수 있도록 특수제작된 브라우저

# seleniumhq.org
# sites.google.com/a/chromium.org/chromedriver
# => https://sites.google.com/chromium.org/driver (2021-07-28)

# ChromeDriver 92.0.4515.43
# chromedriver_win32.zip => chromedriver.exe
# C:\Program Files (x86)\Google\Chrome\Application

# MacOSX : /usr/local/bin 에 복사해두거나
# brew install chromedriver 명령으로 자동설치
# 위치 확인 : which chromedriver

# 빅서 이상 :
# cd    /usr/local/bin
# xattr -d com.apple.quarantine chromedriver  (터미널 실행)

# pip install selenium => selenium-3.141.0 (2019-04-17)
# pip install beautifulsoup4

# requests, bs4로 스크래핑할 수 없는
# 동적 데이터를 포함하는 웹 페이지를
# 원격 조작이 가능한 웹브라우저를 이용해서 처리

from selenium import webdriver
from bs4 import BeautifulSoup

# 스크래핑할 url 지정
# url = 'https://www.hanbit.co.kr/store/store_submain.html'
url = 'https://movie.daum.net/main'

# webdriver 실행
chrome = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

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

# 영화 제목 추출
print(html.select('strong.tit_item a')[0].text)

# 영화 평점 추출
print(html.select('span.txt_append span.txt_num')[0].text)

# 영화 예매율 추출
print(html.select('span.txt_append span.txt_num')[1].text)
