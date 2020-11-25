from framework.elements.base_element import BaseElement


class TextInput(BaseElement):
    def get_text(self):
        element = self.find_element(self.selector)
        element_text = element.text
        return element_text

    def delete_text(self):
        element = self.find_element(self.selector)
        element.clear()

    def send_text(self, text):
        element = self.find_element(self.selector)
        element.send_keys(text)
