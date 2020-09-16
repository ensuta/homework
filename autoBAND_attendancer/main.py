from selenium import webdriver
import time
import os

jugi = 60
logintime = 110
bwr = webdriver.Firefox()
bandurl = 'https://band.us/band/81335499/hashtag/%ED%83%9C%EA%B7%B81'
checkentr = '/html/body/div[1]/div[1]/main/section/div[4]/div/div[1]/div/div[2]/div[2]/div/div[5]/div/div/p[2]'
# /html/body/div[1]/div[1]/main/section/div[4]/div/div[1]/div/div[2]/div[2]/div/div[5]/div/div/p[2] 실제 밴드 주소
checkbtn = '/html/body/div[1]/div[2]/div/div/section/div[2]/div/section/div/div[4]/div[3]/div[2]/div/div[2]/ul/li/div/label'
# /html/body/div[1]/div[1]/main/section/div[4]/div/div[1]/div/div[2]/div[2]/div/div[5] 실제 밴드 주소

'''
def loadpage(self):
    bwr.get(bandurl)
    time.sleep(jugi)
    fwrite
    listener
'''

print('2분뒤에 자동출첵이 시작, 로그인 수동')
bwr.get('https://auth.band.us/login?next_url=https%3A%2F%2Fband.us%2Fband%2F79345807')
time.sleep(logintime)
bwr.get(bandurl)
time.sleep(10)
checkfind = bwr.find_element_by_xpath(checkentr)
checkentrtxt = checkfind.text
fwrite = open('temp.txt', 'w')
fwrite.write(checkentrtxt)
fwrite.close()
bwr.get(bandurl)
time.sleep(jugi)
fwrite
listener

def listener(self):
    if checkentrtxt != fwrite.readline: 
        checking()
        bwr.refresh()
        time.sleep(10)
        checkfind()
        fwrite.write(checkentrtxt)
        fwrite.close()
        bwr.get(bandurl)
        time.sleep(jugi)
        fwrite
        listener
    else:
        bwr.get(bandurl)
        time.sleep(jugi)
        fwrite
        listener

def checking(self):
        # 출석체크 항목으로 이동 (해결됨)
    bwr.find_element_by_xpath(checkentr).click()
    time.sleep(3)
        # 출석체크 체크 버튼 누름
    bwr.find_element_by_xpath(checkbtn).click()
    time.sleep(1)
    bwr.get(bandurl)
    time.sleep(jugi)
    fwrite
    listener
