"""Локаторы для поиска элементов на странице"""

from urllib.parse import urlparse, urlunparse
from selenium.webdriver.common.by import By


class MainPageLocators():
    """Локаторы для MainPage"""
    MAIN_URL = "http://selenium1py.pythonanywhere.com"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link2")

class LoginPageLocators():
    """Локаторы для LoginPage"""
    page_name = 'login'
    # LOGIN_URL = urlunparse(base_url_parse._replace(path=page_name))
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    """Локаторы для ProductPage"""
    PRODUCT_PAGE_URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCECC_ADD_TO_CART_MSG = (By.CSS_SELECTOR, ".alertinner > strong")
    SELECTED_PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    CART_PRICE_MSG = (By.CSS_SELECTOR, ".alert:nth-child(3) > .alertinner  strong")
    SELECTED_PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")