# product_count = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
#
# for products in product_count:
#     products.find_elements(By.XPATH, "//h4/a")
#     if products.text == "iphone X":
#         products.find_elements(By.XPATH, "//button").click()
from selenium.webdriver.common.by import By


class CartPage:
    product_count = (By.XPATH, "//div[@class='card h-100']")
    product_search = (By.XPATH, "//h4/a")
    add_to_cart = (By.XPATH, "//button")
    checkout = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    continueToCheckout = (By.CSS_SELECTOR, "button[class='btn btn-success']")


    def __init__(self,driver):
        self.driver = driver

    def add_product_to_cart(self):
        products = self.driver.find_elements(*CartPage.product_count)
        for product_number in products:
            product_number.find_elements(*CartPage.product_search)
            if product_number.text == "iphone X":
                product_number.find_elements(*CartPage.add_to_cart).click()
            self.driver.find_element(*CartPage.checkout).click()
            self.driver.find_element(*CartPage.continueToCheckout).click()


