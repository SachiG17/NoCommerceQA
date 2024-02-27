import time

from pageObjects.AddNewCustomer import AddNewCustomer
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test004_addNewCustomer():
    username = ReadConfig.getUsername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    def test_searchCustomer(self,setup):
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