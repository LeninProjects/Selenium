from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="E:\python_projects\SeleniumTests\chromedriver.exe")

driver.get("https://www.mvideo.ru/")
cookies = driver.get_cookies()
print(cookies)
cookie = driver.get_cookie('MVID_CITY_ID')
print(cookie)
driver.add_cookie({'name': 'MVID_CITY_ID',
                   'value': 'CityCZ_15570',
                   'domain': '.www.mvideo.ru',
                   'expiry': 3756294034,
                   'httpOnly': True,
                   'path': '/',
                   'secure': False,
                   })
driver.refresh()
#
cookie_after = driver.get_cookie('MVID_CITY_ID')
print(cookie_after)
