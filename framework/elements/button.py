from framework.elements.base_element import BaseElement


class Button(BaseElement):
    def send_file(self, file_path):
        element = self.find_element(self.selector)
        element.send_keys(file_path)
