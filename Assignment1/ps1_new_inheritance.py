import random
'''what is unchangeable: userid'''

class UserDataManager(object):
    user_id_list = []
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
                return False

        # requirement : numbers only        
        if requirement == 'digit':
            if user_input.isdigit():
                return user_input
        else:
            print("invalid input, numbers only")
            return False

        # requirement of email
        if requirement == 'email':
            
            if '@' and '.com' in user_input:
                print('valid email:'+ user_input)
                return user_input
            else:
                print("Email should include @ and .com")
                return False


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


    def __init__(userid, username, password, email):
        userid.list = {}
        userid.username = username
        userid.password = password
        userid.email = email
        userid.list[userid] = { "userid":userid,
                               "username": username, 
                               "password":password, 
                               "email":email}
        UserDataManager.add_user_to_user_id_list
        print("user create successfully")
        return userid.list[userid]
        
    def add_user_to_user_id_list(userid):
        UserDataManager.user_id_list.append(userid)
        print("created successfully: userid:"+ userid)

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

    def user_page(userid):
        print("--------------\n here's your info\n whatdo you want to update?")
        print(UserDataManager.userid.list[userid])
        t = input(f"1/ change your name \n 2/change password 3/change email")
        if t == 1:
            m = input("Enter your new user_name")
            UserDataManager.update_user(userid, new_username= m)
            
        if t == 2:
            m = input("Enter your new password")
            UserDataManager.update_user(userid, new_password= m)

        if t == 3:
            m = input("Enter your new email")
            UserDataManager.update_user(userid, new_email= m)

        return userid.list[userid]


    def login():
        userid = input("Enter your user ID")
        # 1. check user exists 
        if not UserDataManager.check_user(userid):
            print("User did not exist")
            return False
        # 2. check password
        password = input("Enter your Password")
        if UserDataManager.authenticate_user(userid, password):
            print("------------Login Successful")
            return True
        else:
            print("-------------\Login failed, Incorrect password")
            return False
        

    def update_user(userid, new_username = None, new_id = None, new_password = None, new_email = None):
        if userid in UserDataManager.user_id_list:
            if new_id:
                userid.list[userid]["userid"]= new_id
                print("-------------\n userid updated successful")
            if new_username:
                userid.list[userid]["username"]= new_username
                print("-------------\n user_name updated successful")
            if new_password:
                userid.list[userid]["password"] = new_password
                print("-------------\n password updated successful")
            if new_email:
                userid.list[userid]["email"] = new_email
                print("-------------\n email updated successful")

    def register():


    def run(self):

        choice = input(" 1\ for login  \n 2 for register \n 3 for I forgot my password or account")
        if choice == "1":
            # login
            if UserDataManager.login():
                # User Page
                UserDataManager.user_page(userid)
            

        if choice == "2":
        #register
            username = input("type your name")
            if not UserDataManager.check_req("letter", username):
                
                password = input("type your password")
            
                if UserDataManager.check_req("password", password) == True:
                    userid = UserDataManager.generate_user_id(5)
                    UserDataManager.__init__(username, userid, password, email=None)
                    print("-------------\nrole create successfully")
                    
            

    

