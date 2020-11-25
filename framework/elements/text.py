from framework.elements.base_element import BaseElement


class Text(BaseElement):
    def get_text(self):
        element = self.find_element(self.selector)
        element_text = element.text
        return element_text
