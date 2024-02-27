from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities import ExcelUtils
import time
import pytest
class Test_002_DTT_LoginPage():
    path=".//TestData//LoginData.xlsx"
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_Login_ddt(self,setup):
        self.logger.info("---Loading DTT Test Login ----")
        self.logger.info("--------Opening Log In Page---")
        lp = LoginPage(self.driver)
        self.rows=ExcelUtils.getRowCount(self.path,"Sheet1")
        self.columns=ExcelUtils.getColumnCount(self.path,"Sheet1")
        lst_status=[]

        for r in range(2,self.rows+1):
            self.user=ExcelUtils.readData(self.path,"Sheet1",r,1)
            self.password=ExcelUtils.readData(self.path,"Sheet1",r,2)
            self.exp=ExcelUtils.readData(self.path,"Sheet1",r,3)
            lp.setUsername(self.user)
            lp.setPassword(self.password)
            lp.clicklogin()
            time.sleep(5)
            act_title = self.driver.title
            if act_title == "Dashboard / nopCommerce administration":
                if self.exp == "Pass":
                    print(r)
                    self.logger.info("-----Logged In ---")
                    lp.clicklogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("-----Failed---")
                    lp.clicklogout()
                    lst_status.append("Pass")
            elif act_title != "Dashboard / nopCommerce administration":
                if self.exp == "Pass":
                    self.logger.info("-----Failed---")
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("-----Passed---")
                    lst_status.append("Pass")




        if "Fail" not in lst_status:
            self.logger.info("----LOG IN DTT Passed")

        else:
            self.logger.info("Log In Failed")





