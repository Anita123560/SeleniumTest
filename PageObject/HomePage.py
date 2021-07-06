from selenium.webdriver.common.by import By

from PageObject.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.CSS_SELECTOR, "input[id='exampleInputPassword1']")
    gender = (By.ID, "exampleFormControlSelect1")
    submitform = (By.XPATH, "//input[@type='submit']")
    successmessage = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage
        # self.driver.find_element_by_css_selector("a[href*='shop']")
    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getGendder(self):
        return self.driver.find_element(*HomePage.gender)

    def getSubmitForm(self):
        return self.driver.find_element(*HomePage.submitform)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successmessage)