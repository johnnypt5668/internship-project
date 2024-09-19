from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class SubscriptionPage(Page):

    #HEADER_TITLE = (By.XPATH, "//div[@class='lotion-your-h3--price' and text()='Subscription & payments']")
    #HEADER_TITLE = (By.XPATH, "//wized[@class='size' and text()='Subscription & payments']")

    HEADER_TITLE = (By.CSS_SELECTOR, "div[class='lotion-your-h3--price size']")
    BACK_BUTTON = (By.CSS_SELECTOR, "div[class ='back-text']")
    UPGRADE_PLAN_BUTTON = (By.CSS_SELECTOR, "div[class='next-step--']")

    def verify_subscription_page_opened(self):
        self.verify_partial_url('subscription')

    def verify_subscription_header(self):
        self.verify_text("Subscription & payments", *self.HEADER_TITLE)

    def verify_back_button(self):
        self.wait_until_visible(self.BACK_BUTTON)

    def verify_upgrade_plan_button_available(self):
        self.wait_until_visible(self.UPGRADE_PLAN_BUTTON)