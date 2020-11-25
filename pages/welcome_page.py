from framework.base.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.base.utils.logger import Logger
from framework.elements.link import Link

logger = Logger.start()


class WelcomePage(BasePage):
    def __init__(self):
        self.link_locator = (By.XPATH, "//a[@class='start__link']")
        self.link = Link(self.link_locator)

    def is_form_displayed(self):
        return self.link.is_element_present()

    def click_on_next_page_link(self):
        self.link.click()
