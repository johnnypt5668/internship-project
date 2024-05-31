from pages.base_page import Page
from pages.home_page import HomePage
from pages.secondary_page import SecondaryPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.home_page = HomePage(driver)
        self.secondary_page = SecondaryPage(driver)