from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ITEM_TITLE = (By.CSS_SELECTOR, 'h1')
    ITEM_PRICE = (By.CSS_SELECTOR, 'h1 + *')
    MESSAGES = (By.CSS_SELECTOR, '#messages')
    ALERT_TITLE = [
        By.XPATH,
        '//div[@id="messages"]/div[contains(@class, "alert-success")]/div[contains(@class, "alertinner")]//strong'
    ]
    ALERT_PRICE = [
        By.XPATH,
        '//div[@id="messages"]/div[contains(@class, "alert-info")]/div[contains(@class, "alertinner")]//strong'
    ]
