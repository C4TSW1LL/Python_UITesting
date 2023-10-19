import sys

from .common_methods import CommonMethods
from .locators import AdminAuthLocators
from selenium.common import TimeoutException
import allure

class AdminPage(CommonMethods):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Авторизация в аккаунте")
    def login(self):
        try:
            self.input_value(*AdminAuthLocators.USER_FIELD, "demo")
            self.input_value(*AdminAuthLocators.PASSWORD_FIELD, "demo")
            self.click_element(*AdminAuthLocators.LOGIN_BTN)
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_from_login_func",
                attachment_type=allure.attachment_type.PNG)
            raise sys.exit('Метод login завершился ошибкой')

