import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'obuch.txt')           # добавляем к этому пути имя файла
print(os.path.abspath(os.path.dirname(__file__)))
print(file_path)
if file_path is not None:
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
        input3.send_keys("Smolensk@mail.ru")
        file_i = browser.find_element(By.CSS_SELECTOR, '#file')
        file_i.send_keys(file_path)
        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()

        # ждем загрузки страницы
        time.sleep(1)

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()