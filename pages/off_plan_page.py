from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep
class OffPlanPage(Page):

    FWD_OP_BTN = (By.CSS_SELECTOR, "a.pagination__button.w-inline-block")
    BACK_OP_BTN = (By.XPATH, "//div[@class='pagination__button']")
    TOTAL_PAGES = (By.CSS_SELECTOR, '[wized="totalPageProperties"]')

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