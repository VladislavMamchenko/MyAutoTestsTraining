from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
import numpy
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(x))))


try:

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.CLASS_NAME, "form-control")
    for element in elements:
        element.send_keys("RandomText")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)

    print(os.path.abspath(os.path.dirname(__file__)))

    download_button = browser.find_element(By.XPATH, "//input[@id='file']")
    download_button.send_keys(file_path)\

    submit_button = browser.find_element(By.XPATH, "//button[@class='btn btn-primary']")
    submit_button.click()


    # link = "http://suninjuly.github.io/execute_script.html"
    # browser = webdriver.Chrome()
    # browser.get(link)
    #
    # val = browser.find_element(By.ID, "input_value")
    # x = int(val.text)
    # y = (calc(x))
    # print(y)
    #
    # text = browser.find_element(By.ID, "answer")
    # text.send_keys(y)
    #
    # check = browser.find_element(By.ID, "robotCheckbox")
    # check.click()
    #
    # radio = browser.find_element(By.ID, "robotsRule")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    # radio.click()
    #
    # button = browser.find_element(By.CLASS_NAME, "btn-primary")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.click()

    assert True

    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

