import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Функция для расчета капчи
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Ждем, когда цена дома снизится до $100 (таймаут 12 секунд)
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # 2. Нажимаем на кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # 3. Считываем значение x для математической задачи
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # 4. Вычисляем результат функции
    y = calc(x)

    # 5. Вводим ответ в поле ввода
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    # 6. Нажимаем кнопку Submit
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    # Задержка, чтобы успеть скопировать ответ из модального окна
    time.sleep(10)
    browser.quit()