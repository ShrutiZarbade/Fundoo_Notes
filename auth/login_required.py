from response import Response
from config.redis_connection import Redis
import jwt
redis_obj = Redis()

response = {
    'message': "something went wrong"
}


def login_required(method):

    def token_verification(self):
        try:
            print(self.path, type(self.path))
            if self.path is ['/createnotes', '/readnotes']:
                token = self.headers['token']
                print(token)
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                user_id = payload['id']
                token = redis_obj.get(user_id)
                if token is None:
                    raise ValueError("You Need To Login First")
                return method(self)
            else:
                return method(self)
        except jwt.DecodeError:
            response['message'] = "decode error"
            Response(self).jsonResponse(status=404, data=response)
    return token_verification