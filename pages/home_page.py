from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class HomePage(Page):

    SIGNIN_PAGE_EMAIL_BOX =  (By.CSS_SELECTOR, "input[name='email-2']")
    SIGNIN_PAGE_PASSWORD_BOX = (By.CSS_SELECTOR, "input[name='Password']")
    SIGNIN_BUTTON = (By.CSS_SELECTOR, "a[class='login-button w-button']")


    def open_home(self):
        self.driver.get('https://soft.reelly.io/sign-in')

    def enter_email_and_password(self, email, password):
        self.input_text(email, *self.SIGNIN_PAGE_EMAIL_BOX)
        self.input_text(password, *self.SIGNIN_PAGE_PASSWORD_BOX)
        self.click(*self.SIGNIN_BUTTON)

    def click_secondary_button(self):
        self.driver.find_element(By.XPATH, "//a[@href='/secondary-listings']").click()

    def click_mobile_secondary_button(self):
        self.driver.find_element(By.XPATH, "//a[@wized='mobileTabGame']").click()

    def type_email_and_password(self, email, password):
        self.input_text(email, *self.SIGNIN_PAGE_EMAIL_BOX)
        self.input_text(password, *self.SIGNIN_PAGE_PASSWORD_BOX)
        sleep(30)
