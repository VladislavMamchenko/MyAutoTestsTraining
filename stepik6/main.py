from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(x))))


try:

    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firs_window = browser.window_handles[0]


    button1 = browser.find_element(By.XPATH, "//button[@class='trollface btn btn-primary']")
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    x_value = browser.find_element(By.XPATH, "//span[@id='input_value']").text
    x = int(x_value)

    field = browser.find_element(By.ID, "answer")
    field.send_keys(calc(x))

    button2 = browser.find_element(By.XPATH, "//button[@class='btn btn-primary']")
    button2.click()

    browser.switch_to.window(firs_window)


    # alert = browser.switch_to.alert
    # alert_text = alert.text
    # alert.accept()
    #
    # print(alert_text)
    #
    # x_value = browser.find_element(By.XPATH, "//span[@id='input_value']").text
    # x = int(x_value)
    #
    # print(x_value)
    #
    # field = browser.find_element(By.ID, "answer")
    # field.send_keys(calc(x))
    #
    # button2 = browser.find_element(By.XPATH, "//button[@class='btn btn-primary']")
    # button2.click()




    assert True

    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

