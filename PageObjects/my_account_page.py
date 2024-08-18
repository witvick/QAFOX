from selenium.webdriver import chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
class MyAccount:
# MyAccount
    lnk_logout__xpath = "//*[@id='column-right']/div/a[13]"
    my_account_xpath = "//*[@id='column-right']/div/a[4]"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # ACTION METHODS
    def Myaccount(self):
        self.driver.find_element(By.XPATH,self.my_account_xpath).click()
    def Logout(self):
        self.driver.find_element(By.XPATH, self.lnk_logout__xpath).click()
