from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait


@then('Verify Support page opened')
def verify_support_page_opened(context):
    context.app.support_page.verify_support_page_opened()

@then('Verify News page opened')
def verify_news_page_opened(context):
    context.app.support_page.verify_news_page_opened()

@then('Switch back to Settings page')
def switch_to_settings_page(context):
    context.app.support_page.switch_back_to_settings()
