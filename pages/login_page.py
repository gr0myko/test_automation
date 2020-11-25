from framework.base.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.base.utils.logger import Logger
from framework.elements.text_input import TextInput
from framework.elements.button import Button
from framework.elements.box import Box
from framework.elements.dropdown import DropdownField
from framework.elements.checkbox import Checkbox
from framework.elements.text import Text

logger = Logger.start()


class LoginPage(BasePage):
    def __init__(self):
        self.password_locator = (By.XPATH,
                                 "//div//input[contains(@placeholder,'Password')]")
        self.accept_cookies_button = (By.XPATH,
                                      "//div[@class='cookies']//button"
                                      "[contains(@class,'transparent')]")
        self.hide_help_button_locator = (By.XPATH,
                                         "//div[@class='help-form']//button"
                                         "[contains(@class,'send-to-bottom')]")
        self.hidden_help_locator = (By.XPATH,
                                    "//div[@class='help-form is-hidden']")
        self.login_locator = (By.XPATH, "//input[contains(@placeholder,'email')]")
        self.domain_locator = (By.XPATH, "//input[@placeholder='Domain']")
        self.dropdown_locator = (By.XPATH, "//div[@class='dropdown__field']")
        self.dropdown_item_locator = "//div[@class='dropdown__list']" \
                                     "//div[text()='{}']"
        self.terms_agree_locator = (By.XPATH, "//span[@class='checkbox__box']")
        self.next_button_locator = (By.XPATH, "//a[@class='button--secondary']")
        self.timer_locator = (By.XPATH, "//div[contains(@class,'timer--center')]")
        self.help_up_button_locator = (By.XPATH,
                                       "//span[contains(@class,'chevron-up')]")

        self.password_input = TextInput(self.password_locator)
        self.accept_cookies_button = Button(self.accept_cookies_button)

    def is_form_displayed(self):
        return self.password_input.is_element_present()

    def accept_cookies(self):
        self.accept_cookies_button.wait_and_click()

    def is_cookies_form_displayed(self):
        return self.accept_cookies_button.is_element_present()

    def hide_help_form(self):
        hide_help_button = Button(self.hide_help_button_locator)
        hide_help_button.wait_and_click()

    def wait_help_form_to_hide(self):
        help_up_button = Button(self.help_up_button_locator)
        help_up_button.wait_until_invisible()

    def is_help_form_hidden(self):
        hidden_help_box = Box(self.hidden_help_locator)
        return hidden_help_box.is_element_present()

    def fill_in_password(self, password):
        self.password_input.select_text()
        self.password_input.send_text(password)

    def fill_in_login(self, login):
        login_input = TextInput(self.login_locator)
        login_input.select_text()
        login_input.send_text(login)

    def fill_in_domain(self, domain):
        domain_input = TextInput(self.domain_locator)
        domain_input.select_text()
        domain_input.send_text(domain)

    def choose_dropdown_domain(self, domain:str):
        dropdown_domain = DropdownField(self.dropdown_locator)
        dropdown_domain.click()
        dropdown_item = Button((By.XPATH,
                                self.dropdown_item_locator.format(domain)))
        dropdown_item.click()

    def click_on_terms_agree_checkbox(self):
        terms_agree_checkbox = Checkbox(self.terms_agree_locator)
        terms_agree_checkbox.click()

    def click_on_next_button(self):
        next_button = Button(self.next_button_locator)
        next_button.click()

    def get_timer_value(self):
        timer = Text(self.timer_locator)
        return timer.get_text()
