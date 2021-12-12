# 아파트 단지 정보에서 주차장 정보 추출
# k-apt.go.kr
# => 메인페이지 팝업창 닫기 => '단지정보' 클릭
# => 2021.06, 서울, 강남구, 삼성동, 아이파크삼성동 클릭

from selenium import webdriver

import sys
import time

url = 'http://www.k-apt.go.kr/'

chrome = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

chrome.get(url)

# 페이지 내용이 브라우져에 모두 로딩되기를 기다림
chrome.implicitly_wait(2)

# cpu가 아무런 작업을 하지 않고 그냥 시간을 보내게 함
time.sleep(2)

# 팝업창 닫기 1
# chrome.find_element_by_css_selector(
#     '#popup_20210518 > div.layerPopupTitle > div > a').click()
# time.sleep(1)
#
# chrome.find_element_by_css_selector(
#     '#popup_20200720_02 > div.layerPopupTitle > div > a').click()
# time.sleep(1)

# 팝업창 닫기 2
# execute_script : 자바스크립트 명령을 실행할 수 있음
# chrome.execute_script('closeLyserPopup("popup_20210518")')
# time.sleep(1)
# chrome.execute_script('closeLyserPopup("popup_20200720_02")')
# time.sleep(1)

# 팝업창 닫기 2b
pops = chrome.find_elements_by_css_selector('div.layerPopup')
for pop in pops:
    id = pop.get_attribute('id')        # 지정한 요소의 ID 속성값을 알아냄
    js = f'closeLyserPopup("{id}")'
    chrome.execute_script(js)
    time.sleep(1)


# 단지 정보 클릭
chrome.find_element_by_css_selector('#lnbMenu > li:nth-child(2) > a').click()
time.sleep(2)


# 검색할 단지 정보 클릭
chrome.find_element_by_xpath('//*[@title="년도 선택"]/option[text()="2021"]').click()
time.sleep(1)

chrome.find_element_by_xpath('//*[@title="월 선택"]/option[text()="07"]').click()
time.sleep(1)

chrome.find_element_by_xpath('//*[@title="광역시도 선택"]/option[text()="서울특별시"]').click()
time.sleep(1)

chrome.find_element_by_xpath('//*[@title="시군구 선택"]/option[text()="강남구"]').click()
time.sleep(1)

chrome.find_element_by_xpath('//*[@title="읍면동 선택"]/option[text()="삼성동"]').click()
time.sleep(1)

chrome.find_element_by_xpath('//*[@title="아이파크삼성동"]').click()
time.sleep(1)

# 관리시설 정보
chrome.find_element_by_xpath('//*[@alt="관리시설정보"]').click()
time.sleep(1)

# 단지 상세정보에서 주차대수 추출
parking = chrome.find_element_by_xpath('//*[@id="parking_cnt"]').text
print('주차대수 :', parking)
time.sleep(2)

chrome.close()

