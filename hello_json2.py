# 한빛미디어 - store - 전체도서목록을
# json 형식(allbooks.json)으로 저장
# http://www.hanbit.co.kr/store/books/full_book_list.html
# brand, title, publish, pdate, price

import json
from collections import OrderedDict

import requests
from bs4 import BeautifulSoup

url = 'http://www.hanbit.co.kr/store/books/full_book_list.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

res = requests.get(url, headers=headers)
html = BeautifulSoup(res.text, 'lxml')

booklist =[]

# 추출해야 할 데이터 수(행수) 알아내기
bookcnt = len(html.select('table tbody tr'))
print('총 도서수', bookcnt)

# td 만을 대상으로 모두 추출해서 리스트에 저장
for book in html.select('table tbody tr td'):
    booklist.append(book.text.strip())

print(booklist)
# 스크래핑한 도서목록을 json 형식으로 재구성
allbooks = OrderedDict()
books = []

for i in range(0, bookcnt):
    book = OrderedDict()
    book['brand'] = booklist[i * 5]
    book['title'] = booklist[i * 5 + 1]
    book['author'] = booklist[i * 5 + 2]
    book['pdate'] = booklist[i * 5 + 3]
    book['price'] = booklist[i * 5 + 4]
    books.append(book)

allbooks['books'] = books

# 전체도서에 대한 키가 없음 (비추! - 코드의 시작이 중괄호가 아님)
# print(json.dumps(books, ensure_ascii=False, indent=2))

# 전체도서에 대한 키 존재 (추천! - 코드의 시작이 중괄호)
# 키 이름은 books 로 설정
print(json.dumps(allbooks, ensure_ascii=False, indent=2))

# 생성한 json 객체를 파일에 저장함
with open('allbooks.json', 'w', encoding='utf8') as f:
    json.dump(allbooks, f, ensure_ascii=False, indent=2)

