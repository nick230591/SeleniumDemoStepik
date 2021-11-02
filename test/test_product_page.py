import pytest
import time

from pages.product_page import ProductPage
from pages.locators import ProductPageLocators

product_base_link = ProductPageLocators.PRODUCT_PAGE_URL
urls = [f'{product_base_link}/?promo=offer{num}' for num in range(10)]
@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()

    assert page.should_be_add_to_cart_msg().text == page.should_be_selected_product_name().text
    assert page.should_be_cart_price_msg().text == page.should_be_selected_product_price().text
