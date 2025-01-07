from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@then('Confirm Verification page opened')
def confirm_verification_page_opened(context):
    context.app.verification_page.confirm_verification_page_opened()

@then("Verify Upload image button is available")
def verify_upload_image_button_available(context):
    context.app.verification_page.verify_upload_image_button_available()

@then("Verify Next step button is available")
def verify_next_step_button_available(context):
    context.app.verification_page.verify_next_step_button_available()