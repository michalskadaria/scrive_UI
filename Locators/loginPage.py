from selenium.webdriver.common.by import By

scrive_logo = (By.CSS_SELECTOR, 'div.logo-wrapper')
email_input = (By.CSS_SELECTOR, 'input[name="email"]')
password_input = (By.CSS_SELECTOR, 'input[name="password"]')
login_button = (By.CSS_SELECTOR, 'span[data-reactid=".0.1.0.3.0.0.1"]')
login_with_sso_button = (By.CSS_SELECTOR, 'span[data-reactid=".0.1.0.4.0.0.1"]')
sign_up_link = (By.CSS_SELECTOR, 'a[class="put-link-to-signup-here"]')
language_box = (By.CSS_SELECTOR, 'div[class="select-button"]')
error_msg = (By.CSS_SELECTOR), 'div[class="flash-body"]'
login_box = (By.CSS_SELECTOR, 'div[class="login-box"]')
