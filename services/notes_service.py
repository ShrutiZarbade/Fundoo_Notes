"""
    This is the note service in which various function of not is written
    like CRUD operation.
    Author: Shruti Zarbade
    Date: 10/3/2020
"""
from config.mysql_connection import db_obj
import jwt


class NoteServices:

    def create(self, note_data):

        response = {
            "success": False,
            "message": "something went wrong",
            "data": []
        }
        print(note_data, '=====>user data services')

        table_name = "note"
        print(table_name, "======>table name")

        db_obj.insert(data=note_data, table_name=table_name)

        response = {
            "success": True,
            "message": "note created successfully",
        }
        return response

    def read(self, user_id):
        response = {
            "success": False,
            "message": "something went wrong",
        }
        print(user_id, '=====>user id')
        read_data = db_obj.read(table_name="note", column_name='user_id', column_val=user_id)
        print(read_data, '=====>read_data')
        # import pickle
        # data = pickle.loads(read_data)

        # print(data,"=========>>>data")
        response = {
            "success": True,
            "message": "note read successfully",
            "data": read_data
        }
        return response

    def update(self, note_data):
        response = {
            "success": False,
            "message": "something went wrong",
        }

        # import pdb
        # pdb.set_trace()
        print(note_data, "===========>user data")

        column_val = note_data['id']

        print(column_val, "================>column_val id")

        # del note_data["id"]
        print(note_data, "===================")

        db_obj.update(data=note_data, table_name="note")
        response = {
            "success": True,
            "message": "note update successfully",
        }
        return response

    def delete(self, note_data):
        response = {
            "success": False,
            "message": "Something went wrong",
        }
        print(note_data, "=====>>>note data")

        note_id = note_data['id']
        print(note_id, "==========>note id")

        db_obj.delete(table_name="note", del_id=note_id)

        response = {
            "success": True,
            "message": "note deleted successfully",
        }
        return response




