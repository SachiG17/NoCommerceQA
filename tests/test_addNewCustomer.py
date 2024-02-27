import random
import string
import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.AddNewCustomer import AddNewCustomer
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig





class Test003_addNewCustomer():
    username = ReadConfig.getUsername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addnewCustomer(self,setup):
        # self.logger.info("--------Opening Log In Page---")
        lp = LoginPage(self.driver)
        # self.logger.info("--------Entering Username ---")
        lp.setUsername(self.username)
        # self.logger.info("--------Entering Password---")
        lp.setPassword(self.password)
        lp.clicklogin()
        self.logger.info("------Logged IN---")

        time.sleep(5)
        cp = AddNewCustomer(self.driver)
        cp.clickCustomer()
        time.sleep(5)
        cp.clicknewcustomer()
        cp.clickaddnew()
        self.email = random_generator() + "@gmail.com"
        cp.setCustomeremail(self.email)
        cp.setCustomerpassword("test123")
        cp.setFirstName("Sachin")
        cp.setLastName("Shetty")
        cp.setGender("Male")
        cp.setdob("2/13/2024")
        cp.clicksave()

        time.sleep(5)


        self.logger.info("-------Customer Saved------")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))