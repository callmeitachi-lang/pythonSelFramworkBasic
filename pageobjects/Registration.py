import time

from selenium.webdriver.common.by import By


class Registration:

    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.CSS_SELECTOR, "input[type='password']")
    checkbox = (By.ID, "exampleCheck1")
    submitButton = (By.CSS_SELECTOR, "input[value='Submit']")
    successMesg =(By.XPATH, "/html/body/app-root/form-comp/div/div[2]/div/strong")

    def __init__(self, driver):
        self.driver = driver

    def set_name(self):
        return self.driver.find_element(*Registration.name)

    def set_email(self):
        return self.driver.find_element(*Registration.email)

    def set_password(self):
        return self.driver.find_element(*Registration.password)

    def click_checkbox(self):
        return self.driver.find_element(*Registration.checkbox)

    def submit_button(self):
        return self.driver.find_element(*Registration.submitButton).click()



