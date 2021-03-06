from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    print("user: {}".format(user))
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    print("user_id: {}".format(user_id))
    return UserModel.find_by_id(user_id)


