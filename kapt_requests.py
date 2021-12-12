import requests
import json
import time

url1 = 'https://www.k-apt.go.kr/cmmn/bjd/getBjdList.do?bjd_gbn=SIDO'
url2 = 'https://www.k-apt.go.kr/kaptinfo/getKaptList.do?bjd_code=11680103&search_date=202107'
url3 = 'https://www.k-apt.go.kr/kaptinfo/getKaptSetday.do?kapt_code='

#
res = requests.get(url1)
print(res.text)

#
res = requests.get(url2)
print(res.text)

# requests 로 읽어들인 아파트 정보에서 코드, 이름 추출
kapt = json.loads(res.text)
print(kapt)

for apt in kapt['resultList']:
    print(apt['KAPT_NAME'], apt['KAPT_CODE'])

#
res = requests.get(url3 + 'A10026350')
print(res.text)


# url2 + url3 조합해서 주차장 정보 추출
res = requests.get(url2)
kapt = json.loads(res.text)

for apt in kapt['resultList']:
    print(apt['KAPT_NAME'], apt['KAPT_CODE'])

    url = url3 + apt['KAPT_CODE']
    res = requests.get(url)
    time.sleep(3)

    aptinfo = json.loads(res.text)

    parking = aptinfo['kaptInfo']
    print(parking['KAPTD_PCNT'],
          parking['KAPTD_PCNTU'])

    time.sleep(2)
