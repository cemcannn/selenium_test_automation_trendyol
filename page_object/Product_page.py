import time

from selenium.webdriver.common.by import By


class Product_page:
    def __init__(self, driver):
        self.driver = driver

    add_basket = (By.CSS_SELECTOR, "button[class='add-to-basket']")

    def get_add_basket(self):
        self.driver.find_element(*Product_page.add_basket).click()
        time.sleep(1)
        return self.driver.close()
