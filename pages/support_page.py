from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class SupportPage(Page):

    def verify_support_page_opened(self):
        self.verify_partial_url('api.whatsapp.com')

    def verify_news_page_opened(self):
        self.verify_partial_url('t.me/reellydxb')


    def switch_back_to_settings(self):
        self.driver.close()
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[0])