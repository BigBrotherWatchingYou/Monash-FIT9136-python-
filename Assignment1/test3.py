def add_user(user_dict, username, password, userid):
    
    user_dict[username] = {"username": username, "password": password, "userid": userid}
    return user_dict[username]
data = {}
add_user(data, "Yname", "awef234", "234234")
