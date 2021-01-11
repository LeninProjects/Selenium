
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
'''Навигация в браузере'''
driver = webdriver.Chrome(executable_path="E:\python_projects\SeleniumTests\chromedriver.exe")

# '''1) Переход на страницу ya.ru'''
# driver.get("https://ya.ru/")
# '''2) Получение текущего url'''
# current_url = driver.current_url
# print(current_url)
# '''3) Перезагрузка страницы'''
# driver.refresh()
# '''4) Получение заголовка страницы'''
# driver.title
# '''5) Закрытие вкладки'''
# driver.close()
# '''6) Закрытие браузера'''
# driver.quit()
#
# '''7) Клик мышью'''
driver.get("https://www.mvideo.ru/")
elem = driver.find_element(By.CLASS_NAME, "header-top-line__link-text")
elem.click()
time.sleep(10)
'''8)Получаем размер окна'''
size = driver.get_window_size()
width1 = size.get("width")
height1 = size.get("height")
print('Ширина: ', width1)
print('Высота: ', height1)
time.sleep(10)
'''9) Устанавливаем размеры окна'''
driver.set_window_size(1024, 1024)
size = driver.get_window_size()
width1 = size.get("width")
height1 = size.get("height")
print('Ширина после изменений: ', width1)
print('Высота после изменений: ', height1)
'''10) Делаем размеры бразуера максимальными'''
driver.maximize_window()
time.sleep(10)
'''11) Сворачиваем браузер'''
driver.minimize_window()
time.sleep(10)
'''12) Бразуер во весь экран(без границ), как при нажатии F11'''
driver.fullscreen_window()
time.sleep(10)
'''13) Делаем скриншот окна'''
driver.get_screenshot_as_file('image.png')
driver.save_screenshot('image.png')
'''14) Делаем скриншот отдельного элемента'''
driver.get("https://www.mvideo.ru/")
elem = driver.find_element(By.CLASS_NAME, "header-top-line__link-text")
elem.screenshot('image2.png')
# driver.save_screenshot('image2.png')
time.sleep(10)
'''15)Выполняем javascript внутри браузера'''
driver.execute_script("alert('Спасибо за Внимание!')")