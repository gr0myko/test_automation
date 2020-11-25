from pages.welcome_page import WelcomePage
from framework.base.utils.logger import Logger
from pages.login_page import LoginPage
from pages.interests_page import InterestsPage
from framework.base.utils.string_utils import RandomString

logger = Logger.start()


class TestUserinyerface:
    DROPDOWN_DOMAIN = '.com'
    RAND_LOGIN = RandomString.get_random_string(5)
    RAND_PW = RandomString.get_random_password(RAND_LOGIN)
    RAND_DOMAIN = RandomString.get_random_string(5)

    @staticmethod
    def test_fill_in_login_forms(browser):
        welcome_page = WelcomePage()
        assert welcome_page.is_form_displayed(), "Welcome page is not displayed"

        welcome_page.click_on_next_page_link()
        login_page = LoginPage()
        assert login_page.is_form_displayed(), "Login page is not displayed"

        login_page.fill_in_password(TestUserinyerface.RAND_PW)
        login_page.fill_in_login(TestUserinyerface.RAND_LOGIN)
        login_page.fill_in_domain(TestUserinyerface.RAND_DOMAIN)
        login_page.choose_dropdown_domain(TestUserinyerface.DROPDOWN_DOMAIN)
        login_page.click_on_terms_agree_checkbox()
        login_page.click_on_next_button()
        interests_page = InterestsPage()
        assert interests_page.is_form_displayed(), \
            "Interests page is not displayed"

        interests_page.clear_all_interests()
        interests_page.click_on_random_interests(3)
        logger.info("Test Step: Random interests clicked")
        interests_page.upload_avatar()

    @staticmethod
    def test_accept_cookies(browser):
        welcome_page = WelcomePage()
        assert welcome_page.is_form_displayed(), "Welcome page is not displayed"

        welcome_page.click_on_next_page_link()
        login_page = LoginPage()
        assert login_page.is_form_displayed(), "Login page is not displayed"

        login_page.accept_cookies()
        assert login_page.is_cookies_form_displayed() is False, \
            "Cookies form is not hidden"

    @staticmethod
    def test_hide_help_form(browser):
        welcome_page = WelcomePage()
        assert welcome_page.is_form_displayed(), "Welcome page is not displayed"

        welcome_page.click_on_next_page_link()
        login_page = LoginPage()
        assert login_page.is_form_displayed(), "Login page is not displayed"

        login_page.hide_help_form()
        login_page.wait_help_form_to_hide()
        logger.info("Wait for help form to become visible")
        assert login_page.is_help_form_hidden(), "Help form is not hidden"

    @staticmethod
    def test_timer_starts_from_0_on_login_page(browser):
        welcome_page = WelcomePage()
        assert welcome_page.is_form_displayed(), "Welcome page is not displayed"

        welcome_page.click_on_next_page_link()
        login_page = LoginPage()
        assert login_page.is_form_displayed(), "Login page is not displayed"

        assert login_page.get_timer_value() == TestUserinyerface.TIMER_START, "Timer should start with 0"
