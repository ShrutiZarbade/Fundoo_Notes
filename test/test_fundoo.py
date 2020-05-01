import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()


class TestRegistration:

    def test_registration_email_not_given(self):
        url = os.getenv("base_url") + '/register'
        data = {'username': 'rutuja', 'password': 'rutuja', 'email': 'shrutizarbade@gmail.com'}
        headers = {'content_type': "form"}
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        assert res.status_code == 200

#     def test_registration_password_not_given(self):
#         url = os.getenv("base_url") + '/register'
#         data = {'username': 'rutuja', 'email': 'rutujatikhile@gmail.com'}
#         headers = {'content_type': "application/json"}
#         res = requests.post(url=url, data=json.dumps(data), headers=headers)
#         print(res.text)
#         assert res.status_code == 200
#
#     def test_registration_username_not_given(self):
#         url = os.getenv("base_url") + '/register'
#         data = {'password': 'rutuja', 'email': 'rutujatikhile@gmail.com'}
#         headers = {'content_type': "application/json"}
#         res = requests.post(url=url, data=json.dumps(data), headers=headers)
#         print(res.text)
#         assert res.status_code == 200
#
#     def test_registration_successful(self):
#         url = os.getenv("base_url") + '/register'
#         data = {'username': 'rutuja', 'password': 'rutuja', 'email': 'rutujatikhile@gmail.com'}
#         headers = {'content_type': "application/json"}
#         res = requests.post(url=url, data=json.dumps(data), headers=headers)
#         print(res.text)
#         assert res.status_code == 200
#
# class TestLogin:
#
#     def test_login_username_not_given(self):
#         url = os.getenv("base_url") + '/login'
#         data = {'email': 'rutujatikhile@gmail.com'}
#         headers = {'content_type': "application/json"}
#         res = requests.post(url=url, data=json.dumps(data), headers=headers)
#         print(res.text)
#         assert res.status_code == 200
#
#     def test_login_email_not_given(self):
#         url = os.getenv("base_url") + '/login'
#         data = {'username': 'rutuja'}
#         headers = {'content_type': "application/json"}
#         res = requests.post(url=url, data=json.dumps(data), headers=headers)
#         print(res.text)
#         assert res.status_code == 200
#
#     def test_login_wrong_username_given(self):
#         url = os.getenv("base_url") + '/login'
#         data = {'username': 'rutuja123', 'email': 'rutujatikhile@gmail.com'}
#         headers = {'content_type': "application/json"}
#         res = requests.post(url=url, data=json.dumps(data), headers=headers)
#         print(res.text)
#         assert res.status_code == 200
#
#     def test_login_wrong_email_given(self):
#         url = os.getenv("base_url") + '/login'
#         data = {'username': 'rutuja', 'email': 'rutujatikhile.com'}
#         headers = {'content_type': "application/json"}
#         res = requests.post(url=url, data=json.dumps(data), headers=headers)
#         print(res.text)
#         assert res.status_code == 200
#
#     def test_login_successful(self):
#         url = os.getenv("base_url") + '/login'
#         data = {'username': 'rutuja', 'email': 'rutujatikhile@gmail.com'}
#         headers = {'content_type': "application/json"}
#         res = requests.post(url=url, data=json.dumps(data), headers=headers)
#         print(res.text)
#         assert res.status_code == 200
#
# class TestForgot:
#
#     def test_forgot_email_not_given(self):
#         url = os.getenv("base_url") + '/forgot'
#         data = {}
#         headers = {'content_type': "application/json"}
#         res = requests.post(url=url, data=json.dumps(data), headers=headers)
#         print(res.text)
#         assert res.status_code == 200
#
#     def test_forgot_wrong_email_given(self):
#         url = os.getenv("base_url") + '/forgot'
#         data = {'email': 'rutujatikhile.com'}
#         headers = {'content_type': "application/json"}
#         res = requests.post(url=url, data=json.dumps(data), headers=headers)
#         print(res.text)
#         assert res.status_code == 200
#
#     def test_forgot_successful(self):
#         url = os.getenv("base_url") + '/forgot'
#         data = {'email': 'rutujatikhile@gmail.com'}
#         headers = {'content_type': "application/json"}
#         res = requests.post(url=url, data=json.dumps(data), headers=headers)
#         print(res.text)
#         assert res.status_code == 200

# class TestReset:
#
#     def test_reset_password_not_given(self):
#         url = os.getenv("base_url") + '/reset'
#         data = {}
#         headers = {'content_type': "application/json"}
#         res = requests.post(url=url, data=json.dumps(data), headers=headers)
#         print(res.text)
#         assert res.status_code == 200
#
#     def test_reset_successful(self):
#         url = os.getenv("base_url") + '/reset'
#         data = {'password': 'rutuja123'}
#         headers = {'content_type': "application/json"}
#         res = requests.post(url=url, data=json.dumps(data), headers=headers)
#         print(res.text)
#         assert res.status_code == 200

# class TestCreateNote:
#
#     def test_create_note_empty_title(self):
#         url = os.getenv("base_url") + '/create_note'
#         data = {'title': '', 'description': 'making new notes', 'color': 'red'}
#         headers = {'content_type': "application/json"}
#         res = requests.post(url=url, data=json.dumps(data), headers=headers)
#         print(res.text)
#         assert res.status_code == 200
#
#     def test_create_note_empty_description(self):
#         url = os.getenv("base_url") + '/create_note'
#         data = {'title': 'eighth note', 'description': '', 'color': 'red'}
#         headers = {'content_type': "application/json"}
#         res = requests.post(url=url, data=json.dumps(data), headers=headers)
#         print(res.text)
#         assert res.status_code == 200
#
#     def test_create_note_empty_color(self):
#         url = os.getenv("base_url") + '/create_note'
#         data = {'title': 'eighth note', 'description': 'making new notes', 'color': ''}
#         headers = {'content_type': "application/json"}
#         res = requests.post(url=url, data=json.dumps(data), headers=headers)
#         print(res.text)
#         assert res.status_code == 200
#
#     def test_create_note_title_not_given(self):
#         url = os.getenv("base_url") + '/create_note'
#         data = {'description': 'making new notes', 'color': 'red'}
#         headers = {'content_type': "application/json"}
#         res = requests.post(url=url, data=json.dumps(data), headers=headers)
#         print(res.text)
#         assert res.status_code == 200
#
#     def test_create_note_description_not_given(self):
#         url = os.getenv("base_url") + '/create_note'
#         data = {'title': 'eighth note', 'color': 'red'}
#         headers = {'content_type': "application/json"}
#         res = requests.post(url=url, data=json.dumps(data), headers=headers)
#         print(res.text)
#         assert res.status_code == 200
#
#     def test_create_note_color_not_given(self):
#         url = os.getenv("base_url") + '/create_note'
#         data = {'title': 'eighth note', 'description': 'making new notes'}
#         headers = {'content_type': "application/json"}
#         res = requests.post(url=url, data=json.dumps(data), headers=headers)
#         print(res.text)
#         assert res.status_code == 200
#
#     def test_create_note_successful(self):
#         url = os.getenv("base_url") + '/create_note'
#         data = {'title': 'eighth note', 'description': 'making new notes', 'color': 'red'}
#         headers = {'content_type': "application/json"}
#         res = requests.post(url=url, data=json.dumps(data), headers=headers)
#         print(res.text)
#         assert res.status_code == 200
#
# class TestReadNote:
#
#     def test_read_note_successful(self):
#         url = os.getenv("base_url") + '/read_note'
#         # data = {'title': 'eighth note', 'description': 'making new notes', 'color': 'red'}
#         headers = {'content_type': "application/json"}
#         res = requests.get(url=url, headers=headers)
#         print(res.text)
#         assert res.status_code == 200
#
# class TestDeleteNote:
#
#     def test_delete_note_successful(self):
#         url = os.getenv("base_url") + '/read_note'
#         data = {'id': 2}
#         headers = {'content_type': "application/json"}
#         res = requests.get(url=url, data=json.dumps(data), headers=headers)
#         print(res.text)
#         assert res.status_code == 200
