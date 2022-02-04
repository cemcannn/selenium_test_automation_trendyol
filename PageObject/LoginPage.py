from selenium.webdriver.common.by import By

from PageObject.MainPage import MainPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    userName = (By.CSS_SELECTOR, "input[id='login-email']")
    password = (By.CSS_SELECTOR, "input[id='login-password-input']")
    submit = (By.CSS_SELECTOR, "button[type='submit']")

    def getUserName(self):
        return self.driver.find_element(*LoginPage.userName)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def getSubmit(self):
        self.driver.find_element(*LoginPage.submit).click()
        mainPage = MainPage(self.driver)
        return mainPage

