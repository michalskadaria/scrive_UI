import unittest
import HtmlTestRunner

from selenium import webdriver

from pages.loginPage import Loginpage

# DANE TESTOWE
username = "daria.michalska+qa@scrive.com"
password = "testerwsb2021"
incorrect_username = "daria.michalska+q@scrive.com"
incorrect_password = "testerwsb"

url = "https://staging.scrive.com/en/enter#log-in"


class ScriveLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def test_incorrect_email(self):
        driver = self.driver
        driver.get(url)

        loginpage = Loginpage(driver)
        assert loginpage.has_email_input()
        loginpage.fill_email_input(incorrect_username)

        assert loginpage.has_password_input()
        loginpage.fill_password_input(password)

        assert loginpage.has_login_button()
        loginpage.click_login_button()

        assert loginpage.has_error_message()

        def tearDown(self):
            self.driver.quit()

    def test_incorrect_password(self):
        driver = self.driver
        driver.get(url)

        loginpage = Loginpage(driver)
        assert loginpage.has_email_input()
        loginpage.fill_email_input(username)

        assert loginpage.has_password_input()
        loginpage.fill_password_input(incorrect_password)

        assert loginpage.has_login_button()
        loginpage.click_login_button()

        assert loginpage.has_error_message()

        def tearDown(self):
            self.driver.quit()

    def test_correct_login(self):
        driver = self.driver
        driver.get(url)

        loginpage = Loginpage(driver)
        assert loginpage.has_email_input()
        loginpage.fill_email_input(username)

        assert loginpage.has_password_input()
        loginpage.fill_password_input(password)

        assert loginpage.has_login_button()
        loginpage.click_login_button()

        assert loginpage.is_redirected_to_account_dashboard()

        def tearDown(self):
            self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))