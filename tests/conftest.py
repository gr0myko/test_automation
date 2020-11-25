import pytest
from framework.base.config_class import Config
from framework.base.browser import Browser
from framework.base.utils.logger import Logger

logger = Logger.start()


@pytest.fixture(scope="function")
def browser():
    browser = Browser.start()
    Browser.maximize_window()
    browser.get(Config().get_url())
    logger.error(f"Browser opened")
    yield browser
    logger.error(f"Quiting browser")
    Browser.close()
