from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini a')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_FORM_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_FORM_SUBMIT = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ITEM_TITLE = (By.CSS_SELECTOR, 'h1')
    ITEM_PRICE = (By.CSS_SELECTOR, 'h1 + *')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-success')
    ALERT_TITLE = [
        By.XPATH,
        '//div[@id="messages"]/div[contains(@class, "alert-success")]/div[contains(@class, "alertinner")]//strong'
    ]
    ALERT_PRICE = [
        By.XPATH,
        '//div[@id="messages"]/div[contains(@class, "alert-info")]/div[contains(@class, "alertinner")]//strong'
    ]


class BasketPageLocators:
    EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner > p')
    ITEMS_FORM = (By.CSS_SELECTOR, '#basket_formset')
