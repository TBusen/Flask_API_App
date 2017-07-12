from werkzeug.security import safe_str_cmp
from user import User

users = [ # table of users
    User(1, 'bob', 'asdf')
]

username_mapping = {u.username: u for u in users}

userid_mapping = {u.id: u for u in users}

# authenticate a user

def authentiate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password,  password): # returns bool, safe way to compare strings
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
