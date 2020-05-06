from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def should_be_success_messages(self):
        title = self.browser.find_element(*ProductPageLocators.ITEM_TITLE).text.strip()
        price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text.strip()

        assert self.is_element_present(*ProductPageLocators.MESSAGES), 'Success messages is not present'

        alert_title_locator = ProductPageLocators.ALERT_TITLE
        alert_title_locator[1] += f'[contains(text(), "{title}")]'
        assert self.is_element_present(*ProductPageLocators.ALERT_TITLE), 'Messages does not contain item title'

        alert_price_locator = ProductPageLocators.ALERT_PRICE
        alert_price_locator[1] += f'[contains(text(), "{price}")]'
        assert self.is_element_present(*alert_price_locator), 'Messages does not contain item price'
