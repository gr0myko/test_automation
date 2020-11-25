import xmltodict
from framework.base.singleton_metaclass import Singleton
from framework.base.utils.logger import Logger

logger = Logger.start()


class Config(metaclass=Singleton):
    def __init__(self):
        with open('config.xml', 'r') as xml_file:
            config = xmltodict.parse(xml_file.read())
            url = config['configurations']['url']
            browser_type = config['configurations']['browser']
            language = config['configurations']['lang']
            wait = int(config['configurations']['wait'])
            vk_api_url = config['configurations']['vk_api_url']
        self.url = url
        self.browser_type = browser_type
        self.language = language
        self.wait = wait
        self.vk_api_url = vk_api_url

        logger.info(f'Config file opened with {self.url} url, '
                    f'{self.browser_type} browser, {self.language} language, '
                    f'{self.wait} wait')

    def get_url(self):
        return self.url

    def get_browser_type(self):
        return self.browser_type

    def get_language(self):
        return self.language

    def get_wait(self):
        return self.wait

    def get_vk_api_url(self):
        return self.vk_api_url
