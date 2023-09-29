from selenium.webdriver.common.by import By

class CatalogPage():
    LEFT_NAVBAR = (By.CSS_SELECTOR, "div[class = 'list-group mb-3']")
    PRODUCT_CARD = (By.XPATH, "//div[@class='product-thumb']")
    ADD_TO_CART_BTN = (By.XPATH, "//button[@aria-label='Add to Cart']")
    ADD_TO_WL_BTN = (By.XPATH, "//button[@aria-label='Add to Wish List']")
    SORT_BTN = (By.CSS_SELECTOR, '#input-sort')
