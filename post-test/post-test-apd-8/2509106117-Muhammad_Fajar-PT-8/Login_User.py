from Data_User import users

def login_user(username, password):
    for id_user, data in users.items():
        if data["username"] == username and data["password"] == password:
            return {"id": id_user, **data}
    return None