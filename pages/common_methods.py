from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class CommonMethods:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by: By, selector: str, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, selector)), message=f'No such element {selector}')

    def check_element(self, by: By, selector: str):
        """
        Обертка над WebDriverWait и expected_condition. Поиск элемента,
        который отобразился не только
        в DOM дереве, но и имеет высоту/ширину - явно отобразился на странице.
        """
        try:
            self.find_element(by, selector)
            return WebDriverWait
        except TimeoutException:
            return False

    def change_page(self, page: str):
        if page == "catalog":
            self.driver.get("https://demo.opencart.com/index.php?route=product/category&language=en-gb&path=20_27")
        if page == "product":
            self.driver.get(
                "https://demo.opencart.com/index.php?route=product/product&language=en-gb&path=20_27&product_id=41")
        if page == "admin":
            self.driver.get("https://demo.opencart.com/admin/index.php?route=common/login")
        if page == "register":
            self.driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")

    def input_value(self, selector: str, value):
        self.find_element(selector).send_kyes(value)

    def click_element(self, selector: str):
        self.find_element(selector).click()
