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

@then('Click on Off Plan Filters button')
def click_off_plan_filters_button(context):
    context.app.off_plan_page.click_off_plan_filters_button()

@then('Input price in Off Plan From box under Unit price (AED)')
def input_price_in_off_plan_from_box(context):
    context.app.off_plan_page.input_off_plan_from_price('1200000')

@then('Input price in Off Plan To box under Unit price (AED)')
def input_price_in_off_plan_to_box(context):
    context.app.off_plan_page.input_off_plan_to_price('2000000')

@then('Click Off Plan Apply Filter at page bottom')
def click_apply_off_plan_filter_button(context):
    context.app.off_plan_page.click_off_plan_apply_filter_button()

@then("Verify Off Plan price is in range given")
def verify_off_plan_price_in_range_given(context):
    context.app.off_plan_page.verify_off_plan_price_in_range()

@then("Verify properties have title on each")
def verify_off_plan_title_in_each_card(context):
    context.app.off_plan_page.verify_off_plan_cards_have_titles()

@then("Verify properties have image on each")
def verify_off_plan_cards_have_images(context):
    context.app.off_plan_page.verify_off_plan_cards_have_images()

@then("Click on Sales Status button and Out of Stock dropdown")
def click_out_of_stock_dropdown(context):
    context.app.off_plan_page.select_out_of_stock_dropdown()

@then("Verify all boxes have Out of Stock tag")
def verify_out_of_stock_text_is_in_boxes(context):
    context.app.off_plan_page.verify_out_of_stock_tage_appears_in_boxes()

@then("Click on first product")
def click_first_product_button(context):
    context.app.off_plan_page.click_on_first_product()