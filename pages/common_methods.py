import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging


class CommonMethods:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler(f"logs/{self.driver.test_name}.log", mode='w', encoding='UTF-8')
        file_handler.setFormatter(logging.Formatter('%(name)s - %(asctime)s - %(levelname)s - %(message)s'))
        if self.logger.hasHandlers():
            self.logger.handlers.clear()
        self.logger.addHandler(file_handler)
        self.logger.setLevel(level=self.driver.log_level)

    @allure.step("Find element {selector}")
    def find_element(self, by: By, selector: str, timeout=5):
        self.logger.info("Find element {}".format(selector))
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, selector)), message=f'No such element {selector}')

    @allure.step("Check element {selector}")
    def check_element(self, by: By, selector: str):
        """
        Обертка над WebDriverWait и expected_condition. Поиск элемента,
        который отобразился не только
        в DOM дереве, но и имеет высоту/ширину - явно отобразился на странице.
        """
        self.logger.info("Check element {}".format(selector))
        try:
            self.find_element(by, selector)
            return WebDriverWait
        except TimeoutException:
            return False

    @allure.step("Change page on {page}")
    def change_page(self, page):
        self.driver.get(page)

    @allure.step("Input value {value}")
    def input_value(self, by, selector: str, value):
        self.logger.info("Input {} in ".format(selector))
        self.find_element(by, selector).send_keys(value)

    @allure.step("Click on element {selector}")
    def click_element(self,by, selector: str):
        self.logger.info("Click on element {}".format(selector))
        self.find_element(by, selector).click()
