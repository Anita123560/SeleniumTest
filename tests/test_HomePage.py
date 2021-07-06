import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from PageObject.HomePage import HomePage
from TestData.HomePageData import HomePageData

from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        #log.info("first name is "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getPassword().send_keys(getData["password"])
        self.selectOptionByText(homepage.getGendder(), getData["gender"])
        homepage.getSubmitForm().click()
        alertText = homepage.getSuccessMessage().text
        assert "success" in alertText
        self.driver.refresh()



    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param