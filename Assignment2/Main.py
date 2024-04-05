import re
import os
import random
from User import User
from Admin import Admin
from Course import Course
from Review import Review
from Student import Student
from Instructor import Instructor
# from User import User
print("122")
admin_list = ["admin","admin2","admin3"]
student_list = ["student", "student2", "student3" , "student4"]
instructor_list = ["instructor", "instructor2", "instructor3" , "instructor4", "instructor5"]
userdata = {}
userdata["admin"] = {"username":"admin", "password":"admin","role": "admin"}
class Main:
    def show_menu(username):
        # return the command on Menu
        '''This method prints out the available options that the user can choose. You can add
        positional arguments if you need. Fig1 shows an example of the menu output.'''
        # the page after login successful, shows what user can do 
        if userdata[username]["role"] == "admin":
            #Admin login
            print(f"Welcome ",[username],". Your role is ", userdata[username]["role"] )
            print("Please enter Admin command for further service:\n\
            1.EXTRACT_DATA\n\
            2.VIEW_COURSES\n\
            3.VIEW_USERS\n\
            4.VIEW_REVIEWS\n\
            5.REMOVE_DATA")
            # let user take commands
            return take_commands()
            
        def take_commands():
            # get command from user
            user_object = input("take commands (enter 'Logout' to quit)")
            command = ["1","2","3","4","5"]
            if command == "Logout":
                return Main.main
            if user_object not in command:
                print("invalid command")
                return Main.show_menu()
            else:
                return user_object
            
         
            
            
        if userdata[username]["role"] == "User":
            # user login
            pass
        
        return user_role    
    
    
                
                
            
    def process_operations(user_object,user_role,username):
        

        if user_role == "admin":
            if user_object == "1":
                # 1.EXTRACT DATA
                pass
            if user_object == "2":
                #2.VIEW COURSES
                print("The total number of courses is: "+ len(course))
            if user_object == "3":
                # 3.VIEW USERS
                Admin.view_users()
                

            if user_object == "4":
                #4.VIEW REVIEWS
                pass
            if user_object == "5":                
                #5.REMOVE DATA
                pass
            
        if user_role != "admin":
            if user_object in ["1","3","5"]:
                # invalid operation
                print("This option is for admin only")
                
            
            if user_object == "2":
                pass
                
            if user_object == "4":
                pass

        return Main.show_menu(username)
      
    '''This method has one positional argument user_object.
Admin can take commands “1”, “2”, “3”, “4”, “5”. For command “2” and “4”, the end
user needs to enter “TITLE_KEYWORD/ID/INSTRUCTOR_ID” and
“ID/KEYWORD/COURSE_ID” as a second command, followed by a value. 
For example,
if the login user is admin, he can input “2 TITLE_KEYWORD web”(the value after the
second command can only be one word). The system will call corresponding view
course methods and print out all the courses whose title contains “web” (case
insensitive). If the user does not enter any other arguments for command “2” and
“4”, a default overview output will be displayed.
Instructor and Student can take command “2”, “4” and no other arguments are
allowed. If the logged user is instructor or student and the command is “1”, “3”, “5”,
the inherited methods in User class will be executed.
When a user input “logout”, logout the user but the system keeps running.
In this method, it is not allowed to create an object of Admin/Instructor/Student
class. It is assumed that a User class object user_object is passed into this method
and you are not sure about the exact type.'''
#  Menu looks like: 
# Assignment2/Mainmenu.example.png

# !!!   the programm should be like Assignment_2_Specification (1).pdf. page 17-20
        
    def main():
        '''This method handles the main logic of your system. No positional arguments here. It
should keep running until the user input “exit”. At the beginning, this method asks
the user to enter username and password in format “username password”. Next,

create a temp_user object and only assign the username and password to this object.
Then you can use temp_user to call the login() method. Based on the login result, a
corresponding user object can be created (Admin(), Instructor() or Student()). For
different user objects, call the same process_operations(user_object) method to
process all the logics. If the logged user is “Admin”, 1) create an Admin object, 2) call
show_menu() method, 3) call process_operations() method. If the login fails, print
out an error message. If the username password format is incorrect, print out a
different error message.'''
        # let the user enter username and password
        print("Welcome to our system\nPlease input username and password to login:")
        username = User.login()
        # let the user take commands
        userrole = userdata[username]["role"]   
        Main.process_operations(Main.show_menu(username), userrole, username)
        
        '''username = input
        choice = input("enter 1 or 2 or 3")
        if choice == "1":
            # login
            if Main.login() == "admin":
                Admin.constructor()
            if Main.login() == "User":
                User.constructor()

        if choice == "2":
        #register
            Main.register()
        if choice == '3':
            print("Feature not implemented yet.")'''
        
        
        
if __name__ == “__main__”:
    Main.main()
    
'''This part is the entry point of the whole program. In code part, 1. output a message
to indicate the program start. 2. Manually register an admin account(call
register_admin() method). 3. Call the main() method. When marking your
assignment, we will run this file only.'''








