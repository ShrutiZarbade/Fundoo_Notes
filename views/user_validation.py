from config.mysql_connection import db_obj
import json


class User:

    def register(self, that=None):

        try:
            response = {
                "success": False,
                "message": "something went wrong",
                "data": []
            }
            content_length = int(that.headers['Content-Length'])
            body = that.rfile.read(content_length)
            print(json.loads(body), '------------------->body')
            json_data = json.loads(body)

            if json_data['username'] is None:
                response['message'] = "username cannot be empty"

            if json_data['email'] is None:
                response['message'] = "Email cannot be empty"

            if len(json_data['password']) > 0 and len(json_data['email']) > 0 and len(json_data['username']) > 0:
                response = {
                    "success": True,
                    "message": 'User data is valid',
                    "data": [json_data]
                }
        except Exception as e:
            print(e)
            response = response

        return response

    def active(self):
        response = {
            "success": True,
            "message": " user activate successfully "
        }
        return response

    def login(self, that=None):

        try:
            response = {
                "success": False,
                "message": "Something went wrong",
                "data": []
            }
            content_length = int(that.headers['Content-Length'])
            body = that.rfile.read(content_length)
            print(json.loads(body), '------------------->body')
            json_data = json.loads(body)
            print(json_data)
            email = json_data['email']
            print(email, '==========> user enter email')

            # import pdb
            # pdb.set_trace()

            if json_data['email'] is None:
                response['message'] = 'email cannot be empty'

            if len(json_data['email']) > 0 and len(json_data['password']) > 0:
                response = {
                    "success": True,
                    "message": "data is valid",
                    "data": [json_data]
                }
                return response
        except Exception as e:
            print(e)
            response = response
        return response

    def logout(self):
        response = {
           "success": True,
           "message": "User log out"
        }
        return response

    def forgot_password(self, that=None):
        try:
            response = {
                "success": False,
                "message": "Something went wrong",
                "data": []
            }

            content_length = int(that.headers['Content-Length'])
            body = that.rfile.read(content_length)
            json_data = json.loads(body)
            print(json_data, '====================>json data')
            email = json_data['email']

            if email is not None:
                response['success'] = True
                response['message'] = 'user email is valid'
                response['data'] = [{
                    'email': email,
                }]
                return response
        except Exception as e:
            response = response
        return response









