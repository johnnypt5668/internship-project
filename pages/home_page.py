from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

class HomePage(Page):

    SIGNIN_PAGE_EMAIL_BOX =  (By.CSS_SELECTOR, "input[name='email-2']")
    SIGNIN_PAGE_PASSWORD_BOX = (By.CSS_SELECTOR, "input[name='Password']")
    SIGNIN_BUTTON = (By.CSS_SELECTOR, "a[class='login-button w-button']")
    CONNECT_COMPANY_BUTTON = (By.CSS_SELECTOR, "div[class='get-free-period menu']")


    def open_home(self):
        self.driver.get('https://soft.reelly.io/sign-in')

    def enter_email_and_password(self, email, password):
        self.input_text(email, *self.SIGNIN_PAGE_EMAIL_BOX)
        self.input_text(password, *self.SIGNIN_PAGE_PASSWORD_BOX)
        self.click(*self.SIGNIN_BUTTON)


    def click_connect_company_button(self):
        self.click(*self.CONNECT_COMPANY_BUTTON)

    def switch_to_company_page(self ):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[1])


    def click_secondary_button(self):
        self.driver.find_element(By.XPATH, "//a[@href='/secondary-listings']").click()

    def click_mobile_secondary_button(self):
        self.driver.find_element(By.XPATH, "//a[@wized='mobileTabGame']").click()

    def type_email_and_password(self, email, password):
        self.input_text(email, *self.SIGNIN_PAGE_EMAIL_BOX)
        self.input_text(password, *self.SIGNIN_PAGE_PASSWORD_BOX)
        sleep(30)

    def verify_correct_page(self):
        self.verify_url('https://soft.reelly.io/book-presentation')
