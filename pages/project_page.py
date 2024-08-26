from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class ProjectPage(Page):

   BROKER_HEADER = (By.XPATH, "//h1[@class='h1-add']")
   NAME_TEXT_BOX = (By.ID, 'Your-name')
   COMPANY_TEXT_BOX = (By.ID, 'Your-company-name')
   ROLE_TEXT_BOX = (By.ID, 'Role')
   COMPANY_AGE_BOX = (By.ID, 'Age-of-the-company')
   PROJECT_COUNTRY_BOX = (By.ID, 'Country')
   PROJECT_NAME_BOX = (By.ID, 'Name-project')
   PHONE_NUMBER_BOX = (By.ID, 'Phone')
   EMAIL_BOX = (By.ID, 'Email-add-project')
   APPLICATION_BUTTON = (By.CSS_SELECTOR, "input[value='Send an application']")

   def verify_project_page_opened(self):
      self.verify_partial_url('add-a-project')

   def enter_name(self, name):
      self.input_text(name, *self.NAME_TEXT_BOX)

   def enter_project_company(self, project_company):
      self.input_text(project_company, *self.COMPANY_TEXT_BOX)

   def enter_company_role(self, company_role):
      self.input_text(company_role, *self.ROLE_TEXT_BOX)

   def verify_name_input(self, name_input):
      self.verify_input_field_text(name_input, *self.NAME_TEXT_BOX)

   def verify_company_input(self, company_input):
      self.verify_input_field_text(company_input, *self.COMPANY_TEXT_BOX)

   def verify_role_input(self, role_input):
      self.verify_input_field_text(role_input, *self.ROLE_TEXT_BOX)

   def enter_company_age(self, company_age):
      self.input_text(company_age, *self.COMPANY_AGE_BOX)

   def enter_project_country(self, project_country):
      self.input_text(project_country, *self.PROJECT_COUNTRY_BOX)

   def enter_project_name(self, project_name):
      self.input_text(project_name, *self.PROJECT_NAME_BOX)

   def enter_company_phone_number(self, company_phone_number):
      self.input_text(company_phone_number, *self.PHONE_NUMBER_BOX)

   def enter_company_email(self, company_email):
      self.input_text(company_email, *self.EMAIL_BOX)

   def app_button_clickable(self):
      self.wait_until_visible(self.APPLICATION_BUTTON)

