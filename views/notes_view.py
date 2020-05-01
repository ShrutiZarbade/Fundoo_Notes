"""
This is the notes view in which the validation of note is done
Author: Shruti Zarbade
Date: 10/3/2020
"""
import json
import jwt


class Notes:

    def create_notes(self, that=None):
        try:
            response = {
                "success": False,
                "message": "something went wrong",
                "data": []
            }

            # read the content from headers in json format
            content_length = int(that.headers['Content-Length'])
            body = that.rfile.read(content_length)
            json_data = json.loads(body)

            # decode the token present in headers and find the user_id
            token = that.headers['token']

            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            user_id = payload['id']
            json_data['user_id'] = user_id

            response = {
                "success": True,
                "message": "Notes created Successfully",
                "data": [json_data]
            }
        except Exception as e:
            response = response

        return response

    def read_notes(self, that=None):
        try:
            response = {
                "success": False,
                "message": "something went wrong ",
                "data": []
            }
            token = that.headers['token']
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            user_id = payload['id']
            response = {
                "success": True,
                "message": "note read successfully",
                "data": [user_id]
            }
        except Exception as e:
            response = response

        return response

    def update_notes(self, that=None):
        try:
            response = {
                "success": False,
                "message": "something went wrong ",
                "data": []
            }

            # import pdb
            # pdb.set_trace()
            content_length = int(that.headers['Content-Length'])
            data_body = that.rfile.read(content_length)
            data = json.loads(data_body)

            response = {
                "success": True,
                "message": "Note update Successfully",
                "data": [data]
                }
        except Exception as e:
            response = response

        return response

    def delete_notes(self, that=None):
        try:
            response = {
                "success": False,
                "message": "something went wrong ",
            }
            content_length = int(that.headers['Content-Length'])
            data_body = that.rfile.read(content_length)
            note_id = json.loads(data_body)

            response = {
                "success": True,
                "message": "note deleted successfully",
                "data": [note_id]
            }
        except Exception as e:
            response = response

        return response

    def is_pinned(self, that=None):
        try:
            response = {
                "success": False,
                "message": "something went wrong",
            }
            length = int(that.headers['content-length'])
            data = that.rfile.read(length)
            json_data = json.loads(data)

            response = {
                "success": True,
                "message": "data is valid",
                "data": [json_data]
            }
        except Exception as e:
            print(e)
            response = response

        return response

    def is_trashed(self, that=None):
        try:
            response = {
                "success": False,
                "message": "something went wrong"
            }

            length = int(that.headers['Content-Length'])
            data = that.rfile.read(length)
            json_data = json.loads(data)

            if json_data['id'] is None:
                raise ValueError("You have to given the id of a note")

            response = {
                "success": True,
                "message": " Note Data is valid",
                "data": [json_data]
            }

        except ValueError:
            return response
        except Exception as e:
            print(e)
            response = response
        return response

    def is_archived(self, that=None):
        try:
            response = {
                "success": False,
                "message": "something went wrong"
            }

            length = int(that.headers['Content-Length'])
            data = that.rfile.read(length)
            json_data = json.loads(data)
            print(json_data, "===============>data")

            if json_data['id'] is None:
                raise ValueError("You have to given the id of a note")

            response = {
                "success": True,
                "message": " Note Data is valid",
                "data": [json_data]
            }
        except Exception as e:
            print(e)
            response = response
        return response



