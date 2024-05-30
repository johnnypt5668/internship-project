from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait

CURRENT_PAGE = (By.XPATH, "//div[@wized='currentPageProperties']")
FINAL_PAGE = (By.XPATH, "//*[contains(text(), 'totalPageProperties')]")


@then('Verify Secondary page is open')
def verify_secondary_page_is_open(context):
    context.app.secondary_page.verify_secondary_page_opened()


@then('Go to final page using pagination button')
def go_to_final_page(context):
    if CURRENT_PAGE != FINAL_PAGE:
        context.app.secondary_page.click_page_button()


@then('Return to first page using pagination button')
def return_to_first_page(context):
    if CURRENT_PAGE != 1:
        context.app.secondary_page.click_back_page_button()
