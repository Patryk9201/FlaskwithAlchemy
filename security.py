from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
#safe_str_cmp bezpieczniejszym rozwiazaniem niz porownywanie == equal equal#
        return user


def identity(playload):
    user_id = playload['identity']
    return UserModel.find_by_id(user_id)
