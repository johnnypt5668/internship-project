from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


@then('Verify Community page is open')
def verify_community_page_is_open(context):
    context.app.community_page.verify_community_page_opened()

@then ('Verify Support button is clickable')
def verify_support_button_clickable(context):
    context.app.community_page.verify_support_button_clickable()