from framework.base.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.elements.text import Text


class MainPage(BasePage):
    def __init__(self):
        self.info_link_locator = (By.XPATH, "//a[contains(@href,'domains/example')]")

    def is_form_displayed(self):
        info_link = Text(self.info_link_locator)
        if info_link.is_element_present() is True:
            return True
        else:
            return False
