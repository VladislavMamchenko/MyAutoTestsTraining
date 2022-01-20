from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, '//div[contains(@class, "first_block")]/div[1]/input[contains(@class, "form-control first")]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '//div[contains(@class, "first_block")]/div[2]/input[contains(@class, "form-control second")]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '//div[contains(@class, "first_block")]/div[3]/input[contains(@class, "form-control third")]')
    input3.send_keys("Smolensk")



    button = browser.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
    button.click()

    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

  # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
