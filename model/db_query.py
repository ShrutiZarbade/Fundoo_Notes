"""
This is the file for Database operation in which various mysql query is written
Author: Shruti Zarbade
Date: 10/3/2020
"""


class DbOperation:

    def insert_data(self, data, table_name):
        column = []
        rows_values = []
        val = []
        for key, values in data.items():
            column.append(key)
            rows_values.append("%s")
            val.append(values)
        column = ','.join(column)
        print(column, '==========>column')
        val_ = ','.join(['%s']*len(val))
        print(val_, "==========>val_")
        query = f''' Insert into %s (%s) values (%s)''' % (table_name, column, val_)
        print(query, val, "========>>query")
        return query, val

    def read_data(self, table_name, column_name, column_val):
        print(table_name, column_name, column_val)
        if column_val is None and column_name is None:
            sql = f"SELECT * FROM {table_name}"
        else:
            sql = f" SELECT * FROM {table_name} WHERE {column_name}={column_val}"
        return sql

    def update_data(self, data, table_name):
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
        print(set_tokens, '----set_t')
        sql = f"UPDATE {table_name} SET {set_tokens} WHERE id = %s"
        print(sql, '---->q')
        print(val, '---->val')

        return sql, val

    def delete_data(self, table_name, del_id):

        sql = f"DELETE FROM {table_name} WHERE id={del_id}"
        return sql

    def update_note(self, user_id):
        sql = f"UPDATE title,description,colour from note WHERE user_id={user_id}"
        return sql

    def read_par_data(self, email):
        sql = f"SELECT * FROM users WHERE email='"+email+"'"
        return sql

    def read_last_data(self):
        sql = f"SELECT id, email FROM user WHERE id=(SELECT MAX(id) FROM user)"
        return sql

