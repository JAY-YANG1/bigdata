import requests
from bs4 import BeautifulSoup

url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'
params = '?serviceKey=E4JWejlHvBa9gK7FqghIphJIU8GM7VWZYmTiTcOARddkLkHq8ceQHgmaGHahu35csz9AyPJ9B1zdYyg4uecs4w%3D%3D' \
         + '&pageNo=1&numOfRows=10&startCreateDt=20200310&endCreateDt=20210811'

res = requests.get(url + params)
res.encoding = 'utf-8'
rss = BeautifulSoup(res.content, 'lxml-xml')

hdr = 'accDefRate,accExamCnt,accExamCompCnt,careCnt,clearCnt,createDt,deathCnt,decideCnt,' \
      'examCnt,resutlNegCnt,seq,stateDt,stateTime,updateDt\n'

data = ''

for covid in rss.find_all('item'):
    data += covid.accDefRate.text.strip() + ','
    data += covid.accExamCnt.text.strip() + ','
    data += covid.accExamCompCnt.text.strip() + ','
    data += covid.careCnt.text.strip() + ','
    data += covid.clearCnt.text.strip() + ','
    data += covid.createDt.text.strip() + ','
    data += covid.deathCnt.text.strip() + ','
    data += covid.decideCnt.text.strip() + ','
    data += covid.examCnt.text.strip() + ','
    data += covid.resutlNegCnt.text.strip() + ','
    data += covid.seq.text.strip() + ','
    data += covid.stateDt.text.strip() + ','
    data += covid.stateTime.text.strip() + ','
    data += covid.updateDt.text.strip() + '\n'

print(hdr)
print(data)

with open('covid19.csv', 'w', encoding='utf-8') as f:
    f.write(hdr)
    f.write(data)

