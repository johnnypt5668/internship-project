from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

class VerificationPage(Page):

    UPLOAD_IMAGE_BUTTON = (By.CSS_SELECTOR, "div[class='upload-button-2 w-embed']")
    NEXT_STEP_BUTTON = (By.CSS_SELECTOR, "a[wized='nextButtonStep0']")

    def confirm_verification_page_opened(self):
        self.verify_partial_url('verification')

    def verify_upload_image_button_available(self):
        self.wait_until_visible(self.UPLOAD_IMAGE_BUTTON)

    def verify_next_step_button_available(self):
        self.wait_until_visible(self.NEXT_STEP_BUTTON)