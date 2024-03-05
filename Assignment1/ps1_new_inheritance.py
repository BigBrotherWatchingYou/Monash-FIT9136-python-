import random
class UserDataManager(object):
    user_id_list = {}
    # for 1.encrypt\decrypt and 2.check input requirements
    
    def xor_encrypt_decrypt(input0):
        # Initialize an empty string to store the result
        result = ""
        key = "k"
        # Iterate over each character in the message
        for char in input0:
            # Perform XOR operation between the character and the key character
            # Use modulo operator to cycle through the key if it's shorter than the message
            result += chr(ord(char) ^ ord(key))
        return(result) 
    
    def check_req(requirement, user_input):
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
            if user_input.isalpha():
                print('valid letter')
                return user_input
            else:
                print("invalid input, letters only")
                user_input = input('Please enter letters only from a-z(or A-Z):')
                return UserDataManager.check_req('letter', user_input)

        # requirement : numbers only        
        if requirement == 'digit':
            if user_input.isdigit():
                return user_input
        else:
            print("invalid input, numbers only")
            user_input == input('Please enter numbers only from 0-9: ')
            return UserDataManager.check_req('digit', user_input)

        # requirement of email
        if requirement == 'email':
            
            if '@' and '.com' in user_input:
                print('valid email:'+ user_input)
                return user_input
            else:
                print("Email should include @ and .com")
                user_input = input('Please enter a valid email: ')
            
                return UserDataManager.check_req('email', user_input)

        # requirement of 'password = letter(Upper+lower) + digit + @#$@#$  and 16 >=length >= 8'
        if requirement == 'password':
            if len(user_input) < 8 or len(user_input) > 16:
                print("Password should be between 8 and 16 characters long")
            return False

        if not any(char.islower() for char in user_input):
            print("password should include at leat one lower class letter")
            return False
        
        if not any(char.isupper() for char in user_input):
            print(" password should include at least one upper class letter")
            return False

        if not any(char.isdigit() for char in user_input):
            print("password should include at least a number")
            return False
        
        if not any(char in r'[^a-zA-z0-9\s]' for char in user_input):
            print("password should include at least one special character.")
            return False
        
        print("Valid Password\n-----------------")
        return user_input


    def __init__(object, username, userid, password, email):
        object.list = {}
        object.username = username
        object.userid = userid
        object.password = password
        object.email = email
        object.list[userid] = {object.username, object.userid, object.password, object.email}
        UserDataManager.add_user_to_user_id_list
        return object.list, object.username ,object.userid,object.password,object.email,object.list[userid]
        
    def add_user_to_user_id_list(userid):
        UserDataManager.user_id_list.append(userid)

    def check_user(userid):
        if userid in UserDataManager.user_id_list:
            print(f"user{userid}exists.")
            return True
        else:
            print(f"user{userid}does not exist.")
            return False
        
    def generate_user_id(digitsnumber):
        generated_name = ''.join(str(random.randint(0,9)) for i in range(digitsnumber))
        print('your user name:' + generated_name)
        return generated_name
    
    def authenticate_user(userid, password):
        if UserDataManager.user_id_list[userid]["password"] == password:
            return True
        else:
            print("Incorrect password")
            return False
            
    def update_user(object, userid, new_id = None, new_password = None, new_email = None):
        if userid in UserDataManager.user_id_list:
            if new_id:
                object.list.userid= new_id
            if new_password:
                object.list[userid]["password"] = new_password
            if new_email:
                object.list[userid]["email"] = new_email

    
    
    
    def run(self):
        
        choice = input(" 1\ for login \n 2\ for update info \n 3 for register")
        if choice == "1":
            # login
            userid = input("input your id")
        if self.check_user(userid) == True:
            password = input("type your password")
            if self.authenticate_user(userid, password) == True:
                print(f"----------------------\nloginsuccess, here are your info:")
                print(user_id_list[userid])
            else:
                password = ("type your passwor again")
                return self.authenticate_user(userid, password)

        if choice == "2":
        # update infos
            userid = input("type your id")
            if self.check_user(userid) == True:
                password = input("type your password")
            if self.authenticate_user(userid, password) == True:
                print("--------------\n here's your info\n whatdo you want to update?" + UserDataManager.user_id_list[userid])
                t = input("1/for username \n 2/for password 3/for email")
                if t == 1:
                    m = input("type your new username")
                    self.update_user(self, userid, newid= m)

                if t == 2:
                    m = input("type your new password")
                    self.update_user(self, userid, new_password= m)

                    if t == 3:
                        m = input("type your new email")
                        self.update_user(self, userid, new_email= m)
            else:
                # userid not exist

        if choice == "3":
        #register
            username = input("type your name")
            if UserDataManager.check_req("letter", username) == True:
                password = input("type your password")
                if UserDataManager.check_req("password", password) == True:
                    userid = UserDataManager.generate_user_id(5)
                    UserDataManager.__init__(object, username, userid, password, email=None)
                    print("-------------\nrole create successfully")
                    
            

    

