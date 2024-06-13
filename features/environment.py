from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from app.application import Application

from support.logger import logger

def browser_init(context):
    """
    :param context: Behave context
    """
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver =webdriver.Firefox(service=service)

    # service = Service(executable_path='/Users/johnharchar/Desktop/QA/python-selenium-automation/geckodriver')
    # context.driver = webdriver.Firefox(service=service)

    # context.driver = webdriver.Safari()

    # mobile_emulation = {"deviceName": "Nexus 5"}
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
    #                           desired_capabilities=chrome_options.to_capabilities())

    # mobile emulator (Selenium)
    mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service, options=chrome_options)

    # mobile_emulation = {
    #     "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    #     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
    #     "clientHints": {"platform": "Android", "mobile": True}}
    # chrome_options = Options()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # driver = webdriver.Chrome(chrome_options=chrome_options)


    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service)

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    #     ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'johnharchar_osPBA6'
    bs_key = 'd1eBUXaNs6SPRy1WUDmx'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    # options = Options()
    # bstack_options = {
    #     'os' : 'Windows',
    #     'osVersion' : '11',
    #     'browserName': 'Chrome',
    #     'sessionName': 'Verify Secondary pages can be accessed by user'
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)


    context.driver.maximize_window()
    #options.add_argument("--window-size=1920,1080")
    #context.driver.set_window_size(1920, 1080)
    context.driver.implicitly_wait(10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context)


def before_step(context, step):
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.warning('Step failed: {step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()

#behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/main_page_ui.feature