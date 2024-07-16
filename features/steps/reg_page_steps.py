from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select




@given ('Open the registration page')
def open_reg_page(context):
    context.app.reg_page.open_reg_page()

@when ('Enter full name')
def type_full_name(context):
    context.app.reg_page.enter_full_name("John Harchar")

@then ('Enter phone number')
def type_phone_number(context):
    context.app.reg_page.enter_phone("7328875784")

@then ('Enter email')
def type_email(context):
    context.app.reg_page.enter_email("johnnypt@verizon.net")

@then ('Enter password')
def type_password(context):
    context.app.reg_page.enter_password("JimiHendrix1942!")

@then ('Enter company name')
def type_company_name(context):
    context.app.reg_page.enter_company_name("Charsky Productions")

@then ('Select country')
def select_country(context):
    context.app.reg_page.select_country("United States of America")

@then ('Select company size')
def select_size(context):
    context.app.reg_page.select_comp_size("5-10")