# python으로 Hive 서버에 접속해서
# HiveQL를 이용해서 데이터 추출하고
# pandas의 데이터프레임으로 저장함

# 파이썬과 HIVE 연동 방법
# 1. pyhive 패키지 이용 (번거로움)
# 2. jdbc를 이용한 hive 연동 (편한대신 속도저하)


# pyhive 필수 패키지 (sasl, bitarray) 설치 - 윈도우만!
# => sasl 모듈 설치시 에러 발생
# -> C++ 빌드도구로 컴파일 설치 필요!

# https://www.lfd.uci.edu/~gohlke/pythonlibs/#sasl
# 윈도우 환경에서 컴파일이 필요한 파이썬 패키지를
# 미리 빌드해서 배포하는 사이트

# pip install https://download.lfd.uci.edu/pythonlibs/y2rycu7g/sasl-0.2.1-cp37-cp37m-win_amd64.whl
# pip install https://download.lfd.uci.edu/pythonlibs/y2rycu7g/bitarray-2.2.5-cp37-cp37m-win_amd64.whl


# 맥은 그냥 여기서 부터 진행!
# pip install thrift
# pip install thrift-sasl
# pip install PyHive

# hive 계정으로 hive-site.xml 에 다음 내용 추가
# jps 명령으로 RunJar 의 PID 를 알아내서 kill 함
# cd $HIVE_HOME
# vi conf/hive-site.xml
# :set nu
# 4190 라인 찾음

# vi 에서 검색 기능 사용하기 : /검색어
# => 사용예 : /hive.server2.authentication

# <property>
# <name>hive.server2.authentication</name>
# <value>NOSASL</value>
# </property>

# hive server 재시작
# hive --service hiveserver2 &
# import thrift
# from pyhive import hive
#
# sql = 'select * from emp'
# conn = hive.Connection(host='192.168.121.132', username='hive',
#                        database='bigdata', auth='NOSASL')
# # auth='NOSASL' 로 설정하면 dbeaver에서는 접속 불가!
#
# cursor = conn.cursor()
# cursor.execute(sql)
# result = cursor.fetchall()
#
# conn.close()
#
# print(result)

# 정상적으로 파이썬 코드는 실행되지만,
# dbeaver나 putty의 beeline 콘솔은 제대로 접속되지 않음
# => beeline jdbc:hive2://192.168.56.103:10000;auth=noSasl
# 원인 : 추가적인 SASL 설정이 필요함

# dbeaver에서는 edit connection -> driver properties
# => User Properties에 name=auth, value=noSasl 을 생성함

# putty에서는 먼저, beeline 명령만 입력함
# 그 다음 아래 명령을 입력함
# !connect jdbc:hive2://접속주소:포트/db명;auth=noSasl 사용자명

# !connect jdbc:hive2://192.168.121.132:10000/bigdata;auth=noSasl hive


# 4190 라인의 NOSASL 을 다시 NONE 으로 바꾸고 hive-server2 재시작
# <property>
# <name>hive.server2.authentication</name>
# <value>NONE</value>
# </property>

# jdbc + hive 필수 패키지 (hive-jdbc-xxxx.jar)
# https://repo.hortonworks.com/content/repositories/releases/org/apache/hive/hive-jdbc/
# => hive-jdbc-2.3.8-standalone.jar
# https://github.com/timveil/hive-jdbc-uber-jar/releases/tag/v1.9-2.6.5
# => hive-jdbc-uber-2.6.5.0-292.jar

import jaydebeapi as jhive
#
# sql = 'select * from emp'
# conn = jhive.connect(jclassname="org.apache.hive.jdbc.HiveDriver",
#                      url='jdbc:hive2://192.168.121.132:10000/bigdata',
#                      jars='/Users/yjm/Desktop/Java/hive-jdbc-2.3.8-standalone.jar')
#                      #jars='/Users/yjm/Desktop/Java/hive-jdbc-uber-2.6.5.0-292.jar')
#
# cursor = conn.cursor()
# cursor.execute(sql)
# result = cursor.fetchall()
#
# conn.close()
#
# print(result)

# 실행시 아래 내용의 오류 발생시 => JAVA_HOME 환경변수 확인
# JAVA_HOME environment variable properly


# hive에서 넘어온 결과를 데이터프레임으로 만들기

import pandas as pd

sql = 'select * from emp'
conn = jhive.connect(jclassname="org.apache.hive.jdbc.HiveDriver",
                     url='jdbc:hive2://192.168.121.132:10000/bigdata',
                     jars='/Users/yjm/Desktop/Java/hive-jdbc-2.3.8-standalone.jar')

# HiveQl 을 실행하고 결과를 emp 라는 데이터프레임으로 생성
emp = pd.read_sql(sql, conn)

conn.close()

print(emp.head(5))

