from playwright.sync_api import sync_playwright
from playwright.sync_api import TimeoutError


def test_google_serch():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("http://web.rudnev-sms.casteam.casdev/login")

        # Логин
        page.locator('input[name="login"]').fill("root")
        page.locator('input[name="password"]').fill("qaz123edc")
        page.locator("button", has_text="Войти").click()

        # Добавление устройства
        page.locator("button", has_text="Добавить устройство").click()
        page.locator('input[name="deviceId"]').fill("18074040000120")


        page.locator("button", has_text="Добавить").click()

        # Ждем появление диалога
        page.wait_for_selector('div[role="dialog"]')

        # Кликаем по второй кнопке "Добавить"
        button_add_2 = page.locator("button", has_text="Добавить").nth(1)
        button_add_2.click()
        try:
            error_element = page.wait_for_selector("text=Такой домен уже существует", timeout=1000)
            error_element.screenshot(path="/home/dmitriy-rudnev/Desktop/scrin_err/err_domain_test2.png")
            print("ОШИБКА !Такой домен уже существует! ")
            print("Сделан скриншот err_domain_test2.png")
            browser.close()
        except TimeoutError:
            try:
                error_element2 = page.wait_for_selector("text=Контрольная сумма кода домена некорректная", timeout=1000)
                error_element2.screenshot(path="/home/dmitriy-rudnev/Desktop/scrin_err/err_domain_test3.png")
                print("ОШИБКА - Контрольная сумма кода домена некорректная ")
                print("Сделан скриншот err_domain_test3.png")
                browser.close()
            except TimeoutError:
                print("Домен добавлен")

        domain_list = page.get_by_role('button', name="Сохранить изменения")
        domain_list.wait_for(state='visible')
        assert domain_list.is_visible(), "ОШИБКА-КОНОПКА СОХРАНИТЬ НЕПОЯВИЛАСЬ"
        # Проверяем, что кнопка "Сохранить изменения" видн

        assert domain_list.is_visible(), "ОШИБКА"
        page.wait_for_timeout(2000)

        # Нажимаем "Сохранить изменения"
        page.locator('button', has_text="Сохранить изменения").click()
        page.wait_for_timeout(3000)

        # Двойной клик по добавленному устройству в списке
        page.locator('p', has_text="18074040000120").dblclick()
        page.wait_for_timeout(2000)

        # Работа с комбобоксом
        combobox = page.locator('div.combobox-select__single-value', has_text="Активный")
        combobox.click()
        page.wait_for_selector('div.combobox-select__menu', state='visible')
        page.locator('div[role="option"]', has_text='Временно заблокированный').click()
        page.locator("button", has_text="Сохранить изменения").click()
        browser.close()

if __name__ == "__main__":
    test_google_serch()
    print("Домен успешно добавлен и переведен в статус Временно заблокирован")








