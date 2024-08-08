from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

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

@then ('Click on the Settings button')
def click_on_settings_button(context):
    context.app.home_page.click_settings_button()


@then ('Click on the Main Menu button')
def click_on_main_menu_button(context):
    context.app.home_page.click_main_menu_button()

@then ('Switch to new window')
def switch_to_new_page(context):
    context.app.home_page.switch_to_new_page()



@then ('Click on Secondary button')
def click_secondary_button(context):
    sleep (120)
    context.app.home_page.click_secondary_button()

@then ('Click on mobile Secondary button')
def click_mobile_secondary_button(context):
    context.app.home_page.click_mobile_secondary_button()