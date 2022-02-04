from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    loginMenu = (By.CSS_SELECTOR, "p[class='link-text']")
    loginSubMenu = (By.CSS_SELECTOR, "div[class='login-button']")

    def getLoginMenu(self):
        return self.driver.find_element(*HomePage.loginMenu)

    def getLoginSubMenu(self):
        return self.driver.find_element(*HomePage.loginSubMenu)

