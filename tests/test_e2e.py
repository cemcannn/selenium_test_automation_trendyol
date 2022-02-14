import time

import pytest
from selenium.webdriver.common.by import By

from page_object.Home_page import Home_page
from page_object.Login_page import Login_page
from page_object.Product_page import Product_page
from test_data.Login_data import Login_data
from utilities.Base_class import Base_class


class TestOne(Base_class):
    def test_e2e(self, get_data):
        log = self.get_logger()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, "path[id='Combined-Shape']").click()
        home_page = Home_page(self.driver)
        self.action_move_to_element(home_page.get_login_menu()).perform()
        self.action_move_to_element(home_page.get_login_sub_menu()).click().perform()
        login_page = Login_page(self.driver)
        login_page.get_user_name().send_keys(get_data["userName"])
        login_page.get_password().send_keys(get_data["password"])
        log.info("Giriş yapılıyor.")
        main_page = login_page.get_submit()
        time.sleep(2)
        main_page.get_search_bar().send_keys(get_data["searchBar"])
        main_page.get_suggest()
        # mouse click on blank area for pass pop-up
        main_page.get_free_click()
        main_page.get_brand_filter().send_keys(get_data["brandFilter"])
        brands = main_page.get_brand_titles()
        for brand in brands:
            if brand.text == "English Home":
                # //div[@class='fltr-item-text']/parent::a/div[@class='chckbox']
                log.info("Ürün filtrelemesi yapılıyor.")
                brand.find_element(By.XPATH, "parent::a/div[@class='chckbox']").click()

        time.sleep(2)
        rating_list = []
        products = main_page.get_rating_counts()
        for product in products:
            rating_list.append(product.text)
            if product.text == max(rating_list):
                log.info("Ürün sayfasına gidiliyor.")
                product.click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        product_page = Product_page(self.driver)
        log.info("Ürün sepete ekleniyor.")
        product_page.get_add_basket()
        self.driver.switch_to.window(self.driver.window_handles[0])
        check_out_page = main_page.get_link_basket()
        log.info("Ürün açıklaması " + check_out_page.get_product_description())
        assert "Dinosaurs Kadife Çocuk Bornoz 8-10 Yaş Yeşil" in check_out_page.get_product_description()

    @pytest.fixture(params=Login_data.test_e2e_data)
    def getData(self, request):
        return request.param







