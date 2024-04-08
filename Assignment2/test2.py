import re
import os
import random
import string

class Admin:
    def regis():
        print("welcome to register, your role is: admin")
        # open and read admin.txt
        try:
            with open("Assignment2/user_admin.txt") as file:
                admin_list = [k.strip().split(";;;")[1].strip("{}") for k in file if file.strip()]
                # unable to read space lines
            print("admin_list:",admin_list)
        except FileNotFoundError:
            admin_list = []
        
    
        # create username and password
        def input_username():
        
            get_username = input("Enter your name(Enter 'quit' to quit): ")
            if get_username.lower() == "quit":
                quit
            if get_username in admin_list:
                print("username already exits")
                return input_username #prompt user again
            else:
                return get_username

        def input_password():
            get_password = input("enter password: ")
            confirm_password = input("Confirm your password: ")
            # double check password
            if get_password != confirm_password:
                print("Passwords do not match. Please try again.")
                return input_password()
            else:
                return get_password
            
        username = input_username()    
        password = input_password()    
        userid = random.randint(10000, 99999)
        userinfo = f"{userid};;;{username};;;{password}"
            
        with open("Assignment2/user_admin.txt",'a') as f:
            f.write(f"\n{userinfo}")
        print("Admin created successfully.")
            
Admin.regis()            

