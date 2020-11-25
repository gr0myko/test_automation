import xmltodict
import os
from framework.base.config_class import Config
from framework.base.singleton_metaclass import Singleton


class ConfigLoc(metaclass=Singleton):
    def __init__(self):
        with open(f'{os.getcwd()}\\tests\\data\\localization\\'
                  f'menu_items_{Config().get_language()}.xml',
                  'r', encoding="utf8") as local_file:
            config = xmltodict.parse(local_file.read())
            my_page = config['localization']['my_page']
        self.my_page = my_page

    def get_my_page(self):
        return self.my_page
