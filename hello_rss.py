# 기상청 날씨 데이터 수집하기
# www.kma.go.kr
# 기상청 날씨누리 -> 특보.예보 -> 동네예보
# 기상청 날씨누리 -> 생활과산업
#        -> 서비스 -> 인터넷 -> RSS

# RSS : rich site summary
# 사이트를 구독subscribe한 사용자에게 업데이트된
# 컨덴츠를 간편하게 배포하고자 만든 데이터 형식

# RSS 구독 프로그램을 이용하면
# 사이트를 방문하지 않고도 해당 사이트의
# 컨텐츠를 이용할 수 있다는 장점 존재

from urllib.request import urlopen
from html import unescape
import csv


# ssl certificate 오류 해결법
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# 파이썬에서 xml문서를 처리하기 위한 모듈 (lxml)
from xml.etree import ElementTree

# 날씨 정보를 받아올 url 지정
url = 'https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109'

# 지정한 url로 rss 컨텐츠 받아오기
f = urlopen(url)
text = f.read().decode('utf-8')
print(text)

# xml parser를 이용해서 파일을 읽어오고
# 메모리에 xml 계층구조를 만들기 위해
# ElementTree 객체 생성

# 먼저 날씨정보를 파일에 저장
with open('weather.xml', 'w', encoding='utf-8') as f:
    f.write(text)

# 파일의 내용을 읽어들여 계층구조로 생성
tree = ElementTree.parse('weather.xml')

# getroot 메서드로 XML 상위요소를 추출
root = tree.getroot()

# findall 메서드로 추출할 데이터가 있는
# 요소element를 지정함
for w in root.findall('channel/item/description/body/location/data'):
    tmef = w.find('tmEf').text     # 시간
    wf = w.find('wf').text     # 날씨정보
    tmn = w.find('tmn').text     # 최저기온
    tmx = w.find('tmx').text     # 최고기온
    print(tmef, wf, tmn, tmx)

# findall 메서드로 추출할 데이터가 있는
# 요소element를 지정함 (지역 선택)
for loc in root.findall('channel/item/description/body/location'):
    if loc.find('city').text == '서울':
        print('지역명:', loc.find('city').text)
        for w in loc.findall('data'):
            tmef = w.find('tmEf').text  # 시간
            wf = w.find('wf').text  # 날씨정보
            tmn = w.find('tmn').text  # 최저기온
            tmx = w.find('tmx').text  # 최고기온
            print(tmef, wf, tmn, tmx)


