from selenium.webdriver.common.by import By
from framework.elements.box import Box
from framework.elements.text import Text
from framework.elements.button import Button
from framework.elements.image import Image


class PostModel:
    def __init__(self, post_id):
        self.post_id = post_id
        self.id_locator = "//div[contains(@id, '{}')]".format(self.post_id)
        self.new_post_locator = self.id_locator + "//div[contains(@class," \
                                                  "'wall_post_text')]"
        self.post_author_locator = self.id_locator + "//a[@class='author']"
        self.comment_text_locator = self.id_locator + "//div[@class=" \
                                                      "'wall_reply_text']"
        self.comment_author_locator = "//div[@class='replies']" \
                                      + self.id_locator + \
                                      "//div[@class='reply_author']//a"
        self.like_button_locator = self.id_locator + "//a[contains(@class, " \
                                                     "'like_btn')]"
        self.next_comment_locator = self.id_locator + "//a[contains(@class, " \
                                                      "'replies_next')]"
        self.image_locator = self.id_locator + "//a[contains(@class," \
                                               "'image_cover')]"

        self.new_post = Box((By.XPATH, self.new_post_locator))
        self.comment = Text((By.XPATH, self.comment_text_locator))
        self.next_comment = Button((By.XPATH, self.next_comment_locator))
        self.like_button = Button((By.XPATH, self.like_button_locator))
        self.image = Image((By.XPATH, self.image_locator))
        self.post_author = Box((By.XPATH, self.post_author_locator))
