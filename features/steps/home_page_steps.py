from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

@given ('Open the main page')
def open_home(context):
    context.app.home_page.open_home()

@when ('Enter email and password to login')
def enter_email_and_password_to_login(context):
    context.app.home_page.enter_email_and_password("johnnypt@verizon.net", "JimiHendrix1942!")

@when ('Enter email and password')
def enter_email_and_password(context):
    context.app.home_page.type_email_and_password("johnnypt@verizon.net", "JimiHendrix1942!")

@then ('Click on Connect the Company button')
def click_on_connect_button(context):
    context.app.home_page.click_connect_company_button()

@then ('Switch to company window')
def switch_to_new_page(context):
    context.app.home_page.switch_to_company_page()


@then ('Click on Secondary button')
def click_secondary_button(context):
    sleep (120)
    context.app.home_page.click_secondary_button()

@then ('Click on mobile Secondary button')
def click_mobile_secondary_button(context):
    context.app.home_page.click_mobile_secondary_button()

@then ('Verify correct page is open')
def verify_correct_page(context):
    sleep(10)
    context.app.home_page.verify_correct_page()