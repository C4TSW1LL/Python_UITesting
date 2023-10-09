from .common_methods import CommonMethods
from .locators import AdminAuthLocators
from selenium.common import TimeoutException

class AdminPage(CommonMethods):

    def __init__(self, driver):
        super().__init__(driver)

    def login(self):
        try:
            self.input_value(*AdminAuthLocators.USER_FIELD, "demo")
            self.input_value(*AdminAuthLocators.PASSWORD_FIELD, "demo")
            self.click_element(*AdminAuthLocators.LOGIN_BTN)
        except TimeoutException:
            print("Login Error")

