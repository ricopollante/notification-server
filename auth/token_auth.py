import jwt as jwt_init

SECRET_KET = 'superadmin'
algorithm = 'HS256'

def token_encode(username):
    payload_encode = jwt_init.encode({'username' : username}, SECRET_KET, algorithm=algorithm)
    token = payload_encode.decode('UTF')
    return token


def token_verify(token):
        try:
            payload_decode = jwt_init.decode(token, SECRET_KET, algorithm=algorithm)
        except:
            return "Token Invalid"

        return "True"

