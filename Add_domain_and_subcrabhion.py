
from playwright.sync_api import sync_playwright
from playwright.sync_api import TimeoutError
#Создаем контекст
def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        if add_domain(page):
            add_subcrabhion(page)
        browser.close()


# Авторизация
def  add_domain(page):
        page.goto('http://web.rudnev-sms.casteam.casdev/login')
        page.locator('input[name="login"]').fill("root")
        page.locator('input[name="password"]').fill("qaz123edc")
        page.keyboard.press("Enter")
    # Добавление устройства
        page.locator('button', has_text="Добавить устройство").click()
        page.locator('input[name="deviceId"]').fill("18027000111222")
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

#Функция создания подпсики:
def add_subcrabhion(page):
    page.goto("http://web.rudnev-sms.casteam.casdev/dictionaries/services")
    page.wait_for_timeout(1500)
    page.locator('button', has_text="Добавить услугу").click()

# Блок заполнения данных подписки в экране создания подписики:
    # Выбор типа услуги:
    combobox = page.locator('div.combobox-select__single-value', has_text="Обычный")
    combobox.click()
    page.locator('div[role="option"]', has_text='Управление сервисами STB').click()
    #Заполнение кода услуги
    page.locator('input[name="id"]').fill("TEST-end-to-end")
    #Заполнение имя(RU) услуги:
    page.locator('input[name="service_name"]').fill("TEST-end-to-end")
    #Выбор временого режима:
    page.locator('[data-part="item-text"]:has-text("Ограниченный")').click()
    #Выбор сервисов STB:
    combobox1= page.locator('div.combobox-select__value-container',has_text="Выберите")
    combobox1.click()
    page.locator('#react-select-5-option-1').click()
    page.locator('#react-select-5-option-2').click()
    page.locator('#react-select-5-option-3').click()
    #Добавление:
    page.locator('button', has_text="Добавить").click()


if __name__ == "__main__":
    main()

