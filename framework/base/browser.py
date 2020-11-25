from framework.base.browser_factory import BrowserFactory
from framework.base.alert_actions import AlertActions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.base.config_class import Config
from framework.elements.alert import Alert


class Browser:
    driver = None

    @staticmethod
    def start():
        if Browser.driver is None:
            Browser.driver = BrowserFactory.get_driver()
            return Browser.driver
        else:
            return Browser.driver

    @staticmethod
    def close():
        Browser.driver.quit()
        Browser.driver = None

    @staticmethod
    def refresh():
        Browser.driver.refresh()

    @staticmethod
    def maximize_window():
        Browser.driver.maximize_window()

    @staticmethod
    def handle_alert(action: AlertActions):
        alert = Browser.switch_to_alert()
        if action == AlertActions.ACCEPT:
            alert.accept()
        else:
            alert.dismiss()

    @staticmethod
    def get_alert_text():
        alert = Browser.switch_to_alert()
        return alert.get_text()

    @staticmethod
    def send_text_to_prompt(text):
        prompt_alert = Browser.switch_to_alert()
        prompt_alert.send_text_to_alert(text)

    @staticmethod
    def switch_to_alert():
        WebDriverWait(Browser.driver, Config().get_wait()).until(EC.alert_is_present())
        alert = Alert(Browser.driver.switch_to.alert)
        return alert
