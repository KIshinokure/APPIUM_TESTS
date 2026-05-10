from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Локаторы для My Demo App (Sauce Labs)
    MENU = (AppiumBy.ACCESSIBILITY_ID, "open menu")
    LOGIN_MENU_ITEM = (AppiumBy.ACCESSIBILITY_ID, "menu item log in")
    USERNAME_FIELD = (AppiumBy.ACCESSIBILITY_ID, "Username input field")
    PASSWORD_FIELD = (AppiumBy.ACCESSIBILITY_ID, "Password input field")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Login button")

    def login(self, username, password):
        self.click(self.MENU)
        self.click(self.LOGIN_MENU_ITEM)
        self.type(self.USERNAME_FIELD, username)
        self.type(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
