import pytest
import time

from src.pages.product_page import ProductPage
from src.pages.locators import ProductPageLocators

product_base_link = ProductPageLocators.PRODUCT_PAGE_URL
urls = [f'{product_base_link}/?promo=offer{num}' for num in range(10)]
@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    """Пользователь может добавить товар в корзину"""
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    result = page.should_be_add_to_cart_msg()[0].text == page.should_be_selected_product_name()[0].text
    assert result, "Selected product not equal product in cart"
    result = page.should_be_cart_price_msg()[0].text == page.should_be_selected_product_price()[0].text
    assert result, "Price of selected product not equal price of product in cart"

def test_guest_can_see_success_message_after_adding_product_to_basket(browser):
    """После добавления товара в корзину - появляется всплывающее сообщение"""
    link = ProductPageLocators.PRODUCT_PAGE_URL
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    result, msg = page.should_be_add_to_cart_msg()
    assert result, msg
    
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Всплывающее сообщение НЕ появляется если НЕ добавлять товар в корзину"""
    link = ProductPageLocators.PRODUCT_PAGE_URL
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    result, msg = page.is_not_cart_msg_present()
    assert result, msg



