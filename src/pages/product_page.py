from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        # нажимаем на кнопку - "Добавить в корзину"
        add_cart_btn = self.find_element(ProductPageLocators.ADD_TO_CART_BTN)
        add_cart_btn.click()
    
    def should_be_add_to_cart_msg(self):
        """Присутствует сообщение об успешном добавлении товара в корзину?"""
        result = self.find_element(ProductPageLocators.SUCCECC_ADD_TO_CART_MSG)
        false_msg = "Add_to_cart message NOT presented"
        return result, false_msg
    
    def should_be_selected_product_name(self):
        """Присутствует название выбранного товара?"""
        result = self.find_element(ProductPageLocators.SELECTED_PRODUCT_NAME)
        false_msg = "Product_name NOT presented"
        return result, false_msg 
    
    def should_be_cart_price_msg(self):
        """Присутствует цена товаров в корзине?"""
        result = self.find_element(ProductPageLocators.CART_PRICE_MSG)
        false_msg = "Cart_price_msg NOT presented"
        return result, false_msg  
    
    def should_be_selected_product_price(self):
        """Присутствует цена выбранного товара?"""
        result = self.find_element(ProductPageLocators.SELECTED_PRODUCT_PRICE)
        false_msg = "Selected_product_price NOT presented"
        return result, false_msg 

    def is_not_cart_msg_present(self):
        """Сообщение о добавлении товара в корзину отсутствует"""
        result = self.is_not_element_present(ProductPageLocators.SUCCECC_ADD_TO_CART_MSG)
        false_msg = "Add_to_cart_msg is present! But should NOT!"
        return result, false_msg
