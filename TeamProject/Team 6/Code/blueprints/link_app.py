from werkzeug.security import check_password_hash, generate_password_hash

import blueprints.new_data as nd


def link_login(user, pwd):
    from app import db
    result = db['user'].find_one({'name': user})
    if result is None:
        return "User not exists"
    else:
        password = result['password']
        if check_password_hash(password, pwd) is False:
            return "Password wrong"
        else:
            return True

def link_register(user, pwd):
    from app import db
    result = db['user'].find_one({'name': user})
    if result is not None:
        return "User exists"
    else:
        hash_pwd = generate_password_hash(pwd)
        nd.new_user(user, hash_pwd)
        return True

def link_edit(user, old_pwd, new_pwd):
    from app import db
    result = db['user'].find_one({'name': user})
    if result is None:
        return "User not exists"
    else:
        password = result['password']
        if check_password_hash(password, old_pwd) is False:
            return "Old password wrong"
        else:
            hash_pwd = generate_password_hash(new_pwd)
            user_id = result['_id']
            db['user'].update_one({"_id": user_id}, {"$set": {"password": hash_pwd}})
        return True
