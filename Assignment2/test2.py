import os
    
def register():    
    print("welcome to register, your role is: admin")
    # open and read admin.txt
    admin_file = open("Assignment2/user_admin.txt", 'r')
    admin_list = admin_file.read().split()
    admin_file.close()
     
    # create username and password
    def input_username():
        print("Enter your name")
        get_username = input("Enter 'quit' to quit")
        if get_username == "quit":
            quit
        elif get_username in admin_list:
            print("username already exits")
            return input_username()
        else:
            print("valid username")
            return get_username
                        
    def input_password():
        print("enter your password")
        get_password = input("enter password")
        check_password = input("enter password again")
            # double check password
        if get_password != check_password:
            print("both password should be the same")
            return input_password()
        else:
            return get_password
        
    username = input_username()
    password = input_password()
    print("user create successfully")    
    print("username: ", username)
    print("password: ", password)   
    
    
register()        