from selenium.webdriver.common.by import By


class Check_out_page:
    def __init__(self, driver):
        self.driver = driver

    product_description = (By.CSS_SELECTOR, "p[class='pb-item']")

    def get_product_description(self):
        return self.driver.find_element(*Check_out_page.product_description).text
