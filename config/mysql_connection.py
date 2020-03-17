import mysql.connector
from model.db_query import DbOperation
query_obj = DbOperation()
# import os
from dotenv import load_dotenv
load_dotenv()


class MysqlCon:

    def __init__(self, host='localhost', port=6379, db=0, ):
        self.host = host
        self.port = port
        self.db = db
        self.connection = self.connect()

    def connect(self, **kwargs):
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="password",
            database="fundoo_db"
        )
        return mydb

    def create(self):
        pass

    def insert(self, data, table_name):

        sql, val = query_obj.insert_data(data=data, table_name=table_name)
        self.mycursor = self.connection.cursor()
        self.mycursor.execute(sql, val)
        self.connection.commit()

    def read(self, table_name, column_name, column_val):
        query = query_obj.read_data(table_name, column_name, column_val)
        self.mycursor = self.connection.cursor()
        self.mycursor.execute(query)
        data = self.mycursor.fetchall()
        return data

    def update(self, data, table_name):
        sql, val = query_obj.update_data(data, table_name)
        self.mycursor = self.connection.cursor()
        self.mycursor.execute(sql, val)
        self.connection.commit()

    def delete(self, table_name, del_id):
        sql = query_obj.delete_data(table_name, del_id)
        self.mycursor = self.connection.cursor()
        self.mycursor.execute(sql)
        self.connection.commit()

    def last_data(self):
        sql = query_obj.read_last_data()
        self.mycursor = self.connection.cursor()
        self.mycursor.execute(sql)
        data = self.mycursor.fetchone()
        return data

    def drop(self, table_name=None):
        pass

    def disconnect(self):
        self.connection.close()


db_obj = MysqlCon()
con = db_obj.connection

