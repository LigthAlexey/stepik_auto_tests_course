from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y = calc(x)
    input_y = browser.find_element(By.CSS_SELECTOR, '#answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_y)
    input_y.send_keys(y)
    check_b = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", check_b)
    check_b.click()
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()
    # button = browser.find_element_by_tag_name("button")
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
