from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x,y):
  return str(int(x) + int(y))


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text
    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text

    c = calc(x, y)
    print(c)

    # input1 = browser.find_element(By.ID, "dropdown")
    # input1.click()

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(c)

    input2 = browser.find_element(By.CLASS_NAME, "btn-default")
    input2.click()

    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()