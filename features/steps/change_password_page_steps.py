from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

@then('Verify Change password page is open')
def verify_change_password_page_opened(context):
    context.app.change_password_page.verify_change_password_page_opened()

@then('Enter and confirm new password')
def enter_and_confirm_new_password(context):
    context.app.change_password_page.enter_and_confirm_new_password("EricClapton1945")

@then ('Verify Change paasword button is clickable')
def verify_change_password_button_is_clickable(context):
    context.app.change_password_page.verify_change_password_button_clickable()