from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    Country = (By.ID, "country")
    selectCountry = (By.LINK_TEXT, "India")
    checkOutOrder = (By.CSS_SELECTOR, ".btn-success")
    successMessage = (By.CSS_SELECTOR, ".alert-dismissible")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.Country)

    def getSelectCountry(self):
        return self.driver.find_element(*ConfirmPage.selectCountry)

    def getCheckOutOrder(self):
        return self.driver.find_element(*ConfirmPage.checkOutOrder)

    def getSuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.successMessage)
