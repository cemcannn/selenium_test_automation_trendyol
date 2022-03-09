from selenium.webdriver.common.by import By


class Home_page:
    def __init__(self, driver):
        self.driver = driver

    login_menu = (By.CSS_SELECTOR, "p[class='link-text']")
    login_sub_menu = (By.CSS_SELECTOR, "div[class='login-button']")

    def get_login_menu(self):
        return self.driver.find_element(*Home_page.login_menu)

    def get_login_sub_menu(self):
        return self.driver.find_element(*Home_page.login_sub_menu)

