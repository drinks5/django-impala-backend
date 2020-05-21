from django.db.backends.base.introspection import BaseDatabaseIntrospection, TableInfo

class DatabaseIntrospection(BaseDatabaseIntrospection):

    def get_table_list(self, cursor):
        "Returns a list of table names in the current database."
        cursor.execute("SHOW TABLES")
        return [TableInfo(row[0], {'BASE TABLE': 't', 'VIEW': 'v'}['BASE TABLE'])
                for row in cursor.fetchall()]
