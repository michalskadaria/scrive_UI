from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Locators.loginPage import *
from Locators.homePage import *


class Loginpage(object):
    def __init__(self, driver):
        self.driver = driver

    def has_email_input(self):
        emailInput = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(email_input))
        return emailInput is not None

    def fill_email_input(self, username):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(email_input)).send_keys(username)

    def has_password_input(self):
        passwordInput = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(password_input))
        return passwordInput is not None

    def fill_password_input(self, password):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(password_input)).send_keys(password)

    def has_login_button(self):
        loginButton = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(login_button))
        return loginButton is not None

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(login_button)).click()

    def has_error_message(self):
        errorMessageElement = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(error_msg))
        assert errorMessageElement is not None

        return errorMessageElement.text == "Incorrect email or password."

    def is_redirected_to_account_dashboard(self):
        startNewProcess = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(start_new_process))
        return startNewProcess is not None