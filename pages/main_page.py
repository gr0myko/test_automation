from selenium.webdriver.common.by import By

from framework.base.base_page import BasePage
from pages.main_menu import MainMenu
from framework.elements.box import Box


class MainPage(BasePage):
    def __init__(self):
        self.main_menu = MainMenu()
        self.new_post_locator = (By.XPATH, "//div[@id='post_field']")

    def is_form_displayed(self):
        new_post_field = Box(self.new_post_locator)
        return new_post_field.is_element_present()
