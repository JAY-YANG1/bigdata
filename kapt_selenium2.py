# 공동주택관리 정보시스템
# 2018.08, 서울, 강남구, 삼성동 소재 모든 아파트
# 아파트 명칭, 법정동 주소
# 아파트 주차대수 (지상, 지하)등을 추출

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import sys
import time

url = 'http://www.k-apt.go.kr/kaptinfo/openkaptinfo.do'

# 단지검색 키워드
year = '2021'
month = '07'
sido = '서울특별시'
gugun = '강남구'
dong = '삼성동'

# 셀레니엄 실행
options = Options()
options.add_argument('--headless')
chrome = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)

chrome.get(url)
chrome.implicitly_wait(2)
time.sleep(2)


# 단지검색 정보 설정
chrome.find_element_by_xpath(f'//*[@title="년도 선택"]/option[text()="{year}"]').click()
time.sleep(1)

chrome.find_element_by_xpath(f'//*[@title="월 선택"]/option[text()="{month}"]').click()
time.sleep(1)

chrome.find_element_by_xpath(f'//*[@title="광역시도 선택"]/option[text()="{sido}"]').click()
time.sleep(1)

chrome.find_element_by_xpath(f'//*[@title="시군구 선택"]/option[text()="{gugun}"]').click()
time.sleep(1)

chrome.find_element_by_xpath(f'//*[@title="읍면동 선택"]/option[text()="{dong}"]').click()
time.sleep(1)

# 동내 모든 아파트에 대한
# 법정동 주소 출력하기
# cnt = len(chrome.find_elements_by_xpath('//tr[@id]'))     # 15
# cnt = len(chrome.find_elements_by_xpath('//tr[@role="row"]'))   # 16

# 맨 마지막 tr의 id 값을 조사해서 cnt 변수에 대입
cnt = chrome.find_element_by_css_selector('table[id="aptInfoList"] tr:last-child').get_attribute('id')
cnt = int(cnt)

# 아파트 명칭 확인
for i in range(1, cnt + 1):
    apt = chrome.find_element_by_xpath(f'//tr[@id="{i}"]/td[2]').text
    print(apt)

# 자동으로 아파트 명칭, 주소, 주차대수 추출
for i in range(1, cnt + 1):
    chrome.find_element_by_xpath(f'//tr[@id="{i}"]').click()
    time.sleep(1)

    # 아파트 명칭, 법정동 주소 추출
    # 기본정보 클릭
    chrome.find_element_by_xpath('//img[@alt="기본정보"]').click()
    time.sleep(1)
    aptname = chrome.find_element_by_xpath('//td[@id="kapt_name"]').text   # 아파트명칭
    aptaddr = chrome.find_element_by_xpath('//td[@id="kab_addr"]').text    # 아파트 주소
    print(aptname, aptaddr)

    # 아파트 주차대수 (지상, 지하)등을 추출
    chrome.find_element_by_xpath('//img[@alt="관리시설정보"]').click()
    time.sleep(1)
    parking = chrome.find_element_by_xpath('//td[@id="parking_cnt"]').text
    print(parking)

    # 단지검색 버튼 클릭
    chrome.find_element_by_xpath('//img[@alt="단지검색"]').click()
    time.sleep(2)

chrome.close()
