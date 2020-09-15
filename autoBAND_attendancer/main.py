from selenium import webdriver
import time

logintime = 120
print('2분뒤에 자동출첵이 시작됨 로그인은 수동으로 하셈')
bwr = webdriver.Firefox()
bwr.get('https://auth.band.us/login?next_url=https%3A%2F%2Fband.us%2Fband%2F79345807')
bwr.find_element_by_xpath('//*[@id="email_login_a"]').click()
bwr.implicitly_wait(1)
bwr.get('https://auth.band.us/email_login?keep_login=false')
time.sleep(logintime)

loop = 1 
while loop > 0: 
    bwr.get('https://band.us/band/81335499/hashtag/%ED%83%9C%EA%B7%B81') # 밴드 주소를 따와주세요 
    bwr.implicitly_wait(5)
    
    # 춠석체크 항목으로 이동 
    '''(문제 발생)'''
    bwr.find_element_by_xpath('/html/body/div[1]/div[1]/main/section/div[4]/div/div[1]/div/div[2]/div[2]/div/div[5]/div').click()
    bwr.implicitly_wait(3)
    
    # 출석체크 체크 버튼 누름
    bwr.find_element_by_xpath('/html/body/div[1]/div[1]/main/div/section/div/div/div[4]/div[4]/div[2]/div/div[2]/ul/li/div/label').click()
    time.sleep(10)


# /html/body/div[1]/div[1]/main/section/div[4]/div/div[1]/div/div[2]/div[2]/div/div[5] 
# /html/body/div[1]/div[1]/main/section/div[4]/div/div[1]/div/div[2]/div[2]/div/div[5]/div
# Tab 28번시 맨위의 출석체크 항목으로 이동

