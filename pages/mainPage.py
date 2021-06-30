from selenium.webdriver.support.ui import WebDriverWait
from Locators.mainPage import *
from Locators.loginPage import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys


class Mainpage(object):
    def __init__(self, driver):
        self.driver = driver

    def has_login_button(self):
        loginContainer = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(login_container))
        return loginContainer is not None

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(login_container)).click()

    def is_redirected_to_login_page(self):
        loginBox = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(login_box))
        return loginBox is not None
