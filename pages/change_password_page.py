from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep

class ChangePasswordPage(Page):

    CHANGE_PASSWORD_BOX = (By.CSS_SELECTOR, "input[name='Enter-new-password']")
    CONFIRM_PASSWORD_BOX = (By.CSS_SELECTOR, "input[name='Repeat-password']")
    CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, "a[wized='changePasswordButton']")

    def verify_change_password_page_opened(self):
        self.verify_partial_url('set-new-password')

    def enter_and_confirm_new_password(self, new_password):
        self.input_text(new_password, *self.CHANGE_PASSWORD_BOX)
        self.input_text(new_password, *self.CONFIRM_PASSWORD_BOX)
        sleep(5)

    def verify_change_password_button_clickable(self):
        self.wait_until_visible(self.CHANGE_PASSWORD_BUTTON)