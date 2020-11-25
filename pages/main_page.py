from framework.base.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.elements.text_input import TextInput
from framework.base.utils.logger import Logger
from framework.elements.iframe import IFrame
from framework.elements.button import Button

logger = Logger.start()


class MainPage(BasePage):
    def __init__(self):
        self.header_selector = (By.XPATH, "//div//h3")
        self.frame_locator = (By.XPATH, "//iframe[@id='mce_0_ifr']")
        self.bold_button_locator = (By.XPATH, "//div[@id='mceu_3']//button")
        self.input_locator = (By.XPATH, "//body[@id='tinymce']//p")
        self.bold_input_locator = (By.XPATH, "//body[@id='tinymce']//p//strong")
        self.frame = IFrame(self.frame_locator, self.input_locator,
                            self.bold_input_locator)

    def is_form_displayed(self, header_text):
        header = TextInput(self.header_selector)
        logger.info(f"Header text found: {header.get_text()}")
        if header.get_text() == header_text:
            return True
        else:
            return False

    def get_frame_id(self):
        return self.frame.get_id()

    def delete_text_in_frame(self):
        self.frame.delete_text()

    def send_text_to_frame(self, text):
        self.frame.send_text(text)

    def select_text_in_frame(self):
        self.frame.select_text()

    def is_text_bold_in_frame(self):
        return self.frame.is_text_bold()

    def get_frame_text(self):
        return self.frame.get_text()

    def click_on_bold_button(self):
        bold_button = Button(self.bold_button_locator)
        logger.info(f"Bold button clicked")
        bold_button.click()
