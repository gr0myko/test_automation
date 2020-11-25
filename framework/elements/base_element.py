from framework.base.browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from framework.base.config_class import Config
from selenium.webdriver.common.action_chains import ActionChains
from framework.base.utils.logger import Logger

logger = Logger.start()


class BaseElement:
    def __init__(self, selector):
        self.selector = selector
        self.browser = Browser.start()
        self.__element = None
        self.__elements_list = None

    def is_element_present(self):
        try:
            self.wait_and_find()
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
        return True

    def find_element(self, selector):
        if self.__element is None:
            self.__element = self.browser.find_element(*selector)
            return self.__element
        else:
            return self.__element

    def click(self):
        element = self.find_element(self.selector)
        element.click()

    def wait_and_find(self):
        wait = WebDriverWait(self.browser, Config().get_wait())
        wait.until(EC.presence_of_element_located(self.selector))
        element = self.find_element(self.selector)
        logger.info(f"New BaseElement instance saved with selector "
                    f"{self.selector}")
        return element

    def wait_and_click(self):
        element = self.wait_and_find()
        element.click()

    def move_to_element(self):
        action = ActionChains(self.browser)
        element = self.wait_and_find()
        action.move_to_element(element).perform()

    def find_elements(self):
        self.__elements_list = [BaseElement(i) for i in
                                self.browser.find_elements(*self.selector)]
        return self.__elements_list

    def wait_until_invisible(self):
        try:
            wait = WebDriverWait(self.browser, Config().get_wait())
            wait.until(EC.invisibility_of_element_located(self.selector))
        except TimeoutException:
            pass

    def get_attribute(self, attribute: str):
        element = self.wait_and_find()
        return element.get_attribute(attribute)

    def is_element_not_present(self):
        try:
            self.wait_until_invisible()
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
        return True

    def save_elements_to_list(self):
        elements = self.browser.find_elements(*self.selector)
        return elements
