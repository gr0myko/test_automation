import logging
from framework.base.singleton_metaclass import Singleton


class Logger(metaclass=Singleton):
    LOG_FORMAT = '%(asctime)s %(levelname)s:\t%(message)s'

    def __init__(self):
        self.logger = self.start()

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

    def db_query(self, query):
        self.logger.info(f"SQL query: \n{query}")

    def db_response(self, response):
        self.logger.info(f"Response from database ({len(response)} rows): \n")
        for row in response:
            row = tuple([str(i) for i in row])
            self.logger.info(f"{' | '.join(row)}")
        self.logger.info(f"\n")
