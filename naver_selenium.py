# 네이버에 무인으로 로그인 하기

from selenium import webdriver

import sys
import time
import pyperclip

# url = 'https://naver.com'
#
# chrome = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
#
# chrome.get(url)
#
# # 페이지 내용이 브라우져에 모두 로딩되기를 기다림
# chrome.implicitly_wait(2)
#
# # cpu가 아무런 작업을 하지 않고 그냥 시간을 보내게 함
# time.sleep(2)
#
# # 로그인 버튼을 찾아서 selenium이 클릭하게 함
# loginbtn = chrome.find_element_by_class_name('link_login')
# mouse = webdriver.ActionChains(chrome)
# mouse.move_to_element(loginbtn).click().perform()
#
# time.sleep(2)
#
# # 로그인 정보 정의
# userid = 'abc123'
# passwd = '987xyz'
#
# # 로그인 페이지의 id,pwd 입력창, 로그인버튼 찾음
# uid = chrome.find_element_by_id('id')
# pwd = chrome.find_element_by_id('pw')
# loginbtn = chrome.find_element_by_class_name('btn_global')
#
# # id, pwd 입력창에 값 입력
# uid.send_keys(userid)
# time.sleep(2)
# pwd.send_keys(passwd)
# time.sleep(2)
#
# # 로그인 버튼 클릭
# mouse = webdriver.ActionChains(chrome)
# mouse.move_to_element(loginbtn).click().perform()
#
# time.sleep(3)
#
# chrome.close()


# 다음 사이트 자동 로그인 하기
url = 'https://logins.daum.net/accounts/signinform.do'

chrome = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

chrome.get(url)

# 페이지 내용이 브라우져에 모두 로딩되기를 기다림
chrome.implicitly_wait(2)

# cpu가 아무런 작업을 하지 않고 그냥 시간을 보내게 함
time.sleep(2)

# 로그인 정보 정의
userid = 'abc123'
passwd = '987xyz'

# 로그인 페이지의 id,pwd 입력창, 로그인버튼 찾음
uid = chrome.find_element_by_id('id')
pwd = chrome.find_element_by_id('inputPwd')
loginbtn = chrome.find_element_by_id('loginBtn')

# id, pwd 입력창에 값 입력
uid.send_keys(userid)
time.sleep(2)
pwd.send_keys(passwd)
time.sleep(2)

# 로그인 버튼 클릭
mouse = webdriver.ActionChains(chrome)
mouse.move_to_element(loginbtn).click().perform()

time.sleep(3)

chrome.close()
