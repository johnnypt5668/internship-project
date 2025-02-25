from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

class HomePage(Page):

    SIGNIN_PAGE_EMAIL_BOX =  (By.CSS_SELECTOR, "input[name='email-2']")
    SIGNIN_PAGE_PASSWORD_BOX = (By.CSS_SELECTOR, "input[name='Password']")
    SIGNIN_BUTTON = (By.CSS_SELECTOR, "a[class='login-button w-button']")
    CONNECT_COMPANY_BUTTON = (By.CSS_SELECTOR, "div[class='get-free-period menu']")
    OFF_PLAN_BUTTON = (By.CSS_SELECTOR, "a[class='_1-link-menu w-inline-block w--current']")
    SETTINGS_BUTTON = (By.CSS_SELECTOR, "a[href='/settings']")
    MAIN_MENU_BUTTON = (By.CSS_SELECTOR, "a[href='/main-menu']")
    MARKET_BUTTON = (By.CSS_SELECTOR, "a[href='/market-companies']")



    def open_home(self):
        self.driver.get('https://soft.reelly.io/sign-in')

    def enter_email_and_password(self, email, password):
        self.input_text(email, *self.SIGNIN_PAGE_EMAIL_BOX)
        self.input_text(password, *self.SIGNIN_PAGE_PASSWORD_BOX)
        self.click(*self.SIGNIN_BUTTON)


    def click_connect_company_button(self):
        self.click(*self.CONNECT_COMPANY_BUTTON)

    def click_settings_button(self):
        self.click(*self.SETTINGS_BUTTON)

    def click_off_plan_button(self):
        self.click(*self.OFF_PLAN_BUTTON)

    def switch_to_new_page(self ):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[1])

    def click_main_menu_button(self):
        self.click(*self.MAIN_MENU_BUTTON)

    def click_market_button(self):
        self.click(*self.MARKET_BUTTON)

    def click_secondary_button(self):
        self.driver.find_element(By.XPATH, "//a[@href='/secondary-listings']").click()

    #def click_mobile_secondary_button(self):
    #    self.driver.find_element(By.XPATH, "//a[@wized='mobileTabGame']").click()

    def click_mobile_secondary_button(self):
        self.driver.find_element(By.XPATH, "//div[@class='menu-button-text' and text()='Secondary']").click()

    def type_email_and_password(self, email, password):
        self.input_text(email, *self.SIGNIN_PAGE_EMAIL_BOX)