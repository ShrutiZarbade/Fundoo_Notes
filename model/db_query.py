"""
This is the file for Database operation in which various mysql query is written
Author: Shruti Zarbade
Date: 10/3/2020
"""
from config.mysql_connection import Connection


class Query:  # data access layer
    """
        This class define all the mysql query in which
        all the query are dynamic and used for all tables into the database.
    """
    def __init__(self):
        self.mydb = Connection()

    # query for inserting data into table
    def insert(self, data, table_name):
        column = []
        rows_values = []
        val = []
        for key, values in data.items():
            column.append(key)
            rows_values.append("%s")
            val.append(values)
        column = ','.join(column)
        val_ = ','.join(['%s']*len(val))
        query = f''' Insert into %s (%s) values (%s)''' % (table_name, column, val_)
        self.mydb.query_execute(query, value=val)

    # query for reading data from database
    def read(self, table_name, column_name, column_val):
        val = (column_val, )
        if column_val is None and column_name is None:
            query = f"SELECT * FROM {table_name}"
            result = self.mydb.run_query(query)

        else:
            query = f"SELECT * FROM {table_name} WHERE {column_name}= %s"
            result = self.mydb.run_query(query, value=val)
        return result

    # query for updating data into the database
    def update(self, data, table_name):
        column = []
        rows_values = []
        val = []
        id = 0
        print(data, '---->data')
        for key, values in data.items():
            if key != 'id':
                column.append(key)
                val.append(values)
            if key == 'id':
                id = values

        val.append(id)
        set_tokens = ','.join([f'{x}=%s' for x in column])
        query = f"UPDATE {table_name} SET {set_tokens} WHERE id = %s"
        self.mydb.query_execute(query,value=val)

    # query for deleting data from the database
    def delete(self, table_name, del_id):

        query = f"DELETE FROM {table_name} WHERE id={del_id}"
        self.mydb.query_execute(query, value=None)

