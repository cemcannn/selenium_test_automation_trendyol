import time

from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    addBasket = (By.CSS_SELECTOR, "button[class='add-to-basket']")

    def getAddBasket(self):
        self.driver.find_element(*ProductPage.addBasket).click()
        time.sleep(1)
        return self.driver.close()
