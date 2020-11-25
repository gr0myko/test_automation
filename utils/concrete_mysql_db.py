from framework.base.utils.mysql_utils.mysql_utils import MYSQLutils
from tests.data.queries import MIN_TIME_QUERY, PROJECT_TEST_COUNT_QUERY, \
    PROJECTS_BY_DATE_QUERY, BROWSER_TEST_COUNT_QUERY


class ConcreteMYSQLDB:
    def __init__(self):
        self.DB = MYSQLutils()

    def get_min_time_for_test(self, cursor):
        result = self.DB.select(cursor, MIN_TIME_QUERY)
        return result

    def count_unique_test_in_project(self, cursor):
        result = self.DB.select(cursor, PROJECT_TEST_COUNT_QUERY)
        return result

    def select_tests_after_date(self, cursor):
        result = self.DB.select(cursor, PROJECTS_BY_DATE_QUERY)
        return result

    def count_tests_by_browser(self, cursor):
        result = self.DB.select(cursor, BROWSER_TEST_COUNT_QUERY)
        return result
