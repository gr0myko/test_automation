from framework.base.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.elements.box import Box
from framework.elements.checkbox import Checkbox
from framework.base.utils.list_utils import ListUtils
from framework.elements.button import Button


class InterestsPage(BasePage):
    def __init__(self):
        self.interests_locator = (By.XPATH,
                                  "//div[@class='avatar-and-interests']")
        self.unsellect_all_locator = (By.XPATH,
                                      "//label[@for='interest_unselectall']")
        self.all_interests_locator = (By.XPATH,
                                      "//span[contains(@class,'checkbox')]//label")
        self.random_interest_locator = "//label[@for='{}']"
        self.upload_button_locator = (By.XPATH,
                                      "//a[contains(@class,'upload-button')]")
        self.hidden_input_locator = (By.XPATH,
                                     "//a[contains(@class,'upload-button')]"
                                     "//input[@type='file']")

    def is_form_displayed(self):
        interests_box = Box(self.interests_locator)
        return interests_box.is_element_present()

    def clear_all_interests(self):
        unsellect_all_checkbox = Checkbox(self.unsellect_all_locator)
        unsellect_all_checkbox.click()

    def get_all_interests(self):
        all_interests = Checkbox(self.all_interests_locator)
        interests_list = all_interests.save_elements_to_list()
        interests = ListUtils.get_attr_list_from_elements(interests_list, 'for')
        return interests

    def choose_random_interests(self, number: int):
        interests = InterestsPage.get_all_interests(self)
        interests.remove('interest_selectall')
        interests.remove('interest_unselectall')
        random_interests = ListUtils.get_random_elements(interests, number)
        return random_interests

    def click_on_random_interests(self, number: int):
        random_interests = InterestsPage.choose_random_interests(self, number)
        for i in random_interests:
            chosen_interest = Checkbox((By.XPATH,
                                        self.random_interest_locator.format(i)))
            chosen_interest.click()

    def upload_avatar(self):
        upload_button = Button(self.upload_button_locator)
        upload_button.click()
