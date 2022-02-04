import time

import pytest
from selenium.webdriver.common.by import By

from PageObject.HomePage import HomePage
from PageObject.LoginPage import LoginPage
from PageObject.ProductPage import ProductPage
from TestData.LoginData import LoginData
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self, getData):
        log = self.getLogger()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, "path[id='Combined-Shape']").click()
        homePage = HomePage(self.driver)
        self.actionMoveToElement(homePage.getLoginMenu()).perform()
        self.actionMoveToElement(homePage.getLoginSubMenu()).click().perform()
        loginPage = LoginPage(self.driver)
        loginPage.getUserName().send_keys(getData["userName"])
        loginPage.getPassword().send_keys(getData["password"])
        log.info("Giriş yapılıyor.")
        mainPage = loginPage.getSubmit()
        time.sleep(2)
        mainPage.getSearchBar().send_keys(getData["searchBar"])
        mainPage.getSuggest()
        # mouse click on blank area for pass pop-up
        mainPage.getFreeClick()
        mainPage.getBrandFilter().send_keys(getData["brandFilter"])
        brands = mainPage.getBrandTitles()
        for brand in brands:
            if brand.text == "English Home":
                # //div[@class='fltr-item-text']/parent::a/div[@class='chckbox']
                log.info("Ürün filtrelemesi yapılıyor.")
                brand.find_element(By.XPATH, "parent::a/div[@class='chckbox']").click()

        time.sleep(2)
        rating_list = []
        products = mainPage.getRatingCounts()
        for product in products:
            rating_list.append(product.text)
            if product.text == max(rating_list):
                log.info("Ürün sayfasına gidiliyor.")
                product.click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        productPage = ProductPage(self.driver)
        log.info("Ürün sepete ekleniyor.")
        productPage.getAddBasket()
        self.driver.switch_to.window(self.driver.window_handles[0])
        checkOutPage = mainPage.getLinkBasket()
        log.info("Ürün açıklaması " + checkOutPage.getProductDescription())
        assert "Dinosaurs Kadife Çocuk Bornoz 8-10 Yaş Yeşil" in checkOutPage.getProductDescription()

    @pytest.fixture(params=LoginData.test_e2e_data)
    def getData(self, request):
        return request.param







