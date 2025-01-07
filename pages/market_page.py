from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

class MarketPage(Page):

    FWD_MARKET_BTN = (By.CSS_SELECTOR, "a.pagination__button.w-inline-block")
    BACK_MARKET_BTN = (By.XPATH, "//div[@class='pagination__button']")
    CURRENT_MARKET_PAGE = (By.XPATH, "//div[@wized='currentPageMarket']")
    FINAL_MARKET_PAGE = (By.CSS_SELECTOR, "div[wized='totalPageMarket')]")
    DEVELOPERS_BUTTON = (By.CSS_SELECTOR, "div[wized='marketTagDevelopers']")
    LICENSE_BOX = (By.CSS_SELECTOR, "div[class='license-txt']")

    def verify_market_page_open(self):
        self.verify_partial_url('market-companies')

    def click_market_page_button(self):
        last_page = self.find_element(*self.FINAL_MARKET_PAGE)
        n = int(last_page.text)
        for button in range(1, n + 1):
            self.wait_until_clickable_click(self.FWD_MARKET_BTN)

    def click_market_back_page_button(self):
        self.wait_until_clickable_click(self.BACK_MARKET_BTN)

    def click_on_developers_button(self):
        self.wait_until_clickable_click(self.DEVELOPERS_BUTTON)
        sleep(5)

    def verify_license_appears_in_tags(self):
        tags = self.find_elements(*self.LICENSE_BOX)
        for tag in tags:
            self.verify_text('License', *self.LICENSE_BOX)