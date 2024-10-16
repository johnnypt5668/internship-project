from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait


class SecondaryPage(Page):
    # FWD_BTN = (By.XPATH, "//a[@wized='nextPageMLS']")
    # FWD_BTN = (By.XPATH, "//a[@href='https://soft.reelly.io/secondary-listings#']")
    FWD_BTN = (By.CSS_SELECTOR, "a.pagination__button.w-inline-block")
    BACK_BTN = (By.XPATH, "//div[@class='pagination__button']")
    FILTERS_TAB = (By.XPATH, "//div[@class='filter-text' and text()='Filters']")
    WANT_TO_SELL_TAB = (By.CSS_SELECTOR, "div[class='switcher-button active']")
    WANT_TO_BUY_TAB = (By.XPATH, "//div[@class='tag-text-filters' and text()='Want to buy']")
    APPLY_FILTER_BUTTON = (By.CSS_SELECTOR, "a[wized='applyFilterButtonMLS']")
    FOR_SALE_BOX = (By.CSS_SELECTOR, "div[class='listing-card']")
    FOR_SALE_TAG = (By.CSS_SELECTOR, "div[class='for-sale-block']")
    WANT_TO_BUY_TAG = (By.XPATH, "//div[@wized='saleTagMLS' and text()='Want to buy']")

    def verify_secondary_page_opened(self):
        self.verify_partial_url("secondary-listings")

    def click_page_button(self):
        self.wait_until_clickable_click(self.FWD_BTN)

    def click_back_page_button(self):
        self.wait_until_clickable_click(self.BACK_BTN)

    def click_filters_tab(self):
        self.wait_until_clickable_click(self.FILTERS_TAB)

    def click_want_to_sell_tab(self):
        self.wait_until_clickable_click(self.WANT_TO_SELL_TAB)

    def click_want_to_buy_tab(self):
        self.wait_until_clickable_click(self.WANT_TO_BUY_TAB)

    def click_apply_filter_button(self):
        self.wait_until_clickable_click(self.APPLY_FILTER_BUTTON)

    def verify_for_sale_tag_visible(self):
        for_sale_boxes = self.find_elements(*self.FOR_SALE_BOX)
        for_sale_tags = self.find_elements(*self.FOR_SALE_TAG)
        assert len(for_sale_tags) == len(for_sale_boxes), f"Expected {len(for_sale_boxes)}, got {len(for_sale_tags)}"

    def verify_want_to_buy_tag_visible(self):
        for_sale_boxes = self.find_elements(*self.FOR_SALE_BOX)
        want_to_buy_tags = self.find_elements(*self.WANT_TO_BUY_TAG)
        assert len(want_to_buy_tags) == len(for_sale_boxes), f"Expected {len(for_sale_boxes)}, got {len(want_to_buy_tags)}"