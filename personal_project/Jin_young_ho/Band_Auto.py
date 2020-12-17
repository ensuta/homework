#GUI 생성
from tkinter import *
import tkinter.ttk as ttk

#자동으로 키입력
import pyautogui

#밴드 접속등의 역할을 함
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


import time
root = Tk ()
root.title("자동 출석")
root.geometry('300x220')
root.resizable(False, False)

#반
txt2 = Label(root, text = "반")

txt2.place(x = 15, y = 25)


txt3 = Text(root, width = 20, height = 1.3 )

txt3.place(x = 85, y = 25)

#아이디
txt4 = Label(root, text = "아이디")

txt4.place(x = 15, y = 55)


txt5 = Text(root, width = 20, height = 1.3 )

txt5.place(x = 85, y = 55)

#비번
txt6 = Label(root, text = "비밀번호")

txt6.place(x = 15, y = 85)


txt7 = Text(root, width = 20, height = 1.3 )

txt7.place(x = 85, y = 85)



def cmd1():
    #webdriver 위치지정
    driver = webdriver.Chrome('C:\webdriver\chromedriver.exe')

    #주소불러오기
    driver.get('https://band.us/band/79345807/hashtag/4%EB%B0%98')

    #창 최대로 키우기
    driver.maximize_window()

    #webdriver 제어
    action = ActionChains(driver)

    #'이메일로 로그인' 버튼 누르기 
    driver.find_element_by_xpath('//*[@id="email_login_a"]/span').click()

    #아이디 입력하기
    pyautogui.write(str(txt5))
    driver.find_element_by_xpath('//*[@id="email_login_form"]/button').click()

    #패스워드 입력하기
    pyautogui.write(str(txt7))
    driver.find_element_by_xpath('//*[@id="email_password_login_form"]/button').click()
    
    in_sec = 35
    sec = int(in_sec)
    print(sec)
    
    #sec가 0이 되면 반복을 멈춰라
    while (sec != 0 ):
        sec = sec-1
        time.sleep(1)
        print(sec)
    pyautogui.click(x = 951, y = 541)
    pyautogui.click(x = 1222, y = 538)
    driver.find_element_by_xpath('//*[@id="wrap"]/div[3]/div/div/section/button[4]').click()
    while 6:
        in_sec = 3900
        sec = int(in_sec)
        print(sec)
        #sec가 0이 되면 반복을 멈춰라
        while (sec != 0 ):
            sec = sec-1
            time.sleep(1)
            print(sec)
        pyautogui.press('f5')
        pyautogui.click(x = 951, y = 541)
        pyautogui.click(x = 1222, y = 538)
        driver.find_element_by_xpath('//*[@id="wrap"]/div[3]/div/div/section/button[4]').click()
        
    
  
#버튼
btn = Button(root, text = "자동 출석 체크 시작", command = cmd1)

btn.place(x = 80, y = 110)


root.mainloop()


#아직 미
