from framework.base.base_page import BasePage
from framework.elements.button import Button
from framework.elements.text import Text
from framework.base.utils.logger import Logger
from selenium.webdriver.common.by import By

logger = Logger.start()


class MainPage(BasePage):
    def __init__(self):
        self.alert_locator = (By.XPATH, "//button[@onclick='jsAlert()']")
        self.confirm_locator = (By.XPATH, "//button[@onclick='jsConfirm()']")
        self.prompt_locator = (By.XPATH, "//button[@onclick='jsPrompt()']")
        self.result_locator = (By.XPATH, "//p[@id='result']")

    def click_on_alert_button(self):
        alert_button = Button(self.alert_locator)
        logger.info("Alert button clicked")
        alert_button.wait_and_click()

    def click_on_confirm_button(self):
        confirm_button = Button(self.confirm_locator)
        logger.info("Confirm button clicked")
        confirm_button.wait_and_click()

    def click_on_prompt_button(self):
        prompt_button = Button(self.prompt_locator)
        logger.info("Prompt button clicked")
        prompt_button.wait_and_click()

    def get_result_text(self):
        result = Text(self.result_locator)
        logger.info(f"Result text: {result.get_text()}")
        return result.get_text()
