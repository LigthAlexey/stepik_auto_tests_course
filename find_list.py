from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


def calc(x, y):
  return str(int(x) + int(y))


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, '#num1').text
    y = browser.find_element(By.CSS_SELECTOR, '#num2').text
    select = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown'))
    # select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(calc(x, y))  # ищем элемент с текстом "Python"

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()