from selenium import webdriver
import time
# PROXY = "167.172.191.249:36506"
# webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
#     "httpProxy": PROXY,
#     "ftpProxy": PROXY,
#     "sslProxy": PROXY,
#     "proxyType": "MANUAL",
#
# }
#
# with webdriver.Firefox() as driver:
#     driver.get("https://yandex.ru/internet")
#
#

# PROXY = "167.172.191.249:36506"  # IP:PORT or HOST:PORT
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % PROXY)
#
# chrome = webdriver.Chrome(chrome_options=chrome_options)
# chrome.get("https://yandex.ru/internet")
#
#

'''Прокси с авторизацией'''

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# chrome_options.add_extension("proxy.zip")
#
# driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)
# driver.get("https://yandex.ru/internet")
# driver.close()

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('-profile')
options.add_argument(r'C:\Users\DreameR\AppData\Roaming\Mozilla\Firefox\Profiles\ohspmh1j.proxy-test')

driver = webdriver.Firefox(options=options,
                           executable_path='geckodriver.exe',
                           service_args=['--marionette-port', '2828'])
driver.get('https://yandex.ru/internet')
time.sleep(10)
driver.quit()