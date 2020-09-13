import threading
import pyperclip
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

bwr = webdriver.Firefox()
bwr.get('https://auth.band.us/email_login?keep_login=false')
time.sleep(1)

# id, pw 입력할 곳을 찾습니다.

# id 입력
emailtag = bwr.find_element_by_name('email')
emailtag.clear()
time.sleep(1)
emailtag.click()
emailkey = 'ensuta08130813@gmail.com' #input('이메일 : ')
pyperclip.copy(emailkey)
emailtag.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 확인 클릭
ok_btn = bwr.find_element_by_xpath('/html/body/div/section/form/button')
ok_btn.click()

# pw 입력
pwdtag = bwr.find_element_by_name('password')
pwdtag.clear()
time.sleep(1)
pwdkey = 'Ensuta_0813!' #input('비번 : ')
pwdtag.click()
pyperclip.copy(pwdkey)
pwdtag.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 로그인 클릭
login_btn = bwr.find_element_by_xpath('/html/body/div/section/form/button')
login_btn.click()
print('2분안에 캡챠를 캐고 로그인해주세요 2분 후에 자동출석이 됩니다')
time.sleep(120)

#def gyosi():
    # timer=threading.Timer(3900,gyosi)
bwr.get('https://band.us/band/81335499/post/2')
bwr.implicitly_wait(10)

bwr.find_element_by_xpath('/html/body/div[1]/div[1]/main/div/section/div/div/div[4]/div[4]/div[2]/div/div[2]/ul/li/div/label').click()

#pass
