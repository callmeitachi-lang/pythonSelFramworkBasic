from pageobjects.cartPage import CartPage
from pageobjects.homepage import Homepage

from utily.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class Teste2e(BaseClass):

    def test_one(self):
        log = self.getlogger()
        home_page = Homepage(self.driver)
        home_page.click_on_shop().click()
        log.info("Clicking on the shop link")
        cart_page = CartPage(self.driver)
        cart_page.add_product_to_cart()
        log.info("added product to cart")







