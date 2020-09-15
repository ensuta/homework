from selenium import webdriver
import time

logintime = input('로그인 시간 설정 (초) : ')
bwr = webdriver.Firefox()
bwr.get('https://auth.band.us/login?next_url=https%3A%2F%2Fband.us%2Fband%2F79345807')
bwr.find_element_by_xpath('//*[@id="email_login_a"]').click()
bwr.implicitly_wait(1)
bwr.get('https://auth.band.us/email_login?keep_login=false')
time.sleep(logintime)

loop = 1 
while loop > 0: 
    bwr.get('https://band.us/band/81335499/tag/태그1')
    bwr.implicitly_wait(5)
    bwr.find_element_by_xpath('/html/body/div[1]/div[1]/main/section/div[4]/div/div[1]/div/div[2]/div[2]/div/div[5]').click()
    bwr.implicitly_wait(3)
    bwr.find_element_by_xpath('/html/body/div[1]/div[1]/main/div/section/div/div/div[4]/div[4]/div[2]/div/div[2]/ul/li/div/label').click()
    time.sleep(10)

