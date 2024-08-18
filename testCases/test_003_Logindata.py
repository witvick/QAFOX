import time

from selenium.webdriver.chrome import webdriver

from PageObjects.HomePage import Home
from PageObjects.AccountLoginPage import AccountLogPage
from PageObjects.my_account_page import MyAccount
from utlities import XLUtils
from utlities.readProperties import ReadConfig
from utlities.customlogger import LogGen
import os

class Test_Login_DDT():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Logger

    path = r"C:\Users\MR.WICK\PycharmProjects\QAFOX\testdata\QAfox_Logindata.xlsx"

    def test_login_ddt(self, setup):
        self.logger.info("**** Starting test_003_login_Datadriven *******")
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        lst_status = []

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = Home(self.driver)  # HomePage Page Object Class
        self.lp = AccountLogPage(self.driver)  # LoginPage Page Object Class
        self.ma = MyAccount(self.driver)  # MyAccount Page Object class

        for r in range(2, self.rows + 1):

            self.hp.Myaccounthp()

            time.sleep(5)
            self.hp.Login()
            # self.ma.Logout()

            self.email=XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.setEmail(self.email)
            self.lp.setpass(self.password)
            self.lp.Loginbutton()
            time.sleep(5)

            # self.targetpage=self.lp.get_confirmmsg()
            # if self.targetpage==True:
            # if self.targetpage == True:
            if self.exp == 'Valid':
                lst_status.append('Pass')
                time.sleep(5)
                self.ma.Logout()
                time.sleep(5)
                self.ma.Myaccount()
                time.sleep(10)

            elif self.exp == 'Invalid':
                lst_status.append('Fail')



        self.driver.close()
        print(lst_status)

        #final validation
        # if "Fail" not in lst_status:
        #     assert True
        # else:
        #     assert False
        # self.logger.info("******* End of test_003_login_Datadriven **********")
