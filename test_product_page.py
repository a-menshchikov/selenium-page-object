import pytest

from pages.product_page import ProductPage

urls = [f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{n}' for n in range(10)]
urls[7] = pytest.param(urls[7], marks=pytest.mark.xfail)


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_success_messages()
