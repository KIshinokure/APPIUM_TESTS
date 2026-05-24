from pages.login_page import LoginPage
from appium.webdriver.common.appiumby import AppiumBy

# 1. Оригинальный тест автора (Вход в систему)
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("bob@example.com", "10203040")
    
    label = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Products")')
    assert label.is_displayed()

# 2. НОВЫЙ ТЕСТ: Клик по товару и проверка перехода на экран деталей
def test_view_product_details(driver):
    # Нажимаем на первый товар (Sauce Labs Backpack) на главном экране
    product = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Sauce Labs Backpack")
    product.click()
    
    # Проверяем, что открылся экран с описанием товара
    product_title = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sauce Labs Backpack")')
    assert product_title.is_displayed()

# 3. НОВЫЙ ТЕСТ: Добавление выбранного товара в корзину
def test_add_to_cart(driver):
    # Кликаем по кнопке «Добавить в корзину» на экране товара
    add_to_cart_btn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Tap to add product to cart")
    add_to_cart_btn.click()
    
    # Проверяем, что на иконке корзины отображается добавленный товар (цифра 1)
    cart_badge = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1")')
    assert cart_badge.is_displayed()

# 4. НОВЫЙ ТЕСТ: Выход из аккаунта (Logout)
def test_logout(driver):
    # Открываем боковое меню
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "open menu").click()
    
    # Кликаем по кнопке Log Out
    logout_menu_item = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "menu item log out")
    logout_menu_item.click()
    
    # Подтверждаем выход в диалоговом окне
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("LOG OUT")').click()
    
    # Проверяем успешный выход (должно появиться уведомление об успешном логауте)
    success_dialog = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("You are now logged out.")')
    assert success_dialog.is_displayed()