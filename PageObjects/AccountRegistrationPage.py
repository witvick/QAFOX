from selenium.webdriver import chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class AccountRegPage:
    firstname_xpath="// *[ @ id = 'input-firstname']"
    lastname_xpath = "// *[ @ id = 'input-lastname']"
    email_xpath = "//*[@id='input-email']"
    telephone_xpath = "//*[@id='input-telephone']"
    password_xpath = "// *[ @ id = 'input-password']"
    confirmpass_xpath = "//*[@id='input-confirm']"

    agree_terms_xpath="//*[@id='content']/form/div/div/input[1]"
    continue_button_xpath="//*[@id='content']/form/div/div/input[2]"

    header_txt="//*[@id='content']/h1"
    suceess_xpath="//*[@id='common-success']/ul/li[3]/a"

    #Your Account Has Been Created!


    def __init__(self, driver):
        self.driver = driver

    def setFirstname(self,fname):
        self.driver.find_element(By.XPATH, self.firstname_xpath).send_keys(fname)

    def setLastname(self,lname):
        self.driver.find_element(By.XPATH, self.lastname_xpath).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

    def setPhone(self,pno):
        self.driver.find_element(By.XPATH, self.telephone_xpath).send_keys(pno)

    def setpass(self,password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def setconfpass(self,confpass):
        self.driver.find_element(By.XPATH, self.confirmpass_xpath).send_keys(confpass)

    def agreebutton(self):
        self.driver.find_element(By.XPATH, self.agree_terms_xpath).click()

    def continuebutton(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()

    def get_confirmmsg(self):
        try:
            return self.driver.find_element(By.XPATH,self.header_txt).text
        except:
            None








