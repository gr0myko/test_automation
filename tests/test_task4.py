from pages.main_page import MainPage
import pytest
from framework.base.utils.logger import Logger
from framework.base.browser_extensions import BrowserExtensionsIFrame
from framework.base.utils.string_utils import RandomString

logger = Logger.start()


class TestIFrame:
    @staticmethod
    @pytest.mark.parametrize("header", [("An iFrame containing the TinyMCE "
                                         "WYSIWYG Editor")])
    def test_handle_iframe(browser, header):
        main_page = MainPage()
        logger.info(f"Test step: checking form is displayed")
        assert main_page.is_form_displayed(header) is True, \
            "Form is not displayed"

        logger.info(f"Test step: switch to {main_page.get_frame_id()} "
                    f"iframe and add random string")
        rand_string = RandomString().get_random_string(10)
        BrowserExtensionsIFrame.switch_to_iframe(main_page.get_frame_id())
        main_page.delete_text_in_frame()
        logger.info(f"{rand_string} send to iframe input")
        main_page.send_text_to_frame(rand_string)
        print(main_page.get_frame_text())
        print(rand_string)
        assert main_page.get_frame_text() == rand_string, \
            "Random string is not displayed"

        logger.info(f"Test step: select all text and press bold button")
        main_page.select_text_in_frame()
        BrowserExtensionsIFrame.switch_to_default()
        main_page.click_on_bold_button()
        BrowserExtensionsIFrame.switch_to_iframe(main_page.get_frame_id())
        assert main_page.is_text_bold_in_frame() is True, "Input text is not bold"
