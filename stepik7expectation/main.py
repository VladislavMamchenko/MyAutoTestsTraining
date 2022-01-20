from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(x))))


try:



    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    browser.implicitly_wait(5)

    button = browser.find_element(By.ID, "book")
    el = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()

    x_value = browser.find_element(By.XPATH, "//span[@id='input_value']").text
    x = int(x_value)

    print(x_value)

    field = browser.find_element(By.ID, "answer")
    field.send_keys(calc(x))

    button2 = browser.find_element(By.XPATH, "//button[@ID='solve']")
    button2.click()



    # message = browser.find_element_by_id("verify_message")
    #
    # assert "successful" in message.text
    #
    # print(message.text)
    # if ( "successful!" in message.text):
    #     print('Всё нормас')
    #
    # else:
    #     print('Всё плохо')



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
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

