from utils.concrete_mysql_db import ConcreteMYSQLDB


class TestMYSQL:
    def test_get_min_time_for_test(self, cursor):
        ConcreteMYSQLDB().get_min_time_for_test(cursor)

    def test_count_unique_tests_in_project(self, cursor):
        ConcreteMYSQLDB().count_unique_test_in_project(cursor)

    def test_get_tests_after_date(self, cursor):
        ConcreteMYSQLDB().select_tests_after_date(cursor)

    def test_count_tests_by_browser(self, cursor):
        ConcreteMYSQLDB().count_tests_by_browser(cursor)
