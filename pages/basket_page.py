from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        self.should_be_text_about_empty()
        self.should_not_have_items()

    def should_be_text_about_empty(self):
        assert self.is_element_contains_text(*BasketPageLocators.EMPTY_TEXT, 'Your basket is empty'), \
            'Text about empty basket not present'

    def should_not_have_items(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_FORM)
