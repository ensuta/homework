from tkinter import *
import tkinter.ttk as ttk

import pyautogui
import pyperclip
import keyboard

root = Tk ()
root.title("검색도우미(search_helper)")
root.geometry('300x100')
root.resizable(False, False)

#검색엔진
#검색어
txt = Label(root, text = "검색_사이트")
txt2 = Label(root, text = "검색어")

txt.place(x = 1, y = 1)
txt2.place(x = 15, y = 25)

#콤보박스(검색엔진 설정)
values = ['구글', '네이버', '네이버 뉴스', '네이버 지식in', '다음', '야후', '나무위키', '위키백과']
combobox = ttk.Combobox(root, height = 10, values = values, state = 'readonly')
combobox.set("사이트를 고르세요")

combobox.place(x = 85, y = 1)

#검색어 입력
txt3 = Text(root, width = 20, height = 1.3 )


txt3.place(x = 85, y = 25)


def cmd():
    from selenium import webdriver

    #webdriver 위치 지정
    driver = webdriver.Chrome('C:\webdriver\chromedriver.exe')

    searcher1 = combobox.get()
    searcher2 = txt3.get("1.0", END)
    
    if str(searcher1) == '구글':
        driver.get('https://www.google.co.kr/')
        pyperclip.copy(str(searcher2))

        driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').click()

        pyautogui.hotkey("ctrl", "v")

        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        
    elif str(searcher1) == '네이버':
        driver.get('https://www.naver.com/')
        pyperclip.copy(str(searcher2))

        driver.find_element_by_xpath('//*[@id="query"]').click()

        pyautogui.hotkey("ctrl", "v")

        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')


    elif str(searcher1) == '네이버 뉴스':
        driver.get('https://news.naver.com/')
        pyperclip.copy(str(searcher2))

        driver.find_element_by_xpath('//*[@id="lnb.searchForm"]/fieldset/input[1]').click()

        pyautogui.hotkey("ctrl", "v")

        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')


    elif str(searcher1) == '네이버 지식in':
        driver.get('https://kin.naver.com/')
        pyperclip.copy(str(searcher2))

        driver.find_element_by_xpath('//*[@id="nx_query"]').click()

        pyautogui.hotkey("ctrl", "v")

        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')


    elif str(searcher1) == '다음':
        driver.get('https://www.daum.net/')
        pyperclip.copy(str(searcher2))

        driver.find_element_by_xpath('//*[@id="q"]').click()

        pyautogui.hotkey("ctrl", "v")

        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')


    elif str(searcher1) == '나무위키':
        driver.get('https://namu.wiki/w/%EB%82%98%EB%AC%B4%EC%9C%84%ED%82%A4:%EB%8C%80%EB%AC%B8')
        pyperclip.copy(str(searcher2))

        driver.find_element_by_xpath('//*[@id="tchikaf0605cf3"]/input').click()

        pyautogui.hotkey("ctrl", "v")

        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')


    elif str(searcher1) == '위키백과':
        driver.get('https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC')
        pyperclip.copy(str(searcher2))

        driver.find_element_by_xpath('//*[@id="searchInput"]').click()
        
        pyautogui.hotkey("ctrl", "v")

        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

  
#버튼
btn = Button(root, text = "검색", command = cmd)

btn.place(x = 120, y = 51)


root.mainloop()
