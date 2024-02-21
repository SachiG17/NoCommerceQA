import pytest
import selenium
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test_001_LoginPage():
    username="admin@yourstore.com"
    password="admin"

    def test_homepage(self,setup):
        page_title = self.driver.title
        if page_title == "Your store. Login":
            assert True
        else:
            assert False


    def test_Login(self,setup):
        lp = LoginPage(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False

        lp.clicklogout()


