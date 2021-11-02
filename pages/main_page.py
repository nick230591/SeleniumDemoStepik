from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def go_to_login_page(self):
        # переходим на страницу с логином
        login_link = self.find_element(MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        # существует ссылка на страницу с логином?
        result = self.is_element_present(*MainPageLocators.LOGIN_LINK)
        false_msg = "Login link not presented"
        return result, false_msg
