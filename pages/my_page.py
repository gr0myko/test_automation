from selenium.webdriver.common.by import By

from framework.base.utils.string_utils import RandomString
from framework.elements.box import Box
from framework.base.base_page import BasePage
from framework.elements.text import Text
from pages.post import PostModel


class MyPage(BasePage):
    def __init__(self):
        self.id_locator = "//div[contains(@id, '{}')]"
        self.my_page_header_locator = (By.XPATH, "//div[@class='page_top']")
        self.comment_author_locator = "//div[@class='replies']" \
                                      + self.id_locator + \
                                      "//div[@class='reply_author']//a"
        self.submit_post_box_locator = (By.XPATH, "//div[@id='submit_post_box']")
        self.profile_wall_locator = (By.XPATH, "//div[@id='profile_wall']")


    def is_form_displayed(self):
        profile_wall = Box(self.profile_wall_locator)
        return profile_wall

    @staticmethod
    def get_post_text(post_id):
        return PostModel(post_id).new_post.get_text()

    @staticmethod
    def get_post_author(post_id):
        post = PostModel(post_id)
        return RandomString.get_digits(post.post_author.get_attribute('href'))

    def check_text_and_author_in_post(self, post_id, text):
        return self.get_post_text(post_id) == text and \
               self.get_post_author(post_id) == self.get_owner_id()

    @staticmethod
    def is_comment_under_post(post_id):
        post = PostModel(post_id)
        if post.next_comment.is_element_present():
            post.next_comment.click()
        else:
            pass
        return post.comment.is_element_present()

    def check_comment_author(self, comment_id):
        author = Text((By.XPATH, self.comment_author_locator.format(comment_id)))
        return author.get_attribute('data-from-id') == self.get_owner_id()

    @staticmethod
    def like_post(post_id):
        PostModel(post_id).like_button.wait_and_click()

    @staticmethod
    def check_post_is_deleted(post_id):
        return PostModel(post_id).new_post.is_element_not_present()

    def get_owner_id(self):
        submit_post_box = Box(self.submit_post_box_locator)
        return submit_post_box.get_attribute('data-oid')

    @staticmethod
    def get_photo_id(post_id):
        return PostModel(post_id).image.get_attribute('data-photo-id')
