# 공동주택관리 정보시스템
# 2018.08, 서울 강남구, 삼성동 소재 모든 아파트
# 아파트 명칭, 법정동 주소
# 아파트 주차대수 (지상, 지하)등을 추출

# 단, 실제 URL에 질의문자열을 포함시켜 정보 추출

# 1. openkaptinfo.do : 요청 폼 데이터 없음

# 2. getBjdList.do : 요청 폼데이터 포함(지역)
#    ?bjd_gbn=SIDO
#    ?bjd_code=11&bjd_code=SGG
#    ?bjd_code=11680&bjd_gbn=EMD

# 3. getKaptList.do : 요청 폼 데이터 포함 (지역 내 모든 아파트)
# ?bjd_code=11680103&search_date=202107

# 4. getKaptSetday.do : 요청 폼 데이터 포함 (선택한 아파트)
#    ?kapt_code=A10026350
#    주차장 대수 :
#    kaptSetDayList > kaptInfo > KAPTD_PCNTU > "1247"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import sys
import time

# 단지검색 키워드
year = '2021'
month = '07'
sido = '서울특별시'
gugun = '강남구'
dong = '삼성동'

url1 = 'http://www.k-apt.go.kr/kaptinfo/openkaptinfo.do'
url2 = 'https://www.k-apt.go.kr/cmmn/bjd/getBjdList.do?bjd_gbn=SIDO'
url3 = 'https://www.k-apt.go.kr/kaptinfo/getKaptList.do?bjd_code=11680103&search_date=202107'

# 셀레니엄 실행
options = Options()
options.add_argument('--headless')
chrome = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)

chrome.get(url1)
chrome.implicitly_wait(2)

# 검색할 단지 정보 입력 2
yy = Select(chrome.find_element_by_class_name('combo_YYYY'))
yy.select_by_visible_text(year)
time.sleep(1)

mm = Select(chrome.find_element_by_class_name('combo_MM'))
mm.select_by_visible_text(month)
time.sleep(1)

sd = Select(chrome.find_element_by_class_name('combo_SIDO'))
sd.select_by_visible_text(sido)
time.sleep(1)

sgg = Select(chrome.find_element_by_class_name('combo_SGG'))
sgg.select_by_visible_text(gugun)
time.sleep(1)

emd = Select(chrome.find_element_by_class_name('combo_EMD'))
emd.select_by_visible_text(dong)
time.sleep(1)


# 선택한 시, 구, 동에 대한 코드값 출력
# txt_bjdCode 요소가 숨겨져 있기 때문에 요소값을 추출할 수 없음
# display="block" 으로 화면에 표시
bjd = chrome.find_element_by_class_name('txt_bjdCode')
chrome.execute_script('arguments[0].style.display="block"', bjd)
bjdcode = chrome.find_element_by_class_name('txt_bjdCode').text
print(bjdcode)

# 지역 bjd_code 알아보기 - 한글깨짐
chrome.get(url2)
print(chrome.page_source)
time.sleep(2)

# 선택주소 내 apt_code 알아보기 - 한글꺠짐
chrome.get(url3)
print(chrome.page_source)
time.sleep(2)

chrome.close()
