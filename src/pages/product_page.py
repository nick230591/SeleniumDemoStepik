from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        # нажимаем на кнопку - "Добавить в корзину"
        add_cart_btn = self.find_element(ProductPageLocators.ADD_TO_CART_BTN)
        add_cart_btn.click()
    
    def should_be_add_to_cart_msg(self):
        """Присутствует сообщение об успешном добавлении товара в корзину?"""
        return self.find_element(ProductPageLocators.SUCCECC_ADD_TO_CART_MSG)
    
    def should_be_selected_product_name(self):
        """Присутствует название выбранного товара?"""
        return self.find_element(ProductPageLocators.SELECTED_PRODUCT_NAME)
    
    def should_be_cart_price_msg(self):
        """Присутствует цена товаров в корзине?"""
        return self.find_element(ProductPageLocators.CART_PRICE_MSG)
    
    def should_be_selected_product_price(self):
        """Присутствует цена выбранного товара?"""
        return self.find_element(ProductPageLocators.SELECTED_PRODUCT_PRICE)