from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.my_page import MyPage
from pages.menu_items import MenuItems
from utils.vk_api import VKAPI
from tests.data.test_data_config import EMAIL, PASSWORD, PHOTO, MESSAGE, EDITED_MESSAGE


class TestVKAPI:
    VK_API = VKAPI()

    def test_handle_posts_on_my_page(self, browser):
        auth_page = AuthPage()
        assert auth_page.is_form_displayed(), "Authorization page is not opened"
        auth_page.authorize(EMAIL, PASSWORD)
        main_page = MainPage()
        assert main_page.is_form_displayed(), "Main page is not opened"
        main_page.main_menu.select_item(MenuItems.MY_PAGE)

        my_page = MyPage()
        assert my_page.is_form_displayed(), "My page is not opened"
        new_post = self.VK_API.create_post_on_my_page(MESSAGE)
        post_id = new_post.get_value('post_id')
        owner_id = my_page.get_owner_id()
        assert my_page.check_text_and_author_in_post(post_id, MESSAGE), \
            "New post is not correct"

        edited_post = self.VK_API.edit_post_on_my_page(post_id, owner_id,
                                                       EDITED_MESSAGE,
                                                       PHOTO)
        assert my_page.get_post_text(post_id) == EDITED_MESSAGE, \
            "Edited message is not correct"
        assert my_page.get_photo_id(post_id) == edited_post.get_value('photo_id'), \
            "Photo id is not correct"

        comment = self.VK_API.add_comment(post_id)
        assert my_page.is_comment_under_post(post_id), \
            "Comment is not displayed under post"
        assert my_page.check_comment_author(comment.get_value('comment_id')), \
            "Comment author is not correct"

        my_page.like_post(post_id)
        assert self.VK_API.check_post_is_liked_by_user(post_id, owner_id), \
            "Post is not liked by user"

        self.VK_API.delete_post(post_id, owner_id)
        assert my_page.check_post_is_deleted(post_id), "Post is not deleted"
