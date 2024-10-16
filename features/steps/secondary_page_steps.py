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

@then('Click on Filters tab')
def click_on_filters_tab(context):
    context.app.secondary_page.click_filters_tab()

@then('Filter by Want to sell')
def click_want_to_sell_tab(context):
    context.app.secondary_page.click_want_to_sell_tab()

@then('Filter by Want to buy')
def click_want_to_buy_tab(context):
    context.app.secondary_page.click_want_to_buy_tab()

@then('Click Apply Filter at page bottom')
def click_apply_filter_button(context):
    context.app.secondary_page.click_apply_filter_button()

@then('Confirm all properties have For sale tag')
def verify_for_sale_tag_on_all_boxes(context):
    context.app.secondary_page.verify_for_sale_tag_visible()

@then('Confirm all properties have Want to buy tag')
def verify_want_to_buy_tag_on_all_boxes(context):
    context.app.secondary_page.verify_want_to_buy_tag_visible()
