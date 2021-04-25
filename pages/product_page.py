from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def find_product(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT)
        return product.text

    def find_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    def alert_should_contain_product_name(self, product_name):
        text_from_page = self.browser.find_element(*ProductPageLocators.ALERT_AFTER_ADDING_ABOUT_PRODUCT).text
        assert product_name == text_from_page, f"Alert doesn't contain '{product_name}'"

    def alert_should_contain_price(self, price):
        text_from_page = self.browser.find_element(*ProductPageLocators.ALERT_AFTER_ADDING_ABOUT_PRICE).text
        assert price == text_from_page, f"Alert doesn't contain '{price}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
               "Success message is presented, but should not be"
    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
               "Success message is presented, but should disappeared"
