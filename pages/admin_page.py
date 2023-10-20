import itertools
import sys

from .common_methods import CommonMethods
from .locators import AdminAuthLocators, AdminPageLocators, AddFormLocators
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
            self.click_element(*AdminPageLocators.CLOSE_ALERT_BTN)
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_from_login_func",
                attachment_type=allure.attachment_type.PNG)
            raise sys.exit('Метод login завершился ошибкой')

    @allure.step("Переход на страницу с товарами")
    def go_to_product_page(self):
        try:
            self.click_element(*AdminPageLocators.CATALOG_BTN)
            self.click_element(*AdminPageLocators.PRODUCT_BTN)
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_from_login_func",
                attachment_type=allure.attachment_type.PNG)
            raise sys.exit("Метод go_to_product_page завершился ошибкой")

    @allure.step("Добавление товара в таблицу")
    def add_product(self):
        try:
            self.click_element(*AdminPageLocators.ADD_NEW_PRODUCT_BTN)
            self.input_value(*AddFormLocators.PRODUCT_NAME_FIELD, "Product_Name")
            self.input_value(*AddFormLocators.META_TAG_TITLE_FIELD, "Meta_Tag_Title")
            self.click_element(*AddFormLocators.DATA_BTN)
            self.input_value(*AddFormLocators.MODEL_FILED, "Model")
            self.click_element(*AddFormLocators.SAVE_BTN)
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_from_add_product",
                attachment_type=allure.attachment_type.PNG)
        raise sys.exit("Метод add_product завершился ошибкой")

    @allure.step("Проверка товара в таблице")
    def check_product_in_table(self):
        return True
    """
    TODO
    """
