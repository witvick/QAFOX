from selenium.webdriver import chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
class Home:
                                        # Locators

                                        # MyAccount
    lnk_myaccount__xpath = "/html/body/footer/div/div/div[4]/ul/li[1]/a"
                                        # Register
    lnk_register_xpath = "//*[@id='column-right']/div/a[2]"
                                         # login
    box_login_xpath = "//*[@id='column-right']/div/a[1]"
    # # login button
    # button_login_xpath = "//*[@id='customer_login']/div[1]/form/p[3]/input[3]"
    # # Register password
    # box_password_xpath = "//*[@id='reg_password']"
    # # register button
    # button_register_xpath = "//*[@id='customer_login']/div[2]/form/p[3]/input[3]"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # ACTION METHODS

    def Myaccounthp(self):
        self.driver.find_element(By.XPATH, self.lnk_myaccount__xpath).click()

    def Register(self):
        self.driver.find_element(By.XPATH, self.lnk_register_xpath).click()

    def Login(self):
        self.driver.find_element(By.XPATH, self.box_login_xpath).click()
