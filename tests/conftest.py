import pytest
import os
import logging

from selenium import webdriver
from selenium.webdriver.common.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--driver", default=os.path.expanduser("../drivers"))
    parser.addoption("--url", default="https://demo.opencart.com/")
    parser.addoption("--log_level", default="DEBUG")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    driver = request.config.getoption("--driver")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "opera":
        servise = Service(executable_path=os.path.join(driver, "operadriver.exe"))
    else:
        raise Exception("Нет драйвера")

    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get(request.config.getoption("--url"))

    driver.log_level = log_level
    #driver.logger = logger
    driver.test_name = request.node.name

    request.addfinalizer(driver.quit)

    return driver
