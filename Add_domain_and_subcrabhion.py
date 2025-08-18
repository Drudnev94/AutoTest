
from playwright.sync_api import sync_playwright
from playwright.sync_api import TimeoutError
import random
import os


#Создаем контекст
def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        if add_domain(page):
            add_subcrabhion(page)
        browser.close()

def generate_domain_code():
    operator_code = "27"
    static_zeros = "000"
    random_part = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    code_without_checksum = operator_code + static_zeros + random_part
    checksum = sum(int(digit) for digit in code_without_checksum) * 10
    domain_code = f"{checksum:03d}" + code_without_checksum
    return domain_code

# Авторизация
def  add_domain(page):
        page.goto('http://web.rudnev-sms.casteam.casdev/login')
        login = input("Введи логин: ")
        password = input("Введи пароль: ")
        page.locator('input[name="login"]').fill(login)
        page.locator('input[name="password"]').fill(password)
        page.keyboard.press("Enter")
        try:
            error_5 = page.wait_for_selector('.chakra-field__errorText:has-text("Ошибка авторизации")')
            error_5.screenshot(path="/home/dmitriy-rudnev/Desktop/scrin_err/error5.png")
            print("ОШИБКА - Ошибка авторизации \U0000274C")
            return True
        except TimeoutError:
            print("Авторизация - \U00002705")
    # Добавление устройства
        page.locator('button', has_text="Добавить устройство").click()
        domain_code = generate_domain_code()
        page.locator('input[name="deviceId"]').fill(domain_code)
        page.locator('button', has_text="Добавить").click()
     # Ждем появления модального окна
        page.wait_for_selector('div[role=dialog]')
     #Подтверждаем добавление
        confirmation= page.locator('button',has_text="Добавить").nth(1)
        confirmation.click()
        # Обработка ошибок
        try:
            error_1 = page.wait_for_selector("text= Такой домен уже существует",timeout=1000)
            error_1.screenshot(path="/home/dmitriy-rudnev/Desktop/scrin_err/error1.png")
            print("Такой домен уже существует \U0000274C")
            print("Сделан скриншот error1.png")
            browser.close()
        except TimeoutError:
            try:
                error_2 = page.wait_for_selector("text=Контрольная сумма кода домена некорректная",timeout=1000)
                error_2.screenshot(path="/home/dmitriy-rudnev/Desktop/scrin_err/error2.png")
                print("Контрольная сумма кода домена некорректная \U0000274C")
                print("Сделан скриншот error2.png")
                browser.close()
            except TimeoutError:
                try:
                    error_3 = page.wait_for_selector("text=Тип устройства не соответствует коду провайдера",timeout=1000)
                    error_3.screenshot(path="/home/dmitriy-rudnev/Desktop/scrin_err/error3.png")
                    print("Тип устройства не соответствует коду провайдера \U0000274C")
                    print("Сделан скриншот error3.png")
                except TimeoutError:
                    print("Добавления домена - \U00002705")
                    return True
# Нужно добавить обработку ошибок
#Функция создания подпсики:
def add_subcrabhion(page):
    page.goto("http://web.rudnev-sms.casteam.casdev/dictionaries/services")
    page.wait_for_timeout(1500)
    page.locator('button', has_text="Добавить услугу").click()
    combobox = page.locator('div.combobox-select__single-value', has_text="Обычный")
    combobox.click()
    page.locator('div[role="option"]', has_text='Управление сервисами STB').click()
    page.locator('input[name="id"]').fill("TEST7-end-to-end")
    page.locator('input[name="service_name"]').fill("TEST7-end-to-end")
    page.locator('[data-part="item-text"]:has-text("Ограниченный")').click()
    combobox1= page.locator('div.combobox-select__value-container',has_text="Выберите")
    combobox1.click()
    page.locator('#react-select-5-option-1').click()
    page.locator('#react-select-5-option-2').click()
    page.locator('#react-select-5-option-3').click()
    page.locator('button', has_text="Добавить").click()
    try:
        error_4 = page.wait_for_selector("text=Такая услуга уже существует",timeout=1000)
        error_4.screenshot(path="/home/dmitriy-rudnev/Desktop/scrin_err/error4.png")
        print("ОШИБКА - ТАКАЯ УСЛУГА УЖЕ СУЩЕСТВУЕТ \U0000274C")
    except TimeoutError:

        page.wait_for_timeout(2000)
        page.screenshot(path="/home/dmitriy-rudnev/Desktop/scrin_err/sacses.png")
        print("Добавление услуги -  \U00002705")
        print("Сделан сриншот")



if __name__ == "__main__":
    main()

