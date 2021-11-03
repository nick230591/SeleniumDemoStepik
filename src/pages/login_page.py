from urllib.parse import urlparse, urlunparse

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        # проверка login page по нескольким параметрам
        check_func_arr = [
            self.should_be_login_url, 
            self.should_be_login_form,
            self.should_be_register_form
        ]
        for check_func in check_func_arr:
            result, msg = check_func()
            if not result:
                return False, f"It is not Login Page, becouse: {msg}"
        return True, ""

    def should_be_login_url(self):
        # проверка корректности url адреса
        result = LoginPageLocators.page_name in self.browser.current_url
        false_msg = "Login URL not presented"
        return result, false_msg 
        

    def should_be_login_form(self):
        # существует форма логина на странице?
        result = self.is_element_present(LoginPageLocators.LOGIN_FORM)
        false_msg = "Login Form not presented"
        return result, false_msg
                

    def should_be_register_form(self):
        # существует форма регистрации на странице?
        result = self.is_element_present(LoginPageLocators.REGISTER_FORM)
        false_msg = "Register Form not presented"
        return result, false_msg 
    