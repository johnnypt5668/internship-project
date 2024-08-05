from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class SettingsPage(Page):

    EDIT_PROFILE_BUTTON = (By.CSS_SELECTOR, "a[href='/profile-edit']")
    PROFILE_NAME_BOX = (By.NAME, "Fullname")
    PHONE_NUMBER_BOX = (By.NAME, "number")
    COMPANY_BOX = (By.NAME, 'Company-name')

    def click_edit_profile_button(self):
        self.click(*self.EDIT_PROFILE_BUTTON)

    def input_name(self, name):
        input_testname = self.find_element(*self.PROFILE_NAME_BOX)
        input_testname.clear()
        self.input_text("Bob", *self.PROFILE_NAME_BOX)

    def input_number(self, number):
        input_testnumber = self.find_element(*self.PHONE_NUMBER_BOX)
        input_testnumber.clear()
        self.input_text("732-251-5702", *self.PHONE_NUMBER_BOX)

    def input_test_company(self, company):
        input_testco = self.find_element(*self.COMPANY_BOX)
        input_testco.clear()
        self.input_text("Charsky", *self.COMPANY_BOX)

    def verify_correct_name(self, name):
        self.verify_text('Bob', self.PROFILE_NAME_BOX)

    def verify_correct_number(self, number):
        self.verify_text('732-251-5702', *self.PHONE_NUMBER_BOX)

    def verify_correct_company(self, company):
        self.verify_text('Charsky', *self.COMPANY_BOX)


