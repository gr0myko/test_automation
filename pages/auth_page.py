from selenium.webdriver.common.by import By

from framework.base.base_page import BasePage
from framework.elements.text_input import TextInput
from framework.elements.button import Button


class AuthPage(BasePage):
    def __init__(self):
        self.email_input_locator = (By.XPATH, "//input[@id='index_email']")
        self.password_input_locator = (By.XPATH, "//input[@id='index_pass']")
        self.login_button_locator = (By.XPATH,
                                     "//button[@id='index_login_button']")

        self.email_input = TextInput(self.email_input_locator)

    def is_form_displayed(self):
        return self.email_input.is_element_present()

    def fill_in_email(self, email: str):
        self.email_input.send_text(email)

    def fill_in_password(self, password: str):
        password_input = TextInput(self.password_input_locator)
        password_input.send_text(password)

    def click_on_login_button(self):
        login_button = Button(self.login_button_locator)
        login_button.click()

    def authorize(self, email, password):
        self.fill_in_email(email)
        self.fill_in_password(password)
        self.click_on_login_button()
