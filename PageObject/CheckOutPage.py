from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    productDescription = (By.CSS_SELECTOR, "p[class='pb-item']")

    def getProductDescription(self):
        return self.driver.find_element(*CheckOutPage.productDescription).text
