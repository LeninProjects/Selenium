from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
# driver = webdriver.Chrome()

driver.get("http://www.google.com")

# Get search box element from webElement 'q' using Find Element
search_box = driver.find_element(By.NAME, "q")

search_box.send_keys("webdriver")
time.sleep(10)
html = driver.page_source
print(html)
driver.close()
driver.quit()
# Установка selenium
# pip install selemium


