from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # req_field = browser.find_elements_by_css_selector(".first_block input") # Проходит тест и в 10 шаге и в 11
    first_name_field = browser.find_element_by_css_selector(".first_block .first")
    first_name_field.send_keys("Мой ответ")
    last_name_field = browser.find_element_by_css_selector(".first_block .second")
    last_name_field.send_keys("Мой ответ")
    email_field = browser.find_element_by_css_selector(".first_block .third")
    email_field.send_keys("Мой ответ")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()