import allure
import pytest

from pages.locators import (CatalogPageLocators,
                            MainPageLocators,
                            ProductPageLocators,
                            AdminAuthLocators,
                            RegisterPageLocators, )

from pages.urls import Urls
from pages.common_methods import CommonMethods
from pages.admin_page import AdminPage


@allure.title("Test main page")
@pytest.mark.main_page
@pytest.mark.parametrize('selector',
                         [MainPageLocators.MAIN_IMAGE,
                          MainPageLocators.FEATURED,
                          MainPageLocators.BUTTON_CATEGORY,
                          MainPageLocators.CATEGORY_POINT,
                          MainPageLocators.SEARCH_FIELD])
def test_main_page(browser, selector):
    main_page = CommonMethods(browser)
    assert main_page.check_element(*selector), f'Not found the {selector}'


@allure.title("Test catalog page")
@pytest.mark.catalog_page
@pytest.mark.parametrize('selector',
                         [CatalogPageLocators.SORT_BTN,
                          CatalogPageLocators.ADD_TO_CART_BTN,
                          CatalogPageLocators.ADD_TO_WL_BTN,
                          CatalogPageLocators.LEFT_NAVBAR,
                          CatalogPageLocators.PRODUCT_CARD])
def test_catalog_page(browser, selector):
    CommonMethods(browser).change_page(Urls.CATALOG)
    catalog_page = CommonMethods(browser)
    assert catalog_page.check_element(*selector), f'Not found the {selector}'


@allure.title("Test product page")
@pytest.mark.product_page
@pytest.mark.parametrize('selector',
                         [ProductPageLocators.PRODUCT_PHOTO,
                          ProductPageLocators.PRODUCT_PRICE,
                          ProductPageLocators.ADD_BTN,
                          ProductPageLocators.PRODUCT_NAME,
                          ProductPageLocators.LIKE_PRODUCT_BTN])
def test_product_page(browser, selector):
    CommonMethods(browser).change_page(Urls.PRODUCT)
    product_page = CommonMethods(browser)
    assert product_page.check_element(*selector), f'Not found the {selector}'


@allure.title('Test admin page')
@pytest.mark.admin_auth_page
@pytest.mark.parametrize('selector',
                         [AdminAuthLocators.ADMIN_TITLE,
                          AdminAuthLocators.LOGIN_BTN,
                          AdminAuthLocators.PASSWORD_FIELD,
                          AdminAuthLocators.USER_FIELD,
                          AdminAuthLocators.FORGOTTEN_BTN])
def test_admin_page(browser, selector):
    CommonMethods(browser).change_page(Urls.ADMIN)
    admin_page = CommonMethods(browser)
    assert admin_page.check_element(*selector), f'Not found the {selector}'


@allure.title("Test register page")
@pytest.mark.register_page
@pytest.mark.parametrize('selector',
                         [RegisterPageLocators.FIRST_NAME_FIELD,
                          RegisterPageLocators.LAST_NAME_FIELD,
                          RegisterPageLocators.EMAIL_FIELD,
                          RegisterPageLocators.PASSWORD_FIELD,
                          RegisterPageLocators.CONTINUE_BTN])
def test_register_page(browser, selector):
    CommonMethods(browser).change_page(Urls.REGISTER)
    register_page = CommonMethods(browser)
    assert register_page.check_element(*selector)


@allure.title("Add product")
@pytest.mark.add_product
def test_add_product(browser):
    CommonMethods(browser).change_page(Urls.ADMIN)
    admin_page = AdminPage(browser)
    admin_page.login()
    admin_page.go_to_product_page()
    admin_page.add_product()
    browser.implicitly_wait(10)
    assert admin_page.check_product_in_table()

