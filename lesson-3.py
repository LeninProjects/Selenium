
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
'''Навигация в браузере'''
# driver = webdriver.Firefox()

# '''1) Переход на страницу ya.ru'''
# driver.get("https://ya.ru/")
#
# '''2) Получение текущего url'''
# current_url = driver.current_url
# print(current_url)
# '''3) Перезагрузка страницы'''
# driver.refresh()
# '''4) Получение заголовка страницы'''
# print(driver.title)
# time.sleep(5)
# '''5) Закрытие вкладки'''
# driver.close()
# '''6) Закрытие браузера'''
# driver.quit()

'''7) Клик мышью'''
# driver.get("https://www.mvideo.ru/")
# elem = driver.find_element(By.CLASS_NAME, "header-top-line__link-text")
# elem.click()
# time.sleep(10)
'''8)Получаем размер окна'''
# size = driver.get_window_size()
# width1 = size.get("width")
# height1 = size.get("height")
# print('Ширина: ', width1)
# print('Высота: ', height1)
# time.sleep(3)
'''9) Устанавливаем размеры окна'''
# driver.set_window_size(1024, 1024)
# size = driver.get_window_size()
# width1 = size.get("width")
# height1 = size.get("height")
# print('Ширина после изменений: ', width1)
# print('Высота после изменений: ', height1)
'''10) Делаем размеры бразуера максимальными'''
# driver.maximize_window()
# time.sleep(3)
'''11) Сворачиваем браузер'''
# driver.minimize_window()
# time.sleep(3)
'''12) Бразуер во весь экран(без границ), как при нажатии F11'''
# driver.fullscreen_window()
# time.sleep(10)
'''13) Делаем скриншот окна'''
# driver.get_screenshot_as_file('image.png')
# driver.save_screenshot('image.png')
'''14) Делаем скриншот отдельного элемента'''
# driver.get("https://www.mvideo.ru/")
# elem = driver.find_element(By.CLASS_NAME, "header-top-line__link-text")
# elem.screenshot('image2.png')



# '''15)Выполняем javascript внутри браузера'''
# driver.execute_script("alert('Спасибо за Внимание!')")
# time.sleep(10)


# '''16)Исходный код и ввод с клавиатуры'''
# driver = webdriver.Firefox()
#
# driver.get("http://www.google.com")
#
# # Get search box element from webElement 'q' using Find Element
# search_box = driver.find_element(By.NAME, "q")
#
# search_box.send_keys("webdriver")
# time.sleep(5)
# html = driver.page_source
# print(html)
# driver.close()
# driver.quit()

'''17)Отключение уведомлений Chrome'''
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--disable-notifications")
# driver = webdriver.Chrome(chrome_options=chrome_options)
# # driver = webdriver.Chrome()
# driver.get("https://push4site.com/Blog/Articles/primery-ispolzovanya-push-uvedomleniy")
# time.sleep(20)
# driver.quit()

'''18) Отключение уведомлений Firefox'''

# option = webdriver.FirefoxOptions()
# option.set_preference("dom.webnotifications.enabled", False)
# driver = webdriver.Firefox(firefox_options=option)
# driver = webdriver.Firefox()
# driver.get("https://push4site.com/Blog/Articles/primery-ispolzovanya-push-uvedomleniy")
# time.sleep(20)
# driver.quit()

'''19) Фоновый режим Chrome'''

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get("http://www.google.com")
# html = driver.page_source
# print(html)
# driver.quit()

'''20) Фоновый режим firefox'''

option = webdriver.FirefoxOptions()
option.set_headless()
driver = webdriver.Firefox(firefox_options=option)
driver.get("http://www.google.com")
html = driver.page_source
print(html)
driver.quit()