import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.CheckoutPage import CheckOutPage
from PageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self, setup):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        #homePage.shopItems().click()
        checkoutpage = homePage.shopItems()
        cards = checkoutpage.getCardTitle()
        log.info(cards)
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            #print(cardText)
            if cardText == "iphone X":
        #products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        #for product in products:
            # print(product.find_element_by_xpath("div/h4/a").text)
        #    productName = product.find_element_by_xpath("div/h4/a").text
        #    if productName == "iphone X":
        #        print(product.find_element_by_xpath("div/h4/a").text)
                #self.driver.find_element_by_xpath("div/button[@class='btn btn-info']").click()
                checkoutpage.getCardFooter()[i].click()
        self.driver.find_element_by_xpath("//li[@class='nav-item active']/a").click()
        #self.driver.find_element_by_css_selector(".btn-success").click()
        confirmpage = checkoutpage.getCheckoutItems()
        log.info("Entering country name as ind")
        #self.driver.find_element_by_id("country").send_keys("Ind")
        confirmpage.getCountry().send_keys("Ind")

        #wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifyLinkPresence("India")

        #self.driver.find_element_by_link_text("India").click()
        confirmpage.getSelectCountry().click()
        #self.driver.find_element_by_css_selector(".btn-success").click()
        confirmpage.getCheckOutOrder().click()

        #message = self.driver.find_element_by_css_selector(".alert-dismissible").text
        message = confirmpage.getSuccessMessage().text
        print(message)
        successMessage = "Success! Thank you! Your order will be delivered in next few weeks :-)."
        log.info("Text received from application is " +message)
        assert successMessage in message

        self.driver.save_screenshot("screenShoot.png")
