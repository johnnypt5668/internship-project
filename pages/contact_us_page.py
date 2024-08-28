from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class ContactUsPage(Page):

    SOCIAL_MEDIA_ICONS = (By.CSS_SELECTOR, "div[class='text-social']")
    CONNECT_COMPANY_BUTTON = (By.XPATH, "//div[@class='get-free-period menu' and text()='Connect the company']")

    def verify_contact_us_page_opened(self):
        self.verify_partial_url('contact-us')

    def verify_social_media_icons(self):
        self.find_elements(By.CSS_SELECTOR, "div[class='text-social']")

    def verify_connect_company_button_clickable(self):
        self.wait_until_visible(self.CONNECT_COMPANY_BUTTON)