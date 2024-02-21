from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver



    textbox_name_id = "Email"
    textbox_password_id = "Password"
    button_login_css = "button[type='submit']"
    button_logout_linktext="Logout"


    def setUsername(self,username):
        self.driver.find_element(By.ID,self.textbox_name_id).clear()
        self.driver.find_element(By.ID,self.textbox_name_id).send_keys(username)


    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_login_css).click()

    def clicklogout(self):
        self.driver.find_element(By.LINK_TEXT,self.button_logout_linktext).click()

