from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password) -> None:
        email_field, password_field, password_confirm_field, submit_button = \
            self.find_element_with_wait(*LoginPageLocators.REGISTER_FORM_EMAIL), \
            self.find_element_with_wait(*LoginPageLocators.REGISTER_FORM_PASSWORD), \
            self.find_element_with_wait(*LoginPageLocators.REGISTER_FORM_PASSWORD_CONFIRM), \
            self.find_element_with_wait(*LoginPageLocators.REGISTER_FORM_SUBMIT)

        email_field.send_keys(email)
        password_field.send_keys(password)
        password_confirm_field.send_keys(password)
        submit_button.click()

    def should_be_login_form(self) -> None:
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_login_page(self) -> None:
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self) -> None:
        assert 'login' in self.browser.current_url, 'Current URL does not contain "login"'

    def should_be_register_form(self) -> None:
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'
