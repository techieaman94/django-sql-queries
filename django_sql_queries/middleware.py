from django.utils.deprecation import MiddlewareMixin
from django.db import connection
from django.conf import settings


class SQLPrinterMiddleware(MiddlewareMixin):
    """
    Middleware to print out all SQL queries done, their count and execution time
    for each view that is processed for a request.
    """

    def process_response(self, request, response):
        indentation = 2
        sql_query_count = {}
        width = 120
        if len(connection.queries) > 0 and settings.DEBUG:
            total_time = 0.0
            for query in connection.queries:
                sql_cleaned = query["sql"].replace('"', "").replace(",", ", ")
                sql = "\033[1;31m[ %s ]\033[0m %s" % (query["time"], sql_cleaned)
                if sql_query_count.get(sql):
                    sql_query_count[sql] += 1
                else:
                    sql_query_count[sql] = 1
                total_time = total_time + float(query["time"])

            for sql, value in sql_query_count.items():
                while len(sql) > width - indentation:
                    print("%s%s" % (" " * indentation, sql[: width - indentation]))
                    sql = sql[width - indentation :]
                print(
                    "%s%s | \033[1;31m[ Count :  %s ]\033[0m\n"
                    % (" " * indentation, sql, value)
                )

            data_tuple = (" " * indentation, str(total_time), len(connection.queries))
            print(
                "\n%s\033[1;32m[ TOTAL TIME: %s seconds, TOTAL DB QUERIES: %s ]\033[0m"
                % data_tuple
            )
        return response
