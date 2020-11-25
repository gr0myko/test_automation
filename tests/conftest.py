import pytest
from framework.base.config_class import Config
from framework.base.browser import Browser
from framework.base.utils.logger import Logger
import mysql.connector
from framework.base.utils.mysql_utils.mysql_config_class import ConfigMYSQL

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


@pytest.fixture(scope="function")
def cursor():
    connection = mysql.connector.connect(host=ConfigMYSQL().get_host(),
                                         user=ConfigMYSQL().get_user(),
                                         password=ConfigMYSQL().get_password(),
                                         database=ConfigMYSQL().get_database())
    cursor = connection.cursor()
    yield cursor
    cursor.close()
