from selenium.webdriver.common.by import By

from page_object.Check_out_page import Check_out_page


class Main_page:
    def __init__(self, driver):
        self.driver = driver

    search_bar = (By.CSS_SELECTOR, "input[class='search-box']")
    suggest = (By.LINK_TEXT, "Çocuk Bornoz")
    free_click = (By.XPATH, "/html")
    brand_filter = (By.CSS_SELECTOR, "input[class='fltr-srch-inpt'")
    brand_titles = (By.XPATH, "//div[@class='fltr-item-text']")
    rating_counts = (By.CSS_SELECTOR, "div[class*='p-card-wrppr'] a span[class='ratingCount']")
    link_basket = (By.CSS_SELECTOR, "a[class='link account-basket']")

    def get_search_bar(self):
        return self.driver.find_element(*Main_page.search_bar)

    def get_suggest(self):
        return self.driver.find_element(*Main_page.suggest).click()

    def get_free_click(self):
        return self.driver.find_element(*Main_page.free_click).click()

    def get_brand_filter(self):
        return self.driver.find_element(*Main_page.brand_filter)

    def get_brand_titles(self):
        return self.driver.find_elements(*Main_page.brand_titles)

    def get_rating_counts(self):
        return self.driver.find_elements(*Main_page.rating_counts)

    def get_link_basket(self):
        self.driver.find_element(*Main_page.link_basket).click()
        check_out_page = Check_out_page(self.driver)
        return check_out_page


