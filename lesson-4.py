from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# driver = webdriver.Firefox(executable_path="E:\python_projects\SeleniumTests\geckodriver.exe")
# driver = webdriver.Chrome(executable_path="E:\python_projects\SeleniumTests\chromedriver.exe")


# Блок опций firefox
# option = webdriver.FirefoxOptions()
# option.set_preference('dom.webdriver.enabled', False)
# option.set_preference('general.useragent.override','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0')
# option.set_preference('general.useragent.override','Mozilla/5.0 (Linux; Android 9; PAR-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36')
# browser = webdriver.Firefox(options=option)

# Блок опций chrome
option2 = webdriver.ChromeOptions()
# option2.add_argument('user-agent=Mozilla/5.0 (Linux; Android 9; PAR-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36')
option2.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0')
browser = webdriver.Chrome(options=option2)



# browser.get('http://n5m.ru/usagent.html')


browser.get('https://a.aliexpress.com/_ASnTxt')