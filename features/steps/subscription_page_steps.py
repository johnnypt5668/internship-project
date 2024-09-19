from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait

@then('Verify Subscription page is open')
def verify_subscription_page_opened(context):
    context.app.subscription_page.verify_subscription_page_opened()

@then('Verify Subscription & payments header')
def verify_subscription_header(context):
    context.app.subscription_page.verify_subscription_header()

@then('Verify Back button is available')
def verify_back_button_available(context):
    context.app.subscription_page.verify_back_button()

@then('Verify Upgrade plan button is available')
def verify_upgrade_plan_button_available(context):
    context.app.subscription_page.verify_upgrade_plan_button_available()