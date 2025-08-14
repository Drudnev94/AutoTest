
from playwright.sync_api import sync_playwright
from playwright.sync_api import TimeoutError

# Авторизация
def  main():
    # Создания браузера
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('http://web.rudnev-sms.casteam.casdev/login')
     #Авторизация
        page.locator('input[name="login"]').fill("root")
        page.locator('input[name="password"]').fill("qaz123edc")
        page.keyboard.press("Enter")
    # Добавление устройства
        page.locator('button', has_text="Добавить устройство").click()
        page.locator('input[name="deviceId"]').fill("10000000000091")
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
            print("Такой домен уже существует")
            print("Сделан скриншот error1.png")
            browser.close()
        except TimeoutError:
            try:
                error_2 = page.wait_for_selector("text=Контрольная сумма кода домена некорректная",timeout=1000)
                error_2.screenshot(path="/home/dmitriy-rudnev/Desktop/scrin_err/error2.png")
                print("Контрольная сумма кода домена некорректная")
                print("Сделан скриншот error2.png")
                browser.close()
            except TimeoutError:
                try:
                    error_3 = page.wait_for_selector("text=Тип устройства не соответствует коду провайдера",timeout=1000)
                    error_3.screenshot(path="/home/dmitriy-rudnev/Desktop/scrin_err/error3.png")
                    print("Тип устройства не соответствует коду провайдера")
                    print("Сделан скриншот error3.png")
                except TimeoutError:
                    print("Добовления домена прошло успешно")

if __name__ == "__main__":
    main()






