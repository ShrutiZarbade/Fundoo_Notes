"""
This is the file for user services where user related all function are written.
Author: Shruti Zarbade
Date: 10/3/2020

"""
from config.mysql_connection import db_obj
import jwt
# import cgi
from config.redis_connection import Redis
from vendor.sendmail import SmtpSendMail
# send_mail = SmtpSendMail()
# import smtplib
redis_con = Redis()


class UserServices:

    def register(self, **user_data):
        response = {
            "success": False,
            "message": "User not registered",
            "data ": []
        }
        # import pdb
        # pdb.set_trace()
        table_name = "users"
        print(table_name, "==========>table name")

        read_data = db_obj.read(table_name=table_name, column_name=None, column_val=None)
        print(read_data, "===========>read data")

        for data in read_data:
            if data[1] == user_data['username'] or data[3] == user_data['email']:
                response = {
                    "success": True,
                    "message": "User Already Registered"
                }
                break

        if response["success"] == False:
            db_obj.insert(data=user_data, table_name=table_name)
            email = user_data['email']
            print(email, "========>email")
            read_last_data = db_obj.par_data(email)
            print(read_last_data, "=========>read data")
            user_email = read_last_data['email']
            print(user_email, "========>from database")
            user_id = read_last_data['id']

            # generate token for sending token on user mail
            token = jwt.encode({'id': user_id}, 'secret', algorithm='HS256').decode('utf-8')

            message = "Click the link to activate: http://127.0.0.1:8080/activate/?token='" + token + "'"

            # Calling send_mail function to pass the argument token and user mail
            SmtpSendMail().send_mail(user_email, message)

            response = {
                "success": True,
                "message": "User Registered successfully"
            }
        return response

    def activate(self, token=None):

        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        user_id = payload.get('id')
        db_obj.update_data(user_id)

        response = {
            "success": True,
            "message": "You Are Activated!"
        }
        return response

    def login(self, user_data):
        smd = {
            "success": False,
            "message": "User not login",
            "data ": []
        }
        #
        print(user_data, '==========>userdata')
        email = user_data['email']
        print(email, '==============>useremail')
        read_data = db_obj.par_data(email)
        print(read_data, '=========>read data')

        if read_data is not None:
            db_id = read_data[0]
            print(db_id, '============>db_id')
            token = jwt.encode({'id': db_id}, 'secret', algorithm='HS256').decode('utf-8')
            redis_con.set(db_id, token)
            smd = {
                'success': True,
                'message': 'log in successfully',
                'data': [token]
            }
        else:
            smd = {
                'success': True,
                'message': 'User is not Registered'
            }
        return smd

    def logout(self, that=None):

        print(self, "==========>dir")
        smd = {
            "success": False,
            "message": "something went wrong",
            "data": []
        }
        token = that.headers['token']
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        user_id = payload.get('id')
        redis_con.delete(user_id)

        smd = {
            "success": True,
            "message": "User logout successfully",
            "data": []
        }
        return smd

    def forgot_password(self, user_data):
        smd = {
            "success": False,
            "meassage": "something went wrong",
            "data": []
        }
        import pdb
        pdb.set_trace()
        user_email = user_data['email']
        if user_email is not None:
            token = jwt.encode({'id': user_email}, 'secret', algorithm='HS256').decode('utf-8')

            message = "Click the link to reset password http://127.0.0.1:8080/resetpassword/'" + token + "'"

            SmtpSendMail().send_mail(user_email, message)
        smd = {
            "success": True,
            "message": "Successfully mail is send to reset user password ",
            "data": []
        }
        return smd

    def reset_password(self):
        smd = {
            "success": True,
            "message": "something went wrong",
            "data": []
        }
        # message = {
        #     'success': True,
        #     'message': "click the below link ",
        #     'data': [token]
        # }
        # smtp_obj = smtplib.SMTP('localhost')
        # smtp_obj.sendmail(sender, receivers, message)
        # print("successfully send mail")






