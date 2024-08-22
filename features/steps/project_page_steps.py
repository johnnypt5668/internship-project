from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

@then('Verify Project page is open')
def verify_project_page_is_open(context):
    context.app.project_page.verify_project_page_opened()

@then('Enter name')
def enter_name(context):
    context.app.project_page.enter_name('John Harchar')

@then('Enter company')
def enter_company(context):
    context.app.project_page.enter_project_company('Charsky')

@then('Enter company role')
def enter_company_role(context):
    context.app.project_page.enter_company_role('CEO')

@then('Verify name is in text box')
def verify_name_input(context):
    context.app.project_page.verify_name_input('John Harchar')

@then('Verify company is in text box')
def verify_company_inout(context):
    context.app.project_page.verify_company_input('Charsky')

@then('Verify company role is in text box')
def verify_company_role(context):
    context.app.project_page.verify_role_input('CEO')

@then('Enter company age')
def enter_company_age(context):
    context.app.project_page.enter_company_age('10')

@then('Enter project country')
def enter_project_country(context):
    context.app.project_page.enter_project_country("USA")

@then('Enter project name')
def enter_project_name(context):
    context.app.project_page.enter_project_name("Home")

@then('Enter company phone number')
def enter_company_phone_number(context):
    context.app.project_page.enter_company_phone_number("555-555-1234")

@then('Enter company email')
def enter_company_email(context):
    context.app.project_page.enter_company_email("Charsky@gmail.com")

@then('Verify Send an application button is clickable')
def verify_app_buttob_clickable(context):
    context.app.project_page.app_button_clickable()
