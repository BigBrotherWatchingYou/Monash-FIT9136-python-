import string
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
    def get_input(requirement, user_input):
        '''# requirement type: 
        1.letter only
        2.digits only
        3.email only
        4. complex_password 
        # tips: type and press'Enter' can pass the section
    
        # deal with space input in Feb.23.2024'''
        user_input = str(user_input)
        requirement = str(requirement)
        if user_input == '':
            return False
        
        if requirement == 'letter':
            user_input = input("enter your letter")
            if user_input.isalpha():
                print('valid letter')
                return user_input
            else:
                print("invalid, letters only")
                user_input = input('only be letters from a-z(or A-Z)\ntype again')
                return get_input('letter', user_input)

        # requirement : numbers only        
        if requirement == 'digit':
            user_input = input("type your number")
            if user_input.isdigit():
                return user_input
        else:
            print("invalid, numbers only")
            user_input == input('only numbers form 0-9\ntype again')
            
            return get_input('digit', user_input)

        # requirement of email
        if requirement == 'email':
            user_input = input("enter your email")
            if '@' and '.com' in user_input:
                print('valid email:'+ user_input)
                return user_input
            else:
                print('email should include @ or .com')
                user_input = input('enter email')
            
                return get_input('email', user_input)

        # requirement of 'password = letter(Upper+lower) + digit + @#$@#$  and 16 >=length >= 8'
        if requirement == 'password':
            l = 0
            d = 0
            s = 0
            le = 0
            user_input = input("enter password")
            if len(user_input) >= 16:
                print('too long, should be less than 16')
                user_input = input('input a new password')
                return get_input("password", user_input)
        
            if len(user_input) >= 8 and len(user_input) <= 16:
                le += 1
            for char in user_input:
                    if char.isalpha():
                        l += 1
 
                    if char.isdigit():
                        d += 1

                    if char in r'[^a-zA-Z0-9\s]':
                        s += 1
            
            if l != 0 and d != 0 and s != 0 and le != 0:
                print('valid password')
                return user_input
        else:
            print('too simple password')
            user_input = input('letter(Upper + lower) + digit + @#$@#$  and 16 >=length >= 8')
            return get_input("password", user_input)


def run(self):
    choice = input(" 1\ for login \n 2\ for update info \n 3 for register")

