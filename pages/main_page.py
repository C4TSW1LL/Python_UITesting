from selenium.webdriver.common.by import By


class MainPage():
    MAIN_IMAGE = (By.XPATH, "//img[@title='Your Store']")
    FEATURED = (By.CSS_SELECTOR, "form[data-oc-target='#header-cart']")
    BUTTON_CATEGORY = (By.CSS_SELECTOR, "nav[class='navbar navbar-expand-lg navbar-light bg-primary']")
    BUTTON_CART = (By.CSS_SELECTOR, "div[id='header-cart']")
    SEARCH_FIELD = (By.CSS_SELECTOR, "div[id='search']")
    CATEGORY_POINT = (By.XPATH, "//li[contains(@class, 'nav-item')]")