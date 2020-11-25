from framework.base.browser import Browser
from framework.base.utils.logger import Logger

logger = Logger().start()


class BrowserExtensionsIFrame(Browser):
    @staticmethod
    def switch_to_iframe(iframe_id):
        Browser.driver.switch_to.frame(iframe_id)

    @staticmethod
    def switch_to_default():
        Browser.driver.switch_to.default_content()


class BrowserExtensionsCookies(Browser):
    @staticmethod
    def add_cookie(key, value):
        Browser.driver.add_cookie({"name": key, "value": value})
        logger.info(f"Cookie {key} added with value {value}")

    @staticmethod
    def is_cookie_present(key: str):
        if BrowserExtensionsCookies.get_cookie(key) is None:
            return False
        else:
            return True

    @staticmethod
    def delete_cookie(key: str):
        Browser.driver.delete_cookie(key)
        logger.info(f"Cookie {key} deleted")

    @staticmethod
    def get_cookie(key: str):
        return Browser.driver.get_cookie(key)

    @staticmethod
    def get_cookies():
        return Browser.driver.get_cookies()

    @staticmethod
    def delete_all_cookies():
        Browser.driver.delete_all_cookies()
        logger.info("All cookies deleted")
