from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

CURRENT_MARKET_PAGE = (By.XPATH, "//div[@wized='currentPageMarket']")
FINAL_MARKET_PAGE = (By.CSS_SELECTOR, "div[wized='totalPageMarket')]")

@then('Verify market page is open')
def verify_market_page_open(context):
    context.app.market_page.verify_market_page_open()

@then('Go to final market page using pagination button')
def go_to_final_page(context):
    if CURRENT_MARKET_PAGE != FINAL_MARKET_PAGE:
        context.app.market_page.click_market_page_button()
        sleep(5)

@then('Click on Developers button')
def click_on_developers_button(context):
    context.app.market_page.click_on_developers_button()


@then('Return to first market page using pagination button')
def return_to_first_page(context):
    if CURRENT_MARKET_PAGE != 1:
        context.app.market_page.click_market_back_page_button()
    sleep(5)

@then('Verify developers have license tag displayed')
def verify_developers_license_tag(context):
    context.app.market_page.verify_license_appears_in_tags()
