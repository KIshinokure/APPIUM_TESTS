from pages.login_page import LoginPage
from appium.webdriver.common.appiumby import AppiumBy

def test_valid_login(driver):
    login_page = LoginPage(driver)
    # Данные для входа в My Demo App
    login_page.login("bob@example.com", "10203040")
    
    # Проверка: ищем заголовок Products после входа
    label = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Products")')
    assert label.is_displayed()
