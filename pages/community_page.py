from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class CommunityPage(Page):

    #SUPPORT_BUTTON = (By.XPATH, "//a[@class='chat-button w-button' and text()='Contact support']")
    SUPPORT_BUTTON = (By.ID, "w-node-f7ead340-ee2a-2b84-cdd5-5a35322aacbf-7f66deba")

    def verify_community_page_opened(self):
        self.verify_partial_url('community')
        #self.verify_url(self, 'https://soft.reelly.io/community')

    def verify_support_button_clickable(self):
        self.wait_until_visible(self.SUPPORT_BUTTON)
