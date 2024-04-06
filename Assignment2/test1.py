import os
import re

def register_admin():
        print("welcome to register, your role is: admin")
        # open and read admin.txt
        admin_file = open("Assignment2/user_admin.txt", 'r')
        admin_list = admin_file.read().split()
        admin_file.close()
     
        # create username and password
        def input_username():
            print("Enter your name")
            get_username = input("\nEnter 'quit' to quit")
            if get_username.lower() == "quit":
                quit
            elif get_username in admin_list:
                print("username already exits")
                return input_username()
            else:
                print("valid username")
                return get_username

        def input_password():
            print("enter your password")
            get_password = input("\nenter password")
            check_password = input("\nenter password again")
                # double check password
            if get_password != check_password:
                print("both password should be the same")
                return input_password()
            else:
                return get_password
            
        
        username = input_username()
        password = input_password()
        role = "admin"
        # create admin
        admin = {}
        admin[username] = {"username":username , "password":password, "role":role}
        
        def create_admin(userinfo):
            # read user_admin.txt
            with open("Assignment2/user_admin.txt", 'r') as file:
                file_content = file.read()
            
            file_content += '\n' + userinfo
            # write admin into file
            with open("Assignment2/user_admin.txt","w") as file:
                file.write(file_content)
                
        
        create_admin(str(admin[username]))     
        print("admin created successfully")    
            
register_admin()          
         