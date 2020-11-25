from framework.base.utils.api_utils.api_utils import APIutils
from framework.base.utils.api_utils.request_type import RequestType
from framework.base.utils.api_utils.post import Post
from framework.base.utils.api_utils.user import User
from framework.base.utils.api_utils.status_code import StatusCode


class TypicodeApi:
    def __init__(self):
        self.request = None

    def get_post(self, post_id: str):
        self.request = APIutils('/posts/'+post_id, RequestType.GET)
        post = Post(self.request.get_values())
        return post

    def get_posts(self):
        self.request = APIutils('/posts', RequestType.GET)
        posts = []
        for dict_data in self.request.get_values():
            post = Post(dict_data)
            posts.append(post)
        return posts

    def get_sorted_posts(self, key):
        self.request = APIutils('/posts', RequestType.GET)
        posts = []
        for dict_data in self.request.sort_values('id'):
            post = Post(dict_data)
            posts.append(post)
        return posts

    def get_user(self, user_number: str):
        self.request = APIutils('/users/'+user_number, RequestType.GET)
        user = User(self.request.get_values())
        return user

    def get_users(self):
        self.request = APIutils('/users', RequestType.GET)
        users = []
        for dict_data in self.request.get_values():
            user = User(dict_data)
            users.append(user)
        return users

    def check_status(self, status_code=StatusCode.SUCCESS):
        return self.request.check_status(status=status_code)

    def new_post(self, dict_data):
        self.request = APIutils('/posts', RequestType.POST, dict_data)
        post = Post(self.request.get_values())
        return post
