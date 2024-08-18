import time
import pytest
from PageObjects.AccountRegistrationPage import AccountRegPage
from PageObjects.HomePage import Home
from utlities.customlogger import LogGen
from utlities.readProperties import ReadConfig


class TestAccountRegistrationPage:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # Ensure this line is executed

    def test_account_reg(self, setup):
        print("Logger:", self.logger)  # Debugging line
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("***test_001_account registration_started***")
        self.driver.maximize_window()

        self.hp = Home(self.driver)
        self.logger.info("clicking on my account")
        self.hp.Myaccount()
        self.logger.info("clicking on register")
        self.hp.Register()

        self.regpage = AccountRegPage(self.driver)
        self.logger.info("setting first name")
        self.regpage.setFirstname("BABU")
        self.logger.info("setting last name")
        self.regpage.setLastname("SHONA")
        self.regpage.setEmail(ReadConfig.getUseremail())
        self.regpage.setPhone("9899784875")
        self.regpage.setpass(ReadConfig.getPassword())
        self.regpage.setconfpass("BABU19985")
        time.sleep(5)
        self.regpage.agreebutton()
        time.sleep(5)
        self.regpage.continuebutton()
        time.sleep(5)
        self.confmsg = self.regpage.get_confirmmsg()

        if self.confmsg == "Your Account Has Been Created!":
            self.logger.info("*******registration PASSED*******")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(r"C:\Users\MR.WICK\PycharmProjects\QAFOX\screenshots\test_account_reg.png")
            assert False
        self.logger.info("*******registration completed*******")
