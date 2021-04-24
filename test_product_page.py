from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product = product_page.find_product()
    product_price = product_page.find_product_price()
    product_page.add_to_basket()
    page.solve_quiz_and_get_code()
    product_page.alert_should_contain_product_name(product)
    product_page.alert_should_contain_price(product_price)
