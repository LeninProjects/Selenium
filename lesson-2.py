from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="E:\python_projects\SeleniumTests\chromedriver.exe")

'''1) Поиск элемента на странице по id'''
# driver.get("https://www.mvideo.ru/")
# elem = driver.find_element(By.ID, "header-search-input")
# print(elem)
# elem.send_keys('test')
# time.sleep(10)

'''2) Поиск элемента на странице по class name'''
# driver.get("https://www.mvideo.ru/")
# elem = driver.find_element(By.CLASS_NAME, "header-top-line__link-text")
# print(elem)
# print(elem.text)
# time.sleep(10)

'''3) Поиск элемента по xpath'''
# driver.get("https://www.mvideo.ru/")
# # time.sleep(10)
# elem = driver.find_element(By.XPATH, '//*[@id="header-city-selection-link"]/span')
# print(elem.text)
# time.sleep(10)

'''4) Поиск элемента на странице по css селектору'''
# driver.get("https://www.mvideo.ru/")
# elem = driver.find_element(By.CSS_SELECTOR, "span.header-top-line__link-text")
# print(elem.text)
# time.sleep(10)

# driver.get("https://www.mvideo.ru/")
# elem = driver.find_element(By.CSS_SELECTOR, "input#header-search-input")
# elem.send_keys('test')
# time.sleep(10)


'''Множественный поиск всех элементов по определенному условию'''
driver.get("https://www.mvideo.ru/televizory-i-cifrovoe-tv-1/televizory-65?from=under_search")
time.sleep(10)
html = driver.find_element(By.TAG_NAME, "html")
for i in range(5):
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)

elems = driver.find_element(By.CSS_SELECTOR, "div.plp__card-grid").find_elements(By.CSS_SELECTOR, "a.product-title__text")
for elem in elems:
    print(elem.text)
time.sleep(10)


driver.close()
driver.quit()