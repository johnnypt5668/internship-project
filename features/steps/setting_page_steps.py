from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait

@then('Click on Edit Profile')
def edit_profile(context):
    context.app.settings_page.click_edit_profile_button()

@then('Input test name')
def input_test_name(context):
    context.app.settings_page.input_name('Bob')

@then('Input test number')
def input_test_number(context):
    context.app.settings_page.input_number('732-251-5702')

@then('Input test company')
def input_test_company(context):
    context.app.settings_page.input_test_company('Charsky')

@then('Verify correct text is in name field')
def verify_text_in_name(context):
    context.app.settings_page.verify_correct_name('Bob')

@then('Verify correct text is in phone number field')
def verify_phone_number(context):
    context.app.settings_page.verify_correct_number("732-251-5702")

@then('Verify correct text is in compnay field')
def verify_test_company(context):
    context.app.settings_page.verify_correct_company('Charsky')