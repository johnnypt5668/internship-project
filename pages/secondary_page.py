from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait


class SecondaryPage(Page):
    # FWD_BTN = (By.XPATH, "//a[@wized='nextPageMLS']")
    # FWD_BTN = (By.XPATH, "//a[@href='https://soft.reelly.io/secondary-listings#']")
    FWD_BTN = (By.CSS_SELECTOR, "a.pagination__button.w-inline-block")

    BACK_BTN = (By.XPATH, "//div[@class='pagination__button']")

    def verify_secondary_page_opened(self):
        self.verify_partial_url("secondary-listings")

    def click_page_button(self):
        self.wait_until_clickable_click(self.FWD_BTN)

    def click_back_page_button(self):
        self.wait_until_clickable_click(self.BACK_BTN)
