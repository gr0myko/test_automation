from framework.base.utils.logger import Logger


class MYSQLutils:
    @staticmethod
    def get_query_result(cursor, query):
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def select(self, cursor, query_str):
        Logger().db_query(query_str)
        result = self.get_query_result(cursor, query_str)
        Logger().db_response(result)
        return result

    def delete(self, cursor, query):
        Logger().db_query(query)
        self.get_query_result(cursor, query)

    def insert(self, cursor, query):
        Logger().db_query(query)
        self.get_query_result(cursor, query)
