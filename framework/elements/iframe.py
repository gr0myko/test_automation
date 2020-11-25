from framework.elements.base_element import BaseElement
from framework.elements.text_input import TextInput
from framework.base.utils.logger import Logger

logger = Logger.start()


class IFrame(BaseElement):
    def __init__(self, selector, input_locator, bold_input_locator):
        BaseElement.__init__(self, selector)
        self.input_locator = input_locator
        self.bold_input_locator = bold_input_locator
        self.text_input_element = TextInput(self.input_locator)

    def get_id(self):
        element = self.browser.find_element(*self.selector)
        return element.get_attribute("id")

    def delete_text(self):
        self.text_input_element.delete_text()

    def send_text(self, text):
        self.text_input_element.send_text(text)

    def get_text(self):
        return self.text_input_element.get_text()

    def select_text(self):
        logger.info(f"Text {self.text_input_element.get_text()} selected")
        self.text_input_element.select_text()

    def is_text_bold(self):
        bold_input_text = TextInput(self.bold_input_locator)
        return bold_input_text.is_element_present()
