from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

class MarketPage(Page):

    FWD_MARKET_BTN = (By.CSS_SELECTOR, "a.pagination__button.w-inline-block")
    BACK_MARKET_BTN = (By.XPATH, "//div[@class='pagination__button']")

    def verify_market_page_open(self):
        self.verify_partial_url('market-companies')

    def click_market_page_button(self):
        self.wait_until_clickable_click(self.FWD_MARKET_BTN)

    def click_market_back_page_button(self):
        self.wait_until_clickable_click(self.BACK_MARKET_BTN)