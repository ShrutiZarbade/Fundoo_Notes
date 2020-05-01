"""
This is file indicates for mysql connection
Author: Shruti Zarbade
"""
import os
from dotenv import load_dotenv
import mysql.connector
from config.singleton import singleton
load_dotenv()


@singleton
class Connection:

    def __init__(self, **kwargs):
        self.connection = self.connect(**kwargs)
        self.mycursor = self.connection.cursor()

    # this function create the connection
    def connect(self, **kwargs):
        mydb = mysql.connector.connect(
            host=kwargs['host'],
            user=kwargs['user'],
            passwd=kwargs['passwd'],
            database=kwargs['database']
        )
        return mydb

    # this function fetch the data from the database
    def run_query(self, query, value=None):
        self.mycursor.execute(query, value)
        return self.mycursor.fetchall()

    # this function executes the data in database
    def query_execute(self, query,value=None):
        self.mycursor.execute(query,value)
        self.connection.commit()

    # this function is to disconnect the connection
    def disconnect(self):
        self.connection.close()


con = Connection(host=os.getenv("mysql_host"),
                 user=os.getenv("mysql_user"),
                 passwd=os.getenv("mysql_passwd"),
                 database=os.getenv("mysql_database"))


