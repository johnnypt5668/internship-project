from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep
class FirstProductPage(Page):

    ARCHITECTURE_BUTTON = (By.ID, "w-tabs-0-data-w-tab-0")

    def verify_architecture_button_is_visible(self):
        self.verify_text('Architecture', *self.ARCHITECTURE_BUTTON)

    def verify_architecture_button_is_clickable(self):
        self.wait_until_clickable_click(self.ARCHITECTURE_BUTTON)

