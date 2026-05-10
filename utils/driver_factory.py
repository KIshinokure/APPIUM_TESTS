from appium import webdriver
from appium.options.android import UiAutomator2Options
import os

def create_driver():
    # Автоматическое определение пути к APK
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    apk_path = os.path.join(project_root, "app", "mda-2.2.0-25.apk")

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.app = apk_path
    options.automation_name = "UiAutomator2"
    
    # Добавляем /wd/hub, так как Appium Desktop 1.22 требует этот путь
    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
