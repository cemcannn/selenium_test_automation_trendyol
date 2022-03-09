from selenium.webdriver.common.by import By

from page_object.Main_page import Main_page


class Login_page:
    def __init__(self, driver):
        self.driver = driver

    user_name = (By.CSS_SELECTOR, "input[id='login-email']")
    password = (By.CSS_SELECTOR, "input[id='login-password-input']")
    submit = (By.CSS_SELECTOR, "button[type='submit']")

    def get_user_name(self):
        return self.driver.find_element(*Login_page.user_name)

    def get_password(self):
        return self.driver.find_element(*Login_page.password)

    def get_submit(self):
        self.driver.find_element(*Login_page.submit).click()
        main_page = Main_page(self.driver)
        return main_page

