from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

@then('Verify Contact us page is open')
def verify_contact_us_page_is_open(context):
    context.app.contact_us_page.verify_contact_us_page_opened()

@then('Verify social media icons appear')
def verify_social_media_icons(context):
    context.app.contact_us_page.verify_social_media_icons()

@then('Verify Connect the company button on conact us page is clickable')
def verify_connect_company_button_clickable(context):
    context.app.contact_us_page.verify_connect_company_button_clickable()