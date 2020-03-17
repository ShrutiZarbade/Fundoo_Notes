"""
This is the file for routes which is used for giving path for all api
Author: Shruti Zarbade
Date: 10/3/2020

"""

from http.server import BaseHTTPRequestHandler
from views.user_validation import User
from views.notes_view import Notes
from services.user_service import UserServices
from services.notes_service import NoteServices
from auth.login_required import login_required
from response import Response
from urllib.parse import urlparse
import requests
PORT = 8080


class S(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):

        if self.path == '/register':
            with open("./templates/registration.html", "r") as f:

                text = f.read()
                Response(self).html_response(status=200, data=text)

        if self.path == '/login':
            pass

        if self.path == '/logout':
            pass

        if self.path == '/forgotpassword':
            pass

        if self.path == '/createnotes':
            pass

        if self.path == '/readnotes':
            print('---------------->readnotes')
            response = Notes().read_notes(that=self)
            print(response, '============>readnotes')
            if response['success']:
                user_id = response['data'][0]
                print(user_id, '============>user_data')
                response = NoteServices().read(user_id)
                print(response, "--------response")
            Response(self).jsonResponse(status=200, data=response)

    @login_required
    def do_POST(self):

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

        if self.path == '/register':
            response = User().register(that=self)
            if response['success']:
                user_data = response['data'][0]
                response = UserServices().register(**user_data)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/activate':
            response = UserServices().activate(token=query_components['token'])
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/login':
            print('------->login')
            response = User().login(that=self)
            print(response, '------>login')
            if response['success']:
                user_data = response['data'][0]
                print(user_data, '--->')
                response = UserServices().login(user_data=user_data)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/logout':
            print('--------->logout')
            response = User().logout()
            print(response, type(response), '-------->logout')
            if response['success']:
                # user_data = response['data'][0]
                # print(user_data, '----->')
                response = UserServices().logout(that=self)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/forgotpassword':
            response = User().forgot_password(that=self)
            if response['success']:
                user_data = response['data'][0]
                print(user_data, '--------->>>user_data')
                response = UserServices().forgot_password(user_data)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/createnotes':
            print('------------>createnotes')
            response = Notes().create_notes(that=self)
            print(response, '=============>createnotes')
            # import pdb
            # pdb.set_trace()
            if response['success']:
                note_data = response['data'][0]
                print(note_data, '==========>user data')
                response = NoteServices().create(note_data)
            Response(self).jsonResponse(status=200, data=response)

    def do_PUT(self):

        if self.path == '/update_note':
            try:
                print("================>update note")
                response = Notes().update_notes(that=self)
                print(response, '=============>update_note')
                if response['success']:
                    note_data = response['data'][0]
                    print(note_data, '============>user data')
                    response = NoteServices().update(note_data)
            except Exception as e:
                print(e)
            Response(self).jsonResponse(status=200, data=response)

    def do_DELETE(self):

        if self.path == '/delete_note':
            print("========>delete note")
            response = Notes().delete_notes(that=self)
            print(response, '===========>>>delete notes')
            if response['success']:
                note_data = response['data'][0]
                print(note_data, '==========>>note data')
                response = NoteServices().delete(note_data)
            Response(self).jsonResponse(status=200, data=response)




