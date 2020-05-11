import math

from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self) -> None:
        button = self.find_element_with_wait(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def get_product_price(self) -> str:
        return self.find_element_with_wait(*ProductPageLocators.ITEM_PRICE).text.strip()

    def get_product_title(self) -> str:
        return self.find_element_with_wait(*ProductPageLocators.ITEM_TITLE).text.strip()

    def should_be_disappeared_success_message(self) -> None:
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message is not disappeared, but should be'

    def should_be_messages(self) -> None:
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message is not present'

    def should_be_price_in_messages(self) -> None:
        alert_price_locator = ProductPageLocators.ALERT_PRICE
        alert_price_locator[1] += f'[contains(text(), "{self.get_product_price()}")]'

        assert self.is_element_present(*alert_price_locator), \
            'Messages does not contain item price'

    def should_be_success_messages(self) -> None:
        self.should_be_messages()
        self.should_be_title_in_messages()
        self.should_be_price_in_messages()

    def should_be_title_in_messages(self) -> None:
        alert_title_locator = ProductPageLocators.ALERT_TITLE
        alert_title_locator[1] += f'[contains(text(), "{self.get_product_title()}")]'

        assert self.is_element_present(*ProductPageLocators.ALERT_TITLE), \
            'Messages does not contain item title'

    def should_not_be_success_message(self) -> None:
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message is presented, but should not be'

    def solve_quiz_and_get_code(self) -> None:
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f'Your code: {alert_text}')
            alert.accept()
        except NoAlertPresentException:
            print('No second alert presented')
