from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class SettingsPage(Page):

    EDIT_PROFILE_BUTTON = (By.CSS_SELECTOR, "a[href='/profile-edit']")
    PROFILE_NAME_BOX = (By.NAME, "Fullname")
    PHONE_NUMBER_BOX = (By.NAME, "number")
    COMPANY_BOX = (By.NAME, 'Company-name')
    LANGUAGE_BUTTON = (By.ID, "w-dropdown-toggle-0")
    RU_BUTTON = (By.ID, "w-dropdown-list-0")
    RU_MAIN_MENU = (By.XPATH, "//div[@class='menu-button-text' and text()='Главное меню']")
    PROJECT_BUTTON = (By.CSS_SELECTOR, "a[href='/add-a-project']")
    COMMUNITY_BUTTON = (By.XPATH, "//div[@class='setting-text' and text()='Community']")
    CONTACT_US_BUTTON = (By.XPATH, "//div[@class='setting-text' and text()='Contact us']")
    USER_GUIDE_BUTTON = (By.XPATH, "//div[@class='setting-text' and text()='User guide']")
    CHANGE_PASSWORD_BUTTON = (By.XPATH, "//div[@class='setting-text' and text()='Change password']")
    SUBSCRIPTION_BUTTON = (By.XPATH, "//a[@href='/subscription']")

    def click_edit_profile_button(self):
        self.click(*self.EDIT_PROFILE_BUTTON)

    def click_project_button(self):
        self.click(*self.PROJECT_BUTTON)

    def click_community_button(self):
        self.click(*self.COMMUNITY_BUTTON)

    def click_contact_us_button(self):
        self.click(*self.CONTACT_US_BUTTON)

    def click_user_guide_button(self):
        self.click(*self.USER_GUIDE_BUTTON)

    def click_change_password_button(self):
        self.click(*self.CHANGE_PASSWORD_BUTTON)

    def click_subscription_button(self):
        self.click(*self.SUBSCRIPTION_BUTTON)

    def input_name(self, name):
        input_testname = self.find_element(*self.PROFILE_NAME_BOX)
        input_testname.clear()
        self.input_text("Bob", *self.PROFILE_NAME_BOX)
        sleep(5)

    def input_number(self, number):
        input_testnumber = self.find_element(*self.PHONE_NUMBER_BOX)
        input_testnumber.clear()
        self.input_text("732-251-5702", *self.PHONE_NUMBER_BOX)

    def input_test_company(self, company):
        input_testco = self.find_element(*self.COMPANY_BOX)
        input_testco.clear()
        self.input_text("Charsky", *self.COMPANY_BOX)

    def verify_correct_name(self, name):
        self.verify_input_field_text(name, *self.PROFILE_NAME_BOX)

    def verify_correct_number(self, number):
        self.verify_input_field_text(number, *self.PHONE_NUMBER_BOX)

    def verify_correct_company(self, company):
        self.verify_input_field_text(company, *self.COMPANY_BOX)

    def change_language(self):
        lang_button = self.find_element(*self.LANGUAGE_BUTTON)

        actions = ActionChains(self.driver)
        actions.move_to_element(lang_button).perform()
        sleep(3)
        self.click(*self.RU_BUTTON)
        sleep(5)

    def verify_language_change(self):
        actual_text = self.find_element(*self.RU_MAIN_MENU).text
        expected_text = 'Главное меню'
        assert expected_text in actual_text, f"Expected {expected_text}, got {actual_text}"