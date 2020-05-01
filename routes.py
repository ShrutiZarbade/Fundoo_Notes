"""
This is the file for routes which is used for giving path for all api
Author: Shruti Zarbade
Date: 10/3/2020

"""
from http.server import BaseHTTPRequestHandler
from views.users_view import User
from views.notes_view import Notes
from services.user_service import UserServices
from services.notes_service import NoteServices
from auth.login_required import login_required
from response import Response
from urllib.parse import urlparse


class S(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        """
            this function define all the do get request from the server
        """
        # this is the user register path
        if self.path == '/register':
            with open("./templates/registration.html", "r") as f:
                text = f.read()
                Response(self).html_response(status=200, data=text)

        # this is the login path for users
        if self.path == '/login':
            with open("./templates/login.html", "r") as f:
                text = f.read()
                Response(self).html_response(status=200, data=text)

        # this is the logout path for users
        if self.path == '/logout':
            pass

        # this is the forgot password path for users
        if self.path == '/forgot_password':
            with open("./templates/forgot.html", "r") as f:
                text = f.read()
                Response(self).html_response(status=200, data=text)

        # this is the reset password path for users
        if self.path == '/createnotes':
            pass

        # this the path for sending notes into trashed
        if self.path == '/is_trashed':
            pass

        # this the path for pinned the notes
        if self.path == '/is_pinned':
            pass

        # this is the path for archive the notes
        if self.path == '/is_archived':
            pass

        # this is the path for read all the notes of a user
        if self.path == '/readnotes':
            response = Notes().read_notes(that=self)
            if response['success']:
                user_id = response['data'][0]
                response = NoteServices().read(user_id)
            Response(self).jsonResponse(status=200, data=response)

        # this is the path for showing all the archive notes
        if self.path == '/list_archive':
            response = NoteServices().archive_data()
            print(response, "--------response")
            Response(self).jsonResponse(status=200, data=response)

        # this is the path for showing all the trash notes
        if self.path == '/list_trash':
            response = NoteServices().trash_data()
            print(response, "--------response")
            Response(self).jsonResponse(status=200, data=response)

        # this is the path for showing all the pin notes
        if self.path == '/list_pin':
            response = NoteServices().pin_data()
            print(response, "-----------response")
            Response(self).jsonResponse(status=200, data=response)

    @login_required
    def do_POST(self):
        """
            This is the function for uploading the given contained in the database
            :return: response of each path
        """

        response = {
            "success": False,
            "message": "something went wrong",
            "data": []
        }

        print(self.path.split('/?')[0])
        is_matched = self.path.split('/?')[0]
        if is_matched == '/activate':
            query = urlparse(self.path).query
            query_components = dict(qc.split("=") for qc in query.split("&"))
            print(query_components, "query_components----->", query)

            if query_components['token']:
                self.path = '/activate'

        elif is_matched == '/reset':
            query = urlparse(self.path).query
            query_components = dict(qc.split("=") for qc in query.split("&"))
            print(query_components, "query_components----->", query)

            if query_components['token']:
                self.path = '/reset'

        # user registration routes
        if self.path == '/register':
            response = User().register(that=self)
            if response['success']:
                user_data = response['data'][0]
                response = UserServices().register(user_data, that=self)
        Response(self).jsonResponse(status=200, data=response)

        if self.path == '/activate':
            response = UserServices().activate(token=query_components['token'])
            Response(self).jsonResponse(status=200, data=response)

        # user login routes
        if self.path == '/login':
            response = User().login(that=self)
            if response['success']:
                user_data = response['data'][0]
                response = UserServices().login(user_data=user_data)
            Response(self).jsonResponse(status=200, data=response)

        # user logout route
        if self.path == '/logout':
            response = UserServices().logout(that=self)
        Response(self).jsonResponse(status=200, data=response)

        # for forgot password
        if self.path == '/forgot_password':
            response = User().forgot_password(that=self)
            if response['success']:
                user_data = response['data'][0]
                response = UserServices().forgot_password(user_data, that=self)
            Response(self).jsonResponse(status=200, data=response)

        # for reset the password
        if self.path == '/reset':
            response = User().reset_password(that=self)
            if response['success']:
                user_data = response['data'][0]
                response = UserServices().reset_password(user_data, token=query_components['token'])
            Response(self).jsonResponse(status=200, data=response)

        # Create the notes and insert it into the database table

        if self.path == '/createnotes':
            response = Notes().create_notes(that=self)
            if response['success']:
                note_data = response['data'][0]
                response = NoteServices().create(note_data)
            Response(self).jsonResponse(status=200, data=response)

        # updated profile for user

        if self.path == '/upload':
            response = UserServices().upload_profile(that=self)
        Response(self).jsonResponse(status=200, data=response)

    @login_required
    def do_PUT(self):

        if self.path == '/update_note':
            try:
                response = Notes().update_notes(that=self)
                if response['success']:
                    note_data = response['data'][0]
                    response = NoteServices().update(note_data)
            except Exception as e:
                print(e)
            Response(self).jsonResponse(status=200, data=response)

        # Is Trash, Archive and Pin path

        if self.path == '/is_trashed':
            response = Notes().is_trashed(that=self)
            if response['success']:
                data = response['data'][0]
                response = NoteServices().trashed(data)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/is_pinned':
            response = Notes().is_pinned(that=self)
            if response['success']:
                data = response['data'][0]
                response = NoteServices().pinned(data)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/is_archived':
            response = Notes().is_archived(that=self)
            if response['success']:
                data = response['data'][0]
                response = NoteServices().archived(data)
            Response(self).jsonResponse(status=200, data=response)

    @login_required
    def do_DELETE(self):
        """
            this function is used for deleting the notes from the table

        """

        if self.path == '/delete_note':
            response = Notes().delete_notes(that=self)
            if response['success']:
                note_data = response['data'][0]
                response = NoteServices().delete(note_data)
            Response(self).jsonResponse(status=200, data=response)




