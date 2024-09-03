from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class UserGuidePage(Page):

    def verify_user_guide_page_opened(self):
        self.verify_partial_url('user-guide')