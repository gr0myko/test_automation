from pages.main_page import MainPage
from framework.base.browser import Browser
from framework.base.alert_actions import AlertActions
from framework.base.utils.string_utils import RandomString
import pytest
from framework.base.utils.logger import Logger

logger = Logger.start()


class TestAlerts:
    @staticmethod
    @pytest.mark.parametrize("alert_text, alert_result, confirm_text,"
                             " confirm_result, prompt_text, prompt_result",
                             [("I am a JS Alert", "You successfuly clicked an alert",
                              "I am a JS Confirm", "You clicked: Ok",
                              "I am a JS prompt", "You entered: {}")])
    def test_correct_alert_shown(browser, alert_text, alert_result, confirm_text,
                                 confirm_result, prompt_text, prompt_result):
        main_page = MainPage()
        main_page.click_on_alert_button()
        logger.info(f"Checking alert text: "
                    f"{Browser.get_alert_text()} = {alert_text}")
        assert Browser.get_alert_text() == alert_text, "Wrong alert text found"
        Browser.handle_alert(AlertActions.ACCEPT)
        assert main_page.get_result_text() == alert_result, "Wrong result text found"
        main_page.click_on_confirm_button()
        logger.info(f"Checking confirm text: "
                    f"{Browser.get_alert_text()} = {confirm_text}")
        assert Browser.get_alert_text() == confirm_text, "Wrong confirm text found"
        Browser.handle_alert(AlertActions.ACCEPT)
        assert main_page.get_result_text() == confirm_result, "Wrong result text found"
        main_page.click_on_prompt_button()
        logger.info(f"Checking prompt text: "
                    f"{Browser.get_alert_text()} = {prompt_text}")
        assert Browser.get_alert_text() == prompt_text, "Wrong prompt text found"
        rand_string = RandomString().get_random_string(10)
        logger.info(f"Random string for prompt input: {rand_string}")
        Browser.send_text_to_prompt(rand_string)
        Browser.handle_alert(AlertActions.ACCEPT)
        assert main_page.get_result_text() == prompt_result.format(rand_string), "Wrong result text found"
