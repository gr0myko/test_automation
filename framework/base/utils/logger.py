import logging
from framework.base.singleton_metaclass import Singleton


class Logger(metaclass=Singleton):
    LOG_FORMAT = '%(asctime)s %(levelname)s:\t%(message)s'

    @staticmethod
    def start():
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(Logger.LOG_FORMAT)
        file_handler = logging.FileHandler('actions.log', mode='w')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
