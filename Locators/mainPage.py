from selenium.webdriver.common.by import By

solutions_container = (By.CSS_SELECTOR, 'nav.nav-menu>div:first-of-type')
cases_container = (By.CSS_SELECTOR, 'nav.nav-menu>div:nth-of-type(2)')
resources_cointainer = (By.CSS_SELECTOR, 'nav.nav-menu>div:nth-of-type(3)')
pricing_container = (By.CSS_SELECTOR, 'nav.nav-menu>div:nth-of-type(4)')
company_container = (By.CSS_SELECTOR, 'nav.nav-menu>div:nth-of-type(5)')
support_container = (By.CSS_SELECTOR, 'a.navbarlink.menutext[href="https://support.scrive.com"]')
login_container = (By.CSS_SELECTOR, 'a.navbarlink.menutext[href="/en/enter"]')
language_container = (By.CSS_SELECTOR, 'div[id="flag-dropdown-toggle"]')
free_account_container = (By.CSS_SELECTOR, 'a.button-cta.navbar.w-button')