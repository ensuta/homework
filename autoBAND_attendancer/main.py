import threading
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

logintime = input('로그인 시간 설정 (초) : ')
bwr = webdriver.Firefox()
bwr.get('https://auth.band.us/email_login?keep_login=false')
time.sleep(logintime)

loop = 0
while loop > 0:
    bwr.get('https://band.us/band/81335499/tag/태그1')
    bwr.implicitly_wait(5)
    bwr.find_element_by_xpath('/html/body/div[1]/div[1]/main/section/div[4]/div/div[1]/div/div[2]/div[2]/div/div[5]').click()
    bwr.implicitly_wait(3)
    bwr.find_element_by_xpath('/html/body/div[1]/div[1]/main/div/section/div/div/div[4]/div[4]/div[2]/div/div[2]/ul/li/div/label').click()
    time.sleep(60*60)

