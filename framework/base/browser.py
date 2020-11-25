from framework.base.browser_factory import BrowserFactory


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
