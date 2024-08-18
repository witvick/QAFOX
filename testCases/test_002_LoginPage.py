import time
import pytest
from PageObjects.HomePage import Home
from utlities.customlogger import LogGen
from utlities.readProperties import ReadConfig
from PageObjects.AccountLoginPage import AccountLogPage


class TestAccountLoginPage:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Ensure this line is executed

    def test_account_login(self, setup):
        print("Logger:", self.logger)  # Debugging line
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("***test_001_account Login_started***")
        self.driver.maximize_window()

        self.hp = Home(self.driver)
        self.logger.info("clicking on my account")
        self.hp.Myaccounthp()
        self.logger.info("clicking on Login")
        self.hp.Login()

        self.logpage = AccountLogPage(self.driver)
        self.logpage.setEmail(ReadConfig.getUseremail())
        self.logpage.setpass(ReadConfig.getPassword())

        time.sleep(5)
        self.logpage.Loginbutton()

        time.sleep(5)
        self.confmsg = self.logpage.get_confirmmsg()

        if self.confmsg == "My Account":
            self.logger.info("*******registration PASSED*******")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(r"C:\Users\MR.WICK\PycharmProjects\QAFOX\screenshots\test_account_login.png")
            assert False
        self.logger.info("*******registration completed*******")
