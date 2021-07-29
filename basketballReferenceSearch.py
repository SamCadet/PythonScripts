#! python3

# basketballReferenceSearch.py - Automate searching for player on basketball-reference.com

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyinputplus as pyip
import pyautogui

browser = webdriver.Chrome("C:\\Users\\Sam\\Downloads\\chromedriver.exe")
# linkElem = browser.find_element_by_tag_name('/players/')


timeout = time.time() + 20 * 1      # 20 seconds

while True:
    openPage = browser.get('https://www.basketball-reference.com/')
    searchElem = browser.find_element_by_name('search')
    searchElem.click()
    # startTime = time.time()
    # endTime = time.time()
    try:
        user = searchElem.send_keys(
            pyip.inputStr('Enter player/team name and press ENTER: ', timeout=20))
    except pyip.TimeoutException:
        print('Search and program aborted.')
        break
    # if endTime > timeout:
    #     print('Search and program aborted.')
    #     break
    else:
        searchElem.send_keys(Keys.ENTER)
        # linkElem.click()
        print(pyip.inputYesNo('Do you want to conduct another search?: '))
        if pyip.inputYesNo() == 'yes':
            newTab = pyautogui.hotkey('ctrl', 't')
            continue
        if pyip.inputYesNo() == 'no':
            print('All done, have a good day yoooo!!!')
            break
