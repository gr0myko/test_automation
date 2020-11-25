import xmltodict
import os
from framework.base.singleton_metaclass import Singleton


class ConfigMYSQL(metaclass=Singleton):
    def __init__(self):
        with open(f'mysql_config.xml', 'r') as xml_file:
            config = xmltodict.parse(xml_file.read())
            user = config['configurations']['user']
            host = config['configurations']['host']
            password = config['configurations']['password']
            database = config['configurations']['database']
        self.user = user
        self.host = host
        self.password = password
        self.database = database

    def get_user(self):
        return self.user

    def get_host(self):
        return self.host

    def get_password(self):
        return self.password

    def get_database(self):
        return self.database
