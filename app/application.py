from pages.base_page import Page
from pages.community_page import CommunityPage
from pages.contact_us_page import ContactUsPage
from pages.home_page import HomePage
from pages.project_page import ProjectPage
from pages.registration_page import RegPage
from pages.secondary_page import SecondaryPage
from pages.settings_page import SettingsPage
from pages.user_guide_page import UserGuidePage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.community_page = CommunityPage(driver)
        self.contact_us_page = ContactUsPage(driver)
        self.home_page = HomePage(driver)
        self.project_page = ProjectPage(driver)
        self.reg_page = RegPage(driver)
        self.secondary_page = SecondaryPage(driver)
        self.settings_page = SettingsPage(driver)
        self.user_guide_page = UserGuidePage(driver)
