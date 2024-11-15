from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

CURRENT_PAGE = (By.XPATH, "//div[@wized='currentPageProperties']")
FINAL_PAGE = (By.XPATH, "//*[contains(text(), 'totalPageProperties')]")

@then('Verify off plan page is open')
def verify_off_plan_page_opened(context):
    context.app.off_plan_page.verify_off_plan_page_opened()

@then('Go to final off page listings using pagination button')
def go_to_final_off_page_listing(context):
    context.app.off_plan_page.go_to_last_pagination()


@then('Return to first off page listings using pagination button')
def return_to_first_off_page_listing(context):
    context.app.off_plan_page.go_to_first_pagination()