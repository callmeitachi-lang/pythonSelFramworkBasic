from selenium.webdriver.common.by import By


class Homepage:

    # to use the driver from the test we need to call it in our constructor
    shop = (By.LINK_TEXT, "Shop")

    def __init__(self, driver):
        self.driver = driver

    def click_on_shop(self):
        return self.driver.find_element(*Homepage.shop)

# * python will consider this as a tuple hence its necessary to add it
