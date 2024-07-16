from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class RegPage(Page):

    REG_PAGE_NAME_BOX = (By.ID, 'Full-Name')
    REG_PAGE_PHONE = (By.ID, 'phone2')
    REG_PAGE_EMAIL = (By.ID, 'Email-3')
    REG_PAGE_PASSWORD = (By.ID, 'field')
    REG_PAGE_COMPANY = (By.ID, 'Company-website')
    REG_PAGE_COUNTRY = (By.CSS_SELECTOR, "select[id='country-select']")
    REG_PAGE_SIZE = (By.CSS_SELECTOR, "select[id='Agents-amount-2']")


    def open_reg_page(self):
        self.driver.get('https://soft.reelly.io/sign-up')

    def enter_full_name(self, full_name):
        self.input_text(full_name, *self.REG_PAGE_NAME_BOX)

    def enter_phone(self, phone):
        self.input_text(phone, *self.REG_PAGE_PHONE)

    def enter_email(self, email):
        self.input_text(email, *self.REG_PAGE_EMAIL)

    def enter_password(self, password):
        self.input_text(password, *self.REG_PAGE_PASSWORD)

    def enter_company_name(self, company_name):
        self.input_text(company_name, *self.REG_PAGE_COMPANY)

    def select_country(self, country_name):
        country = self.find_element(*self.REG_PAGE_COUNTRY)
        select = Select(country)
        select.select_by_value("United States of America")

    def select_comp_size(self, size):
        size = self.find_element(*self.REG_PAGE_SIZE)
        select = Select(size)
        select.select_by_value("5-10")

