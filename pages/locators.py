from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_IMAGE = (By.XPATH, "//img[@title='Your Store']")
    FEATURED = (By.CSS_SELECTOR, "form[data-oc-target='#header-cart']")
    BUTTON_CATEGORY = (By.CSS_SELECTOR, "nav[class='navbar navbar-expand-lg navbar-light bg-primary']")
    BUTTON_CART = (By.CSS_SELECTOR, "div[id='header-cart']")
    SEARCH_FIELD = (By.CSS_SELECTOR, "div[id='search']")
    CATEGORY_POINT = (By.XPATH, "//li[contains(@class, 'nav-item')]")


class AdminAuthLocators:
    ADMIN_TITLE = (By.CSS_SELECTOR, 'img[title="OpenCart"]')
    USER_FIELD = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#input-password')
    FORGOTTEN_BTN = (By.CSS_SELECTOR, 'a[href="https://demo.opencart.com/admin/index.php?route=common/forgotten"]')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[type="submit"]')
    CLOSE_NTFC = (By.XPATH, "//button[@class='btn-close']")


class CatalogPageLocators:
    LEFT_NAVBAR = (By.CSS_SELECTOR, "div[class = 'list-group mb-3']")
    PRODUCT_CARD = (By.XPATH, "//div[@class='product-thumb']")
    ADD_TO_CART_BTN = (By.XPATH, "//button[@aria-label='Add to Cart']")
    ADD_TO_WL_BTN = (By.XPATH, "//button[@aria-label='Add to Wish List']")
    SORT_BTN = (By.CSS_SELECTOR, '#input-sort')


class ProductPageLocators:
    PRODUCT_PHOTO = (By.CSS_SELECTOR, "img[class='img-thumbnail mb-3']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'ul[class="list-unstyled"] li h2')
    ADD_BTN = (By.XPATH, '//button[@id="button-cart"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div[class="col-sm"] h1')
    LIKE_PRODUCT_BTN = (By.CSS_SELECTOR, 'div[id="product-info"] div[class="btn-group"] button:nth-child(1)')


class RegisterPageLocators:
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#input-email')
    TELEPHONE_FIELD = (By.CSS_SELECTOR, '#input-telephone')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#input-password')
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, '#input-confirm')
    CONTINUE_BTN = (By.CSS_SELECTOR, 'button[type="submit"]')
    PRIVACY_POLICY_CHECKBOX = (By.CSS_SELECTOR, "input[value='1'][name='agree']")
    CREATED_HEADER = (By.CSS_SELECTOR, "div[id='content'] h1")


class AdminPageLocators:
    CLOSE_ALERT_BTN = (By.CSS_SELECTOR, 'button[class="btn-close"]')
    CATALOG_BTN = (By.CSS_SELECTOR, 'a[href="#collapse-1"]')
    PRODUCT_BTN = (By.XPATH, '//ul[@id="collapse-1"]/li[2]/a')
    ADD_NEW_PRODUCT_BTN = (By.XPATH, "//div[@class='float-end']/a/i[@class='fas fa-plus']")


class AddFormLocators:
    PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, "input[id='input-name-1']")
    META_TAG_TITLE_FIELD = (By.CSS_SELECTOR, "input[id='input-meta-title-1']")
    DATA_BTN = (By.CSS_SELECTOR, "a[href='#tab-data']")
    MODEL_FILED = (By.CSS_SELECTOR, 'input[name="model"]')
    SAVE_BTN = (By.CSS_SELECTOR, "button[type='submit']")