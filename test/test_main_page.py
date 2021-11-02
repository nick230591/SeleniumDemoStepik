from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.locators import MainPageLocators

def test_guest_can_go_to_login_page(browser):
    link = MainPageLocators.MAIN_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    result, msg = login_page.should_be_login_page()
    assert result, msg

def test_guest_should_see_login_link(browser):
    link = MainPageLocators.MAIN_URL
    page = MainPage(browser, link)
    page.open()
    result, msg = page.should_be_login_link()
    assert result, msg