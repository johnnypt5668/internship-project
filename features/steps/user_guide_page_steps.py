from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait

@then('Verify User Guide page opened')
def verify_user_guide_page_opened(context):
    context.app.user_guide_page.verify_user_guide_page_opened()

@then('Verify User Guide video has title')
def verify_user_guide_video_has_title(context):
    context.app.user_guide_page.verify_video_title()