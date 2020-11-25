import os
from framework.base.utils.string_utils import RandomString

EMAIL = ""
PASSWORD = ""
PHOTO = os.getcwd() + '\\tests\\data\\vk_api.jpg'
MESSAGE = RandomString.get_random_string(10)
EDITED_MESSAGE = MESSAGE + ' edited'
