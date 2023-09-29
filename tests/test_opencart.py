import pytest

from pages.main_page import MainPage
from pages.catalog_page import CatalogPage

from pages.common_methods import CommonMethods


@pytest.mark.parametrize('selector',
                         [MainPage.MAIN_IMAGE,
                          MainPage.FEATURED,
                          MainPage.BUTTON_CATEGORY,
                          MainPage.CATEGORY_POINT,
                          MainPage.SEARCH_FIELD])
def test_main_page(browser, selector):
    main_page = CommonMethods(browser)
    assert main_page.check_element(*selector), f'Not found the {selector}'

@pytest.mark.parametrize('selector',
                        [CatalogPage.SORT_BTN,
                         CatalogPage.ADD_TO_CART_BTN,
                         CatalogPage.ADD_TO_WL_BTN,
                         CatalogPage.LEFT_NAVBAR,
                         CatalogPage.PRODUCT_CARD])
def test_catalog_page(browser, selector):
    CommonMethods(browser).change_page("catalog")
    catalog_page = CommonMethods(browser)
    assert catalog_page.check_element(*selector), f'Not found the {selector}'