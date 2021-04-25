from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Empty basket message is not presented"      

    def basket_shouldnt_contain_item(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET), \
            "Basket contains items, but should not be"
