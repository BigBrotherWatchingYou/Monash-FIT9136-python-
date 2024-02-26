user_id_list = []
class User_Management_System(self, user_id_list):
    def __init__(self, username, userid, password, email):
        self.list = {}
        self.list[userid] = {self.username, self.userid, self.password, self.email}
        
    def add_user_to_user_id_list(userid, user_id_list):
        user_id_list.append(userid)
    def add_user(self, username, userid, password, email):
        self.list[userid] = {"username": username, "userid": userid, "userpassword": password, "useremail": email}

    def check_user(userid):
        if userid in user_id_list:
            print(f"user{userid}exists")
            return True
        else:
            print(f"user{userid}does not exists")
            return False
    def update_user(self, userid, new_id = None, new_password = None, new_email = None):
        if userid in user_id_list:
            if new_id:
                self.list[userid]["userid"] = new_id
            if new_password:
                self.list[userid]["password"] = new_password
            if new_email:
                self.list[userid]["email"] = new_email



def run(self):
    choice = input(" 1\ for login \n 2\ for update info \n 3 for register")

