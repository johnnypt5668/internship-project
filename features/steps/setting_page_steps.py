
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

@then('Change language to Russiian with button on top right')
def change_language_to_russian(context):
    context.app.settings_page.change_language()

@then('Verify language has changed to RU')
def verify_language_change_to__russian(context):
    context.app.settings_page.verify_language_change()


@then('Click on Add a Project button')
def click_add_project(context):
    context.app.settings_page.click_project_button()

@then('Click on the Community button')
def click_community_button(context):
    context.app.settings_page.click_community_button()

@then('Click on the Contact us button')
def click_on_contact_us_button(context):
    context.app.settings_page.click_contact_us_button()

@then('Click on User Guide button')
def click_user_guide_button(context):
    context.app.settings_page.click_user_guide_button()

@then('Click on Change password button')
def click_change_password_button(context):
    context.app.settings_page.click_change_password_button()