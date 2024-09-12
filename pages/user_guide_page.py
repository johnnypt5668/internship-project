from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class UserGuidePage(Page):

    VIDEO_TEXT = (By.XPATH, "//div[text()='Full overview of Reelly platform']")

    def verify_user_guide_page_opened(self):
        self.verify_partial_url('user-guide')

    # def verify_video_title(self):
    #     #frame1 = self.driver.find_element(By.CSS_SELECTOR, "iframe[class='embedly-embed']")
    #     #frame2 = self.driver.find_element(By.CSS_SELECTOR, "iframe[title='Full overview of Reelly platform']")
    #     #self.driver.switch_to.frame(frame1)
    #     #self.driver.switch_to.frame(frame2)
    #     self.verify_text('Full overview of Reelly platform', *self.VIDEO_TEXT)

    def verify_video_title(self):
        titles = self.driver.find_elements(*self.VIDEO_TEXT)
        assert all(title.text.strip() != "" for title in titles), "Not all lesson videos have titles"