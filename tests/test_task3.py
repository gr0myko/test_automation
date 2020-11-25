from pages.main_page import MainPage
from framework.base.browser_extensions import BrowserExtensionsCookies
from framework.base.utils.logger import Logger

logger = Logger.start()


class TestCookies:
    KEY_1, KEY_2, KEY_3 = [f"example_key_{a}" for a in range(1, 4)]
    VALUE_1, VALUE_2, VALUE_3 = [f"example_value_{a}" for a in range(1, 4)]

    @staticmethod
    def test_operations_with_cookies(browser):
        main_page = MainPage()
        logger.info(f"Test step: main page is displayed")
        assert main_page.is_form_displayed() is True, "Main page is not displayed"
        for key, value in [(TestCookies.KEY_1, TestCookies.VALUE_1),
                           (TestCookies.KEY_2, TestCookies.VALUE_2),
                           (TestCookies.KEY_2, TestCookies.VALUE_2)]:
            BrowserExtensionsCookies.add_cookie(key, value)
            assert BrowserExtensionsCookies.is_cookie_present(key) is True, \
                "Cookie is not present"

        logger.info(f"Test step: delete first cookie")
        BrowserExtensionsCookies.delete_cookie(TestCookies.KEY_1)
        assert BrowserExtensionsCookies.is_cookie_present(TestCookies.KEY_1) is False, \
            "Cookie is still present"

        logger.info(f"Test step: change value of third cookie")
        new_value = "example_value_300"
        BrowserExtensionsCookies.add_cookie(TestCookies.KEY_3, new_value)
        assert BrowserExtensionsCookies.get_cookie(TestCookies.KEY_3)["value"] == new_value, \
            "Cookie's value is not correct"

        logger.info(f"Test step: delete all cookies")
        BrowserExtensionsCookies.delete_all_cookies()
        assert not BrowserExtensionsCookies.get_cookies(), "Cookie is still present"
