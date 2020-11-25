from framework.elements.base_element import BaseElement


class Box(BaseElement):
    def get_text(self):
        element = self.wait_and_find()
        return element.text
