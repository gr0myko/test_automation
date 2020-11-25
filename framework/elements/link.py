from framework.elements.base_element import BaseElement


class Link(BaseElement):
    def get_link(self):
        element = self.find_element(self.selector)
        return element.get_attribute("href")
