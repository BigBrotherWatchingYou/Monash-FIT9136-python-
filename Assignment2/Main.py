import re
import os
import random
from User import User

class Main:
    def show_menu():
'''This method prints out the available options that the user can choose. You can add
positional arguments if you need. Fig1 shows an example of the menu output.'''
        print("Welcome to our system")
        
    
    def login    
# Fig1 show menu example
    def process_operations(user_object):
'''This method has one positional argument user_object.
Admin can take commands “1”, “2”, “3”, “4”, “5”. For command “2” and “4”, the end
user needs to enter “TITLE_KEYWORD/ID/INSTRUCTOR_ID” and
“ID/KEYWORD/COURSE_ID” as a second command, followed by a value. For example,
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
Assignment2/Mainmenu.example.png

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
if __name__ == “__main__”:
    Main.main()
    
'''This part is the entry point of the whole program. In code part, 1. output a message
to indicate the program start. 2. Manually register an admin account(call
register_admin() method). 3. Call the main() method. When marking your
assignment, we will run this file only.'''
