from selenium.webdriver.common.by import By

from tests.conftest import driver


class AddNewCustomer:

    def __init__(self,driver):
        self.driver = driver

    linkCustomer_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    linkNewCustomer_css = "body > div:nth-child(3) > aside:nth-child(2) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > nav:nth-child(2) > ul:nth-child(1) > li:nth-child(4) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > p:nth-child(2)"
    linkaddnew_xpath = "//a[normalize-space()='Add new']"
    textbox_customeremail_xpath = "//input[@id='Email']"
    textbox_customerpwd_xpath = "//input[@id='Password']"
    textbox_FirstName_xpath = "//input[@id='FirstName']"
    textbox_LastName_xpath = "//input[@id='LastName']"
    gender_male_xpath = "//label[normalize-space()='Male']"
    gender_female_xpath = "//label[normalize-space()='Female']"
    dob_xpath = "//input[@id='DateOfBirth']"
    textbox_company_xpath = "//input[@id='Company']"
    linksave_xpath = "//button[@name='save']"
    msg_xpath = "//div[@class='alert alert-success alert-dismissable']"

    def clickCustomer(self):
        self.driver.find_element(By.XPATH,self.linkCustomer_xpath).click()

    def clicknewcustomer(self):
        self.driver.find_element(By.CSS_SELECTOR,self.linkNewCustomer_css).click()

    def clickaddnew(self):
        self.driver.find_element(By.XPATH,self.linkaddnew_xpath).click()

    def setCustomeremail(self,customeremail):
        self.driver.find_element(By.XPATH,self.textbox_customeremail_xpath).send_keys(customeremail)


    def setCustomerpassword(self,customerpassword):
        self.driver.find_element(By.XPATH,self.textbox_customerpwd_xpath).send_keys(customerpassword)

    def setFirstName(self,firstname):
        self.driver.find_element(By.XPATH,self.textbox_FirstName_xpath).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element(By.XPATH,self.textbox_FirstName_xpath).send_keys(lastname)

    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH,self.gender_male_xpath).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH, self.gender_female_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.gender_male_xpath).click()

    def setdob(self,dob):
        self.driver.find_element(By.XPATH, self.dob_xpath).send_keys(dob)

    def setcompany(self,company):
        self.driver.find_element(By.XPATH,self.textbox_company_xpath).send_keys(company)

    def clicksave(self):
        self.driver.find_element(By.XPATH,self.linksave_xpath).click()

    def print_msg(self):
        message=self.driver.find_element(By.XPATH,self.msg_xpath).text
        print(message)