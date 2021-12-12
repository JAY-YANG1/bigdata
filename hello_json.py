# 파이썬으로 JSON 형식 다루기
# javascript object notation
# 자바스크립트에서 객체를 표현하는 방식을 이용해서
# 각종 프로그래밍 언어에서 데이터를 표현함
# 예전에는 csv, xml로 데이터를 표현했다면
# 지금은 json으로 거의 대부분 이용해서 표현

# json은 파이썬의 사전식dictionary 자료형과 비슷
# [ { 키 : 값 }, { ... } ]
# { 'userid': 'zzyzzy', 'passwd':'123456', 'age' : 15 }

# <data>
#     <userid>zzyzzy</userid>
#     <passwd>123456</passwd>
#     <age>15</age>
# </data>

# 파이썬에서 json을 다룰려면 json 내장객체 호출
import json

# JSON 파일을 생성하기 위한 사전형 객체 호출
from collections import OrderedDict

# json 객체를 만들려면 먼저, python의 dict 객체처럼 정의
member = {'userid': 'abc123', 'passwd': '987xyz', 'age': 28}
print(member)

# dumps 라는 함수를 이용해서
# 텍스트로 작성된 dict 객체를 json 객체로 변환
# 이렇게 변환된 객체는 메모리내에 생성됨
# jsobj = json.dumps(member)

# indent 속성을 이용하면 json 문자열을 보기좋게 들여쓰기 적용
jsobj = json.dumps(member, indent=2)
print(jsobj)

# 이름, 이메일, 전화번호를 person 이라는 json 객체로 생성
# ensure_ascii 속성을 False로 지정하면
# ASCII로의 강제 인코딩을 중지할 수 있음 - 한글깨짐 방지
person = {'name': '양재묵', 'email': 'abc123@987xyz.com', 'phone': '123-4567-8912'}
jsobj = json.dumps(person, indent=2, ensure_ascii=False)
print(jsobj)

# OrderedDict 객체를 이용해서 json 객체 정의 (추천!)
# 특정 속성이 여러개의 값으로 구성되는 경우 리스트로 정의
person2 = OrderedDict()
person2['name'] = '양재묵'
person2['email'] = 'abc123@987xyz.com'
person2['phone'] = '123-4567-8912'
# 특정 속성이 여러개의 값으로 구성되는 경우 리스트로 정의
person2['friends'] = ['지현', '혜교', '수지']

# 특정 속성이 여러개의 객체로 구성되는 경우 dict로 정의
schools = OrderedDict()
schools['중학교'] = '서울중학교'
schools['고등학교'] = '서울고'
schools['대학교'] = '서울대'

person2['schools'] = schools

print(person2)
person2b = json.dumps(person2, indent=2, ensure_ascii=False)
print(person2b)

# person2 객체를 JSON 파일로 저장
# 즉, 메모리에 생성된 json 객체를 파일에 저장하기 위해 사용
# dump(json객체, 파일객체, 옵션)
with open('person.json', 'w', encoding='utf-8') as j:
    json.dump(person2, j, ensure_ascii=False)


# json 파일로 저장된 객체를 읽어서 출력하기
# load(파일객체)
with open('person.json', 'r', encoding='utf-8') as j:
    person_data = json.load(j)

print(person_data)

