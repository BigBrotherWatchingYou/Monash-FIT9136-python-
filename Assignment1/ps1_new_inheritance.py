import random
'''what is unchangeable: userid'''

class UserDataManager:
    user_id_list = []
    user_data = {}
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
        
            '''if not any(char in r'[^a-zA-z0-9\s]' for char in user_input):
                print("password should include at least one special character.")
                return False'''
        
            print("Valid Password\n-----------------")
            return user_input


    def add_user_to_user_id_list(userid,username, password, email):
        # add the userid to the list
        UserDataManager.user_id_list.append(userid)
        
        # create user
        user_info = {"userid": userid,
                     "username": username,
                     "password": password,
                     "email": email}
        UserDataManager.user_data[userid] = user_info
        print("User created successfully, your id:", userid, "\n ----------Welcome -----------------------")
        
       # turn to user_page
        UserDataManager.user_page(userid)

    def check_user(userid):
        # check does the user exists
        if userid in UserDataManager.user_id_list:
            print(f"user{userid}exists.")
            return True
        else:
            print(f"user{userid}does not exist.")
            return False
        
    def generate_user_id(digitsnumber):
        # create a userid
        generated_id = ''.join(str(random.randint(0,9)) for i in range(digitsnumber))
        return generated_id
    
    def authenticate_user(userid, password):
        # check password and userid 
        if UserDataManager.user_data[userid]["password"] == password:
            return True
        else:
            print("Incorrect password")
            return False

    def user_page(userid):
        # the page after login successfully
        print("--------------\n User Page\n whatdo you want to do?")
        for key, value in ((UserDataManager.user_data[userid]).items()):
            print (key,":", value)
        print("1/ change name  \n 2/change password \n 3/change email")
        t = input(" \n (Enter q to quit )")
        if t == "1":
            m = input("Enter your new user_name")
            UserDataManager.update_user(userid, new_username= m)
            return UserDataManager.user_page(userid)
            
        if t == "2":
            m = input("Enter your new password")
            UserDataManager.update_user(userid, new_password= m)
            return UserDataManager.user_page(userid)

        if t == "3":
            m = input("Enter your new email")
            if not UserDataManager.check_req("email",m):
                return
            UserDataManager.update_user(userid, new_email= m)
            return UserDataManager.user_page(userid, t="3")
        
        if t == "q":
            return UserDataManager.run()
        else:
            print("Invalid input(user_page)")


    def login():
        print("Login Page\n--------------------------\nplease Enter your user userID\n(Enter 'q' to quit")
        userid = input("type here")
        # 1. check user exists
        if userid == "q":
            return UserDataManager.run() 
        
        if not UserDataManager.check_user(userid):
            print("User did not exist")
            return UserDataManager.login()
        # 2. check password
        print("please Enter your Password")
        password = input("type here")
        if not UserDataManager.authenticate_user(userid, password):
            print("------------Login Failed")
            return UserDataManager.run()
        
        else:
            print("login successfully")
            return UserDataManager.user_page(userid)
        

    def update_user(userid, new_username = None, new_id = None, new_password = None, new_email = None):
        # for user update their information
        if userid in UserDataManager.user_id_list:
            if new_id:
                UserDataManager.user_data[userid]["userid"]= new_id
                print("-------------\n userid updated successful ------------------\n")
            if new_username:
                UserDataManager.user_data[userid]["username"]= new_username
                print("-------------\n user_name updated successful ------------------\n")
            if new_password:
                UserDataManager.user_data[userid]["password"] = new_password
                print("-------------\n password updated successful -------------------\n")
            if new_email:
                UserDataManager.user_data[userid]["email"] = new_email
                print("-------------\n email updated successful -----------------\n")

    def register():
        print("Enter your name")
        username = input("type here (Enter q to quit )")
        if username == "q":
            return UserDataManager.run()
        # username could be  anything
        
            
        # check password format
        def input_password():
            print("enter your password")
            password = input("type here(Enter q to quit registration)")
            if password == "q":
                return UserDataManager.run()
            # check password requirements
            if UserDataManager.check_req("password", password):
                return password
            else:
                return input_password()
        
        
        userid = UserDataManager.generate_user_id(5)
        UserDataManager.add_user_to_user_id_list(userid,username,input_password() , email="No email")
 
    def run():
        # Main programm
        print("----------------------")
        print(" 1\ for login  \n 2\ for register \n 3\ for I forgot my password or account")
        choice = input("type here")
        if choice == "1":
            # login
            UserDataManager.user_page(UserDataManager.login())
                
            

        if choice == "2":
        #register
            UserDataManager.register()
        elif choice == '3':
            print("Feature not implemented yet.")
        else:
            print("Invalid choice. Please try again.")
            
            
if __name__ == "__main__":
    UserDataManager.run()
    

