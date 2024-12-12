from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

@then('Verify architecture visualization is visible')
def verify_architecture_visualization(context):
    context.app.first_product_page.verify_architecture_button_is_visible()

@then('Verify architecture visualization is clickable')
def verify_architecture_visualization_clickable(context):
    context.app.first_product_page.verify_architecture_button_is_clickable()