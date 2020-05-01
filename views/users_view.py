"""
 This file validate the data given by user and passed it to future services
 Author: Shruti Zarbade"
 Date: 9/3/2020
"""


import cgi
from utils import validate_email


class User:

    # this function validate the data for registration process
    def register(self, that=None):
        try:
            response = {
                        "success": False,
                        "message": "something went wrong",
                    }
            form = cgi.FieldStorage(fp=that.rfile,  headers=that.headers, environ={'REQUEST_METHOD': 'POST',
                                    'CONTENT_TYPE': that.headers['Content-Type'],})
            form_keys = list(form.keys())
            username = form['username'].value
            email = form['email'].value
            password = form['password'].value

            if len(username) == 0:
                response['message'] = "username cannot be empty"
                raise ValueError

            if not validate_email(email):
                response['message'] = "Email is not a valid"
                return response

            if len(password) == 0:
                response['message'] = "password not be empty"
                raise ValueError

            data ={}
            data['username'], data['email'], data['password'] = username, email, password

            # updating response
            response['success'], response['message'], response['data'] = True, "data is valid", [data]

        except ValueError:
            response = response

        except Exception as e:
            response = response
        return response

    # this data validate the data for login
    def login(self, that=None):
        try:
            response = {
                "success": False,
                "message": "something went wrong"
            }

            form = cgi.FieldStorage(fp=that.rfile,  headers=that.headers, environ={'REQUEST_METHOD': 'POST',
                                    'CONTENT_TYPE': that.headers['Content-Type'],})
            form_keys = list(form.keys())
            email = form['email'].value
            password = form['password'].value

            if not validate_email(email):
                response['message'] = "Email is not a valid"
                return response

            if len(password) == 0:
                response['message'] = "password not be empty"
                raise ValueError

            data = {}
            data['email'], data['password'] = email, password

            response['success'] = True
            response['message'] = "Data is valid"
            response['data'] = [data]

        except ValueError:
            response = response

        except Exception as e:
            print(e)
            response = response
        return response

    # data validation for forgot password
    def forgot_password(self, that=None):
        try:
            response = {
                "success": False,
                "message": "Something went wrong",
                "data": []
            }
            form = cgi.FieldStorage(fp=that.rfile, headers=that.headers, environ={'REQUEST_METHOD': 'POST',
                                    'CONTENT_TYPE': that.headers['Content-Type'], })

            form_keys = list(form.keys())
            email = form['email'].value

            if not validate_email(email):
                response['message'] = "Email is not a valid"
                return response

            data = {}
            data['email'] = email

            response['success'] = True
            response['message'] = "data is valid"
            response['data'] = [data]

        except Exception as e:
            response = response
        return response

    # data validation for reset password
    def reset_password(self, that=None):
        try:
            response = {
                "success": False,
                "message": "something went wrong"
            }

            form = cgi.FieldStorage(fp=that.rfile, headers=that.headers, environ={'REQUEST_METHOD': 'POST',
                                    'CONTENT_TYPE': that.headers['Content-Type'], })
            form_keys = list(form.keys())

            password = form['password'].value

            if password == 0:
                response['message'] = "password not be empty"
                raise ValueError

            data ={}
            data['password'] = password

            response['success'] = True
            response['message'] = "data is valid"
            response['data'] = [data]

        except ValueError:
            response = response

        except Exception as e:
            response = response
        return response












