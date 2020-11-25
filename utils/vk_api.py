from framework.base.utils.api_utils.api_utils import APIutils
from framework.base.utils.api_utils.request_type import RequestType
from utils.post import Post
from utils.photo import Photo
from utils.comment import Comment
from tests.data.api_config import TOKEN, VERSION


class VKAPI:
    PARAMS = {'access_token': TOKEN, 'v': VERSION}

    def __init__(self):
        self.request = None

    def get_response(self):
        return self.request.get_json_result()['response']

    def create_post_on_my_page(self, message):
        self.PARAMS['message'] = message
        self.request = APIutils('/wall.post?', RequestType.POST, self.PARAMS)
        new_post = Post(self.get_response())
        return new_post

    def get_upload_url(self, group_id):
        self.PARAMS['group_id'] = group_id
        self.request = APIutils('/photos.getWallUploadServer?',
                                RequestType.POST, self.PARAMS)
        post = Post(self.get_response())
        return post.get_value('upload_url')

    def get_parameters_for_photo_saving(self, group_id, filename):
        self.request = APIutils(self.get_upload_url(group_id), RequestType.POST,
                                files={'photo': open(filename, "rb")})
        return self.request.get_values()

    def save_wall_photo(self, group_id, filename):
        params = self.get_parameters_for_photo_saving(group_id, filename)
        params['access_token'] = TOKEN
        params['v'] = VERSION
        params['group_id'] = group_id
        self.request = APIutils('/photos.saveWallPhoto?',
                                RequestType.POST, params)
        photo = Photo(self.get_response()[0])
        return photo

    def edit_post_on_my_page(self, post_id, group_id, message=None, file=None):
        self.PARAMS['post_id'] = str(post_id)
        self.PARAMS['owner_id'] = group_id
        if file is None:
            if message is None:
                self.request = APIutils('/wall.edit?', RequestType.POST, self.PARAMS)
                post = Post(self.get_response())
            else:
                self.PARAMS['message'] = message
                self.request = APIutils('/wall.edit?', RequestType.POST, self.PARAMS)
                post = Post(self.get_response())
        else:
            photo = self.save_wall_photo(group_id, file)
            self.PARAMS['attachments'] = 'photo' + str(photo.get_value('owner_id')) + \
                                     '_' + str(photo.get_value('id'))
            self.PARAMS['message'] = message
            self.request = APIutils('/wall.edit?', RequestType.POST, self.PARAMS)
            post = Post(self.get_response())
            post.add_attribute('photo_id', str(photo.get_value('owner_id')) +
                               '_' + str(photo.get_value('id')))
        return post

    def add_comment(self, post_id):
        self.PARAMS['post_id'] = post_id
        self.request = APIutils('/wall.createComment?', RequestType.POST, self.PARAMS)
        comment = Comment(self.get_response())
        return comment

    def check_post_is_liked_by_user(self, post_id, user_id):
        self.PARAMS['item_id'] = post_id
        self.PARAMS['user_id'] = user_id
        self.PARAMS['type'] = 'post'
        self.request = APIutils('/likes.isLiked?', RequestType.POST, self.PARAMS)
        post = Post(self.get_response())
        return post.get_value('liked') == 1

    def delete_post(self, post_id, owner_id):
        self.PARAMS['owner_id'] = owner_id
        self.PARAMS['post_id'] = post_id
        self.request = APIutils('/wall.delete?', RequestType.POST, self.PARAMS)
        return self.request.get_request_text()
