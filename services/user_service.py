"""
This is the file for user services where user related all function are written.
Author: Shruti Zarbade
Date: 10/3/2020

"""
from model.db_query import Query
import jwt
import cgi, os
from config.redis_connection import RedisConnection
from vendor.sendmail import SendMail
send_mail_obj = SendMail()
db_object = Query()
redis_con = RedisConnection()


class UserServices:

    def register(self, user_data, that=None):
        response = {
            "success": False,
            "message": "User not registered",
            }
        user_email = user_data['email']
        table_name = "users"

        # checking the email id  is available in table or not
        read_data = db_object.read(table_name=table_name, column_name="email", column_val=user_email)

        if read_data == []:
            db_object.insert(data=user_data, table_name=table_name)
            db_data = db_object.read(table_name=table_name, column_name="email", column_val=user_email)
            db_id, db_email = db_data[0][0], db_data[0][2]

            # generate token for sending token on user mail
            token = jwt.encode({'id': db_id}, 'secret', algorithm='HS256').decode('utf-8')

            host = that.headers['Host']
            protocol = that.protocol_version.split('/')[0].lower()

            message = f"Click the link to activate: {protocol}://{host}/activate/?token={token} "

            # Calling send_mail function to pass the argument token and user mail
            send_mail_obj.send_mail(db_email, message)

            response['success'], response['message'] = True, "User Registered successfully"
        else:
            response['success'] = True
            response['message'] = "User Already registered"

        return response

    def activate(self, token):
        response = {
            "success": True,
            "message": "something went wrong"
            }
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        user_id = payload.get('id')
        data = {
            "id": user_id,
            "is_active": True
        }
        table_name = "users"
        db_object.update(table_name=table_name, data=data)

        response['success'], response['message'] = True, "User Activated successfully"
        return response

    def login(self, user_data):
        response = {
            "success": False,
            "message": "User not login",
            "data ": []
        }
        # unpacking the data from the user data
        user_email = user_data['email']
        user_password = user_data['password']
        table_name = "users"

        # read the data from the database
        read_data = db_object.read(table_name=table_name, column_name=None, column_val=None)

        for data in read_data:
            db_id, username, email, password, is_active = data
            if email == user_email and password == user_password and is_active == 1:
                token = jwt.encode({'id': db_id}, 'secret', algorithm='HS256').decode('utf-8')
                redis_con.set(db_id, token)
                response['success'] = True
                response['message'] = "User Registered successfully"
                response['data'] = token

        return response

    def logout(self, that=None):
        response = {
            "success": False,
            "message": "something went wrong",
            "data": []
        }
        token = that.headers['token']
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        user_id = payload.get('id')
        redis_con.delete(user_id)

        response['success'] = True
        response['message'] = "User logout successfully"
        return response

    def forgot_password(self, user_data, that=None):
        response = {
            "success": False,
            "message": "something went wrong",
            "data": []
        }
        user_email = user_data['email']

        read_data = db_object.read(table_name="users", column_name="email", column_val=user_email)

        if read_data == []:
            response['message'] = "This user is not registered"

        else:
            db_id = read_data[0][0]
            token = jwt.encode({'id': db_id}, 'secret', algorithm='HS256').decode('utf-8')

            host = that.headers['Host']
            protocol = that.protocol_version.split('/')[0].lower()

            # import pdb
            # pdb.set_trace()

            message = f"Click the link to reset password {protocol}://{host}/reset/?token={token}"

            send_mail_obj.send_mail(user_email, message)
            response['success'] = True
            response['message'] = "Successfully mail is send to reset user password "

            return response

    def reset_password(self, user_data, token):
        response = {
            "success": True,
            "message": "something went wrong",
            "data": []
        }
        user_password = user_data['password']
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        user_id = payload.get('id')
        data = {
            "id": user_id,
            "password": user_password
        }
        table_name = "users"
        db_object.update(table_name=table_name, data=data)

        response['success']=True,
        response['message'] = "Your password is reset"
        return response

    def upload_profile(self, that=None):
        try:
            response = {
                "success": False,
                "message": "Something went wrong",
                "data": []
            }
            ctype, pdict = cgi.parse_header(that.headers['content-type'])
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")

            if ctype == 'multipart/form-data':
                form = cgi.FieldStorage(fp=that.rfile, headers=that.headers, environ={'REQUEST_METHOD': 'POST',
                                        'CONTENT_TYPE': that.headers['Content-Type'], })
                filename = form['upfile'].filename
                data = form['upfile'].file.read()
                open("./media/%s" % filename, "wb").write(data)

                path = f"./media/{filename}"

                token = that.headers['token']
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                user_id = payload.get('id')

                data = {
                    "path": path,
                    "user_id": user_id
                }

                db_object.insert(data=data, table_name="profile")

                response['success'] = True
                response['message'] = "Successfully upload profile pic"

        except Exception as e:
            print(e)
        return response







