from selenium import webdriver
import time
import os

bwr = webdriver.Firefox()

logintime = 110
jugi = 60
delay = 2
bandurl = 'https://band.us/band/81335499/hashtag/%ED%83%9C%EA%B7%B81'
checkentr = '/html/body/div[1]/div[1]/main/section/div[4]/div/div[1]/div/div[2]/div[2]/div/div[5]'
# /html/body/div[1]/div[1]/main/section/div[4]/div/div[1]/div/div[2]/div[2]/div/div[5] 출첵 항목
checkboxtxt = '/html/body/div[1]/div[1]/main/section/div[4]/div/div[1]/div/div[2]/div[2]/div/div[5]/div/div/p[2]'
# /html/body/div[1]/div[1]/main/section/div[4]/div/div[1]/div/div[2]/div[2]/div/div[5]/div/div/p[2] 출첵 제목
checkbtn = '/html/body/div[1]/div[2]/div/div/section/div[2]/div/section/div/div[4]/div[3]/div[2]/div/div[2]/ul/li/div/label'

# 수동으로 로그인
print('2분뒤에 자동출첵이 시작, 로그인 수동')
bwr.get('https://auth.band.us/login?next_url=https%3A%2F%2Fband.us%2Fband%2F79345807')
time.sleep(logintime)

#사이트로 이동 (최초)
bwr.get(bandurl)
time.sleep(delay)

i = 1
while i > 0:
    # 출첵항목의 제목 불러오고 임시저장
    xpath = bwr.find_element_by_xpath(checkboxtxt)
    chcktxt = xpath.text
    print(chcktxt)
    f = open('temp.txt', 'w')

    if chcktxt != f.readline:

        # 출석체크 항목으로 이동 (해결됨)
        bwr.find_element_by_xpath(checkentr).click()
        time.sleep(delay)
        # 출석체크 체크 버튼 누름
        bwr.find_element_by_xpath(checkbtn).click()
        time.sleep(delay)
        # 다시 불러오기
        bwr.get(bandurl)
        time.sleep(delay)
        # 기록된 값 바꾸기
        bwr.find_element_by_xpath(checkboxtxt)
        chcktxt=chcktxt
        f.write(chcktxt)
        f.close()
        # 새로고침
        bwr.get(bandurl)
        time.sleep(jugi)
        bwr.get(bandurl)
        time.sleep(delay)
    else:
        # 새로고침
        time.sleep(jugi)
        bwr.get(bandurl)
        time.sleep(delay)