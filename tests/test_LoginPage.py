import pytest
import selenium
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
class Test_001_LoginPage():
    username=ReadConfig.getUsername()
    password=ReadConfig.getpassword()
    logger=LogGen.loggen()
    def test_homepage(self,setup):
        self.logger.info("--------Verifying Home page Title---")
        page_title = self.driver.title
        if page_title == "Your store. Login":
            assert True
            self.logger.info("--------Passed verify Home page test cases---")

        else:
            assert False
            self.logger.info("--------Test Case1:Failed.....---")



    def test_Login(self,setup):
        self.logger.info("--------Opening Log In Page---")
        lp = LoginPage(self.driver)
        self.logger.info("--------Entering Username ---")
        lp.setUsername(self.username)
        self.logger.info("--------Entering Password---")
        lp.setPassword(self.password)
        lp.clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("--------Test Case2:Passed.....---")

        else:
            assert False
            self.logger.info("--------Test Case2:Failed.....---")

        lp.clicklogout()


