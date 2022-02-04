from selenium.webdriver.common.by import By

from PageObject.CheckOutPage import CheckOutPage


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    searchBar = (By.CSS_SELECTOR, "input[class='search-box']")
    suggest = (By.LINK_TEXT, "Çocuk Bornoz")
    freeClick = (By.XPATH, "/html")
    brandFilter = (By.CSS_SELECTOR, "input[class='fltr-srch-inpt'")
    brandTitles = (By.XPATH, "//div[@class='fltr-item-text']")
    ratingCounts = (By.CSS_SELECTOR, "div[class*='p-card-wrppr'] a span[class='ratingCount']")
    linkBasket = (By.CSS_SELECTOR, "a[class='link account-basket']")

    def getSearchBar(self):
        return self.driver.find_element(*MainPage.searchBar)

    def getSuggest(self):
        return self.driver.find_element(*MainPage.suggest).click()

    def getFreeClick(self):
        return self.driver.find_element(*MainPage.freeClick).click()

    def getBrandFilter(self):
        return self.driver.find_element(*MainPage.brandFilter)

    def getBrandTitles(self):
        return self.driver.find_elements(*MainPage.brandTitles)

    def getRatingCounts(self):
        return self.driver.find_elements(*MainPage.ratingCounts)

    def getLinkBasket(self):
        self.driver.find_element(*MainPage.linkBasket).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage


