from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait

@given ('Open the main page')
def open_home(context):
    context.app.home_page.open_home()

@when ('Enter email and password to login')
def enter_email_and_password(context):
    context.app.home_page.enter_email_and_password("johnnypt@verizon.net", "JimiHendrix1942!")

@then ('Click on Secondary button')
def click_secondary_button(context):
    context.app.home_page.click_secondary_button()