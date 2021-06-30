import time
import unittest
import HtmlTestRunner

from selenium import webdriver

from pages.mainPage import Mainpage

url = "https://staging.scrive.com/"

class MainPageToLoginRedirect(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_login_redirect_main_page(self):
        self.driver.get(url)

        mainpage = Mainpage(self.driver)
        assert mainpage.has_login_button()
        mainpage.click_login_button()
        time.sleep(5)
        assert mainpage.is_redirected_to_login_page()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))