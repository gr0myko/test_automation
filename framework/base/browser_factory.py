from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from framework.base.config_class import Config


class BrowserFactory:
    @staticmethod
    def get_driver():
        options = Options()
        options.add_experimental_option("prefs", {
            "safebrowsing.enabled": True,
            "intl.accept_languages": f"{Config().get_language()}"
        })

        if Config().get_browser_type() == 'Chrome':
            return webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
        elif Config().get_browser_type() == 'Firefox':
            return webdriver.Firefox(executable_path=GeckoDriverManager().install())
        else:
            raise Exception(f"{Config().get_browser_type()} is not a supported browser")
