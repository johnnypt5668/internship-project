from pages.base_page import Page
from pages.change_password_page import ChangePasswordPage
from pages.community_page import CommunityPage
from pages.contact_us_page import ContactUsPage
from pages.first_product_page import FirstProductPage
from pages.home_page import HomePage
from pages.market_page import MarketPage
from pages.off_plan_page import OffPlanPage
from pages.project_page import ProjectPage
from pages.registration_page import RegPage
from pages.secondary_page import SecondaryPage
from pages.settings_page import SettingsPage
from pages.subscription_page import SubscriptionPage
from pages.support_page import SupportPage
from pages.user_guide_page import UserGuidePage
from pages.verification_page import VerificationPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.change_password_page = ChangePasswordPage(driver)
        self.community_page = CommunityPage(driver)
        self.contact_us_page = ContactUsPage(driver)
        self.first_product_page = FirstProductPage(driver)
        self.home_page = HomePage(driver)
        self.market_page = MarketPage(driver)
        self.off_plan_page = OffPlanPage(driver)
        self.project_page = ProjectPage(driver)
        self.reg_page = RegPage(driver)
        self.secondary_page = SecondaryPage(driver)
        self.settings_page = SettingsPage(driver)
        self.subscription_page = SubscriptionPage(driver)
        self.support_page = SupportPage(driver)
        self.user_guide_page = UserGuidePage(driver)
        self.verification_page = VerificationPage(driver)
