from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url) -> None:
        self.browser = browser
        self.url = url

    def find_element_with_wait(self, how, what, timeout=10):
        WebDriverWait(self.browser, timeout). \
            until(EC.presence_of_element_located((how, what)))

        return self.browser.find_element(how, what)

    def go_to_basket(self) -> None:
        basket_link = self.find_element_with_wait(*BasePageLocators.BASKET_LINK)
        basket_link.click()

    def go_to_login_page(self) -> None:
        login_link = self.find_element_with_wait(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def is_disappeared(self, how, what, timeout=4) -> bool:
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_present(self, how, what, timeout=10) -> bool:
        try:
            self.find_element_with_wait(how, what, timeout)
        except NoSuchElementException:
            return False

        return True

    def is_not_element_present(self, how, what, timeout=4) -> bool:
        try:
            WebDriverWait(self.browser, timeout).\
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_element_contains_text(self, how, what, text, timeout=4) -> bool:
        try:
            WebDriverWait(self.browser, timeout).\
                until(EC.text_to_be_present_in_element((how, what), text))
        except TimeoutException:
            return False

        return True

    def open(self) -> None:
        self.browser.get(self.url)

    def should_be_authorized_user(self) -> None:
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            'User icon is not presented, probably unauthorised user'

    def should_be_login_link(self) -> None:
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            'Login link is not presented'
