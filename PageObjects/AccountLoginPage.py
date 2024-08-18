from selenium.webdriver import chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class AccountLogPage:
    email_xpath = "//*[@id='input-email']"
    password_xpath = "// *[ @ id = 'input-password']"
    login_button_xpath = "//*[@id='content']/div/div[2]/div/form/input"
    text_myaccount_xpath= "//*[@id='content']/h2[1]"
    #Your Account Has Been Created!


    def __init__(self, driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

    def setpass(self,password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def Loginbutton(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def get_confirmmsg(self):
        try:
            return self.driver.find_element(By.XPATH,self.text_myaccount_xpath).text
        except:
            None








