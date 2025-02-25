from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep
class OffPlanPage(Page):

    FWD_OP_BTN = (By.CSS_SELECTOR, "a.pagination__button.w-inline-block")
    BACK_OP_BTN = (By.XPATH, "//div[@class='pagination__button']")
    TOTAL_PAGES = (By.CSS_SELECTOR, '[wized="totalPageProperties"]')
    #OFF_PLAN_FILTERS_TAB = (By.XPATH, "//div[@class='filter-text' and text()='Filters']")
    OFF_PLAN_FILTERS_TAB = (By.CSS_SELECTOR, '[class="points-block-game"] [wized="openFiltersWindow"]')
    #OFF_PLAN_FILTERS_TAB = (By.XPATH, "//a[@wized='
    OFF_PLAN_FROM_PRICE_BOX = (By.CSS_SELECTOR, "input[wized='unitPriceFromFilter']")
    OFF_PLAN_TO_PRICE_BOX = (By.CSS_SELECTOR, "input[wized='unitPriceToFilter']")
    APPLY_OFF_PLAN_FILTER_BUTTON = (By.CSS_SELECTOR, "a[wized='applyFilterButton']")
    OFF_PLAN_FOR_SALE_BOX = (By.CSS_SELECTOR, "a[wized='cardOfProperty']")
    OFF_PLAN_TITLE_BOX = (By.CLASS_NAME, "project-name")
    OFF_PLAN_IMAGE_BOX = (By.CLASS_NAME, "project-image")
    OFF_PLAN_STATUS_BOX = (By.CSS_SELECTOR, "div[wized='projectStatus'")
    FIRST_PRODUCT = (By.CLASS_NAME, "project-image")



    def verify_off_plan_page_opened(self):
        self.verify_url('https://soft.reelly.io/')
        sleep(5)

    def click_off_page_forward_button(self):
        self.wait_until_clickable_click(self.FWD_OP_BTN)
        sleep(2)

    def go_to_last_pagination(self):
        self.total_pages = self.find_element(*self.TOTAL_PAGES).text
        print(self.total_pages)
        for page in range(1, int(self.total_pages)):
            self.click_off_page_forward_button()
            sleep(2)


    def click_off_page_back_page_button(self):
        self.wait_until_clickable_click(self.BACK_OP_BTN)
        sleep(2)

    def go_to_first_pagination(self):
        for page in range(1, int(self.total_pages)):
            self.click_off_page_back_page_button()
            sleep(2)

    def click_off_plan_filters_button(self):
        #off_plan_filter = self.find_element(*self.OFF_PLAN_FILTERS_TAB)
        self.wait_until_clickable_click(self.OFF_PLAN_FILTERS_TAB)

    def input_off_plan_from_price(self, from_price):
        self.input_text("1200000", *self.OFF_PLAN_FROM_PRICE_BOX)

    def input_off_plan_to_price(self, to_price):
        self.input_text("2000000", *self.OFF_PLAN_TO_PRICE_BOX)
        sleep(5)

    def click_off_plan_apply_filter_button(self):
        self.wait_until_clickable_click(self.APPLY_OFF_PLAN_FILTER_BUTTON)

    def verify_off_plan_price_in_range(self):
        from_value = 1200000
        to_value = 2000000
        sale_prices = self.find_elements(By.XPATH,  "//div[@class='price-value']")
        price_box = self.find_elements(By.CSS_SELECTOR, '.name-object-block')

        for price in sale_prices:
            price_text = price.text.replace("AED", "").replace(",", "").strip()
            assert from_value <= int(price_text) <= to_value, f"Expected price to be between {from_value} and {to_value}, got {price_text}"

    def verify_off_plan_cards_have_titles(self):
        for_sale_boxes = self.find_elements(*self.OFF_PLAN_FOR_SALE_BOX)
        off_plan_title_box = self.find_elements(*self.OFF_PLAN_TITLE_BOX)
        assert len(off_plan_title_box) == len(for_sale_boxes), f"Expected {len(for_sale_boxes)}, got {len(off_plan_title_box)}"

    def verify_off_plan_cards_have_images(self):
        for_sale_boxes = self.find_elements(*self.OFF_PLAN_FOR_SALE_BOX)
        off_plan_image_box = self.find_elements(*self.OFF_PLAN_IMAGE_BOX)
        assert len(off_plan_image_box) == len(for_sale_boxes), f"Expected {len(for_sale_boxes)}, got {len(off_plan_image_box)}"

    #def verify_for_sale_tag_visible(self):
    #    for_sale_boxes = self.find_elements(*self.FOR_SALE_BOX)
    #    for_sale_tags = self.find_elements(*self.FOR_SALE_TAG)
    #    assert len(for_sale_tags) == len(for_sale_boxes), f"Expected {len(for_sale_boxes)}, got {len(for_sale_tags)}"
    def select_out_of_stock_dropdown(self):
        dropdown_menu = self.find_element(By.ID, "Location-2")
        select = Select(dropdown_menu)
        select.select_by_value('Out of stock')
        sleep(5)

    def verify_out_of_stock_tage_appears_in_boxes(self):
        boxes = self.find_elements(*self.OFF_PLAN_FOR_SALE_BOX)
        for box in boxes:
            self.verify_text('Out of stock', *self.OFF_PLAN_STATUS_BOX)

    def click_on_first_product(self):
        self.wait_until_clickable_click(self.FIRST_PRODUCT)

   