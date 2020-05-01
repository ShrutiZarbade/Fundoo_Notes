"""
    This is the note service in which various function of not is written
    like CRUD operation.
    Author: Shruti Zarbade
    Date: 10/3/2020
"""
from model.db_query import Query
db_object = Query()


class NoteServices:

    def create(self, note_data):

        response = {
            "success": False,
            "message": "something went wrong",
            "data": []
        }
        table_name = "notes"

        db_object.insert(data=note_data, table_name=table_name)

        response['success'] = True
        response['message'] = "note created successfully"
        return response

    def read(self, user_id):
        response = {
            "success": False,
            "message": "something went wrong",
        }
        read_data = db_object.read(table_name="notes", column_name='user_id', column_val=user_id)

        response['success'] = True
        response['message'] = "note read successfully"
        response['data'] = read_data
        return response

    def update(self, note_data):
        response = {
            "success": False,
            "message": "something went wrong",
        }

        # import pdb
        # pdb.set_trace()

        column_val = note_data['id']

        db_object.update(data=note_data, table_name="notes")
        response['success'] = True
        response['message'] = "note update successfully"

        return response

    def delete(self, note_data):
        response = {
            "success": False,
            "message": "Something went wrong",
        }
        note_id = note_data['id']

        db_object.delete(table_name="notes", del_id=note_id)

        response['success'] = True
        response['message'] = "note deleted successfully"
        return response

    def trashed(self, data):
        try:
            response = {
                "success": False,
                "message": "something went wrong"
            }
            note_id = data['id']
            db_object.update(data=data, table_name="notes")

            response = {
                "success": True,
                "message": "note move to trash successfully",
            }
            return response
        except Exception as e:
            print(e)
            response = response
        return response

    def archived(self, data):
        try:
            response = {
                "success": False,
                "message": "something went wrong"
            }
            note_id = data['id']
            db_object.update(data=data, table_name="notes")

            response = {
                "success": True,
                "message": "note archived successfully",
            }
            return response
        except Exception as e:
            print(e)
            response = response
        return response

    def pinned(self, data):
        try:
            response = {
                "success": False,
                "message": "something went wrong"
            }
            note_id = data['id']
            db_object.update(data=data, table_name="notes")

            response = {
                "success": True,
                "message": "note pinned successfully",
            }
            return response
        except Exception as e:
            print(e)
            response = response
        return response

    def trash_data(self):
        try:
            response = {
                "success": False,
                "message": "something went wrong"
            }
            read_data = db_object.read(table_name="notes", column_val=None, column_name=None)
            list = []
            for data in read_data:
                is_trash = data[7]
                if is_trash == 1:
                    list.append(data)
                    response = {
                        "success": True,
                        "message": "data  shown successfully",
                        "data": [list]
                    }
        except Exception as e:
            print(e)
            response = response
        return response

    def archive_data(self):
        try:
            response = {
                "success": False,
                "message": "something went wrong"
            }
            read_data = db_object.read(table_name="notes", column_val=None, column_name=None)
            list = []
            for data in read_data:
                is_archived = data[6]
                if is_archived == 1:
                    list.append(data)
                    response = {
                        "success": True,
                        "message": "data  shown successfully",
                        "data": [list]
                    }
        except Exception as e:
            print(e)
            response = response
        return response

    def pin_data(self):
        try:
            response = {
                "success": False,
                "message": "something went wrong"
            }
            read_data = db_object.read(table_name="notes", column_val=None, column_name=None)
            list = []
            for data in read_data:
                is_pin = data[5]
                if is_pin == 1:
                    list.append(data)
                    response = {
                        "success": True,
                        "message": "data  shown successfully",
                        "data": [list]
                    }
        except Exception as e:
            print(e)
            response = response
        return response






