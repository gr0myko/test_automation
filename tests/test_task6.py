import pytest

from framework.base.utils.logger import Logger
from framework.base.utils.api_utils.status_code import StatusCode
from utils.typicode_api import TypicodeApi
from framework.base.utils.api_utils.post import Post
from framework.base.utils.api_utils.user import User

from tests.data.test_data import RANDOM_TITLE, RANDOM_BODY, NEW_POST, USER_5

logger = Logger.start()


class TestAPI:
    RANDOM_TITLE = RANDOM_TITLE
    RANDOM_BODY = RANDOM_BODY
    NEW_POST = NEW_POST
    USER_5 = USER_5
    TYPICODE_API = TypicodeApi()

    def test_get_all_posts(self):
        posts = self.TYPICODE_API.get_sorted_posts('id')

        assert self.TYPICODE_API.check_status(), "Request status code is not correct"
        assert posts, "Request result is empty"

    @pytest.mark.parametrize("post_id, user_id_value, id_value", [('99', 10, 99)])
    def test_get_99_post(self, post_id, user_id_value, id_value):
        post_99 = self.TYPICODE_API.get_post(post_id)

        assert self.TYPICODE_API.check_status(), "Request status code is not correct"
        assert post_99.get_value('userId') == user_id_value, \
            "UserId value is not correct"
        assert post_99.get_value('id') == id_value, "Id value is not correct"
        assert post_99.get_value('title'), "Title value is empty"
        assert post_99.get_value('body'), "Title value is empty"

    @pytest.mark.parametrize("post_id", ['150'])
    def test_get_150_post(self, post_id):
        post_150 = self.TYPICODE_API.get_post(post_id)

        assert self.TYPICODE_API.check_status(StatusCode.NOT_FOUND), \
            "Request status code is not correct, 404 expected"
        assert post_150.is_empty(), "Empty response expected"

    def test_post_new_post(self):
        new_post = Post(self.NEW_POST)
        created_post = self.TYPICODE_API.new_post(self.NEW_POST)

        assert self.TYPICODE_API.check_status(StatusCode.CREATED), \
            "Post was not created"
        assert created_post == new_post, "Values of post are not correct"

    @pytest.mark.parametrize("user_id", [5])
    def test_get_all_users(self, user_id):
        user_5 = User(self.USER_5)
        users = self.TYPICODE_API.get_users()

        assert self.TYPICODE_API.check_status(), "Request status code is not correct"
        assert users, "Request result is empty"

        user_5_from_list = User.get_user_from_list(users, user_id)

        assert user_5_from_list == user_5, "Comparison failed"

    @pytest.mark.parametrize("user_id", ['5'])
    def test_get_user_5(self, user_id):
        user_5 = User(self.USER_5)
        user = self.TYPICODE_API.get_user(user_id)

        assert self.TYPICODE_API.check_status(), "Request status code is not correct"
        assert user == user_5, "Comparison failed"
