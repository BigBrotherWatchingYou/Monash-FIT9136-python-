import re
import os
import random
# from User import User
admin_list = ["admin","admin2","admin3"]
student_list = ["student", "student2", "student3" , "student4"]
instructor_list = ["instructor", "instructor2", "instructor3" , "instructor4", "instructor5"]
userdata = {}
userdata["admin"] = {"username":"admin", "password":"admin","role": "admin"}
class Main:
    def show_menu(user_role):
        # return the command on Menu
        '''This method prints out the available options that the user can choose. You can add
        positional arguments if you need. Fig1 shows an example of the menu output.'''
        # the page after login successful, shows what user can do 
        if user_role == "Admin":
            #Admin login
            print("Please enter Admin command for further service:\n\
            1.EXTRACT_DATA\n\
            2.VIEW_COURSES\n\
            3.VIEW_USERS\n\
            4.VIEW_REVIEWS\n\
            5.REMOVE_DATA")
            # let user take commands
            return take_commamds()
            
        def take_commamds():
            # get command from user
            user_object = input("take commands (enter 'Logout' to quit)")
            command = ["1","2","3","4","5"]
            if command == "Logout":
                return Main.main
            if user_object not in command:
                print("invalid command")
                return Main.show_menu(user_role)
            else:
                return user_object
            
         
            
            
        if user_role == "User":
            # user login
            pass
        
        return user_role    
    
    def login():    
        # Fig1 show menu example
        # return "Admin login" or "User login"
        
        # let user input
        userinput = input("format: username password(enter 'exit' to quit)")
        
        #quit
        if userinput == "exit":
            print("Thanks for using, programm quit")
            quit
            
        # incorrect input
        if len(userinput).split() != 2:
            print("format(there should be a space between name and password): username password")
            return Main.login()
        else:
            # legal input
            username = userinput.split()[0]
            password = userinput.split()[1]
            
        # start authenticating username and password    
        authenticate_user(username, password)    
        def authenticate_user(username, password):
            #check do the user exist
            if username not in admin_list:
                #user do not exist
                print("user id do not exist")
                return Main.login()
            if userdata[username]["password"] == password:
                # login successful
                if userdata[username]["role"] == "admin":
                    #Admin login
                    return "Admin"
                else:
                    # normal user login
                    return "User"
            else:
                # login failed
                print("incorrect username and password\n\
                    input format:username password")
                return Main.login()
                
                
            
    def process_operations(user_object,user_role):
        

        if user_role == "Admin":
            if user_object == "1":
                # 1.EXTRACT DATA
                pass
            if user_object == "2":
                #2.VIEW COURSES
                pass
            if user_object == "3":
                # 3.VIEW USERS
                print("total number of admin: " + len(admin_list))
                print("total number of instructor: " + len(instructor_list))
                print("total number of student: " + len(student_list))

            if user_object == "4":
                #4.VIEW REVIEWS
                pass
            if user_object == "5":                
                #5.REMOVE DATA
                pass
            
        if user_role == "User":
            if user_object == "1":
                pass
            if user_object == "2":
                pass
            if user_object == "3":
                pass
            if user_object == "4":
                pass
            if user_object == "5":                
                pass
        
      
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
        user_role = Main.login()
        # let the user take commands
           
        Main.process_operations(Main.show_menu(user_role), user_role)
        
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




class Admin(User):
    def constructor():
        print
#Admin only have attributes id(int, default value -1), username(str, default value “”)
#and password(str, default value “”) which can be inherited from the parent class.
    def register_admin():
#This method checks the user_admin.txt file to find out whether the username already
#exists or not. If not, register this admin. If it exists, do nothing.
    def extract_course_info():
        '''This method can get course information from the raw_data.txt. The extracted course
info should be saved into file following the format below:

“course_id;;;course_title;;;image_100x100;;;headline;;;num_of_
subscribers;;;avg_rating;;;course_content_length”.
For each line in the raw_data.txt file, you can copy and paste it to Json Parser Online
to check the format. Each line contains more than one course. All the corresponding
attributes can be found in the text. You can use the library re or str methods to
extract the data. The course content length in the text is like “40.5 hours”. Only 40.5
need to be retrieved. The course data will be saved into the course.txt file.
'''
    def extract_review_info():
        '''This method can get review information from the review_data folder. The extracted
review info saving format is
“review_id;;;review_content;;;review_rating;;;course_id”
The course id can be obtained from each file’s name in the review_data folder.
'''
    def extract_students_info():
        '''This method can get student information from the review_data folder. Each review
string contains one user information. Assume each user only has one review. The
attributes of each student are id, username, password, user_title, user_image_50x50,
user_initials and review_id. If a student’s id cannot be found in the string, you need
to generate it by calling the generate_unique_user_id() method defined in the User
class. The username should be generated by converting the user_title to lowercase
and replacing all the whitespace to underscore. The password is generated by
converting user_initials to lowercase and combining the user id. The password
expression looks like “user_initials + user_id + user_initials”. User_initials can be
obtained from the review data. For example, user_id is 12345, user initials is “DE”,
the password is “de12345de”. The student info will be written into file
user_student.txt and the format example is:
“id;;;username;;;password;;;user_title;;;user_image_50x50;;;us
er_initials;;;review_id”.
'''
    def extract_instructor_inro():
'''This method extracts information from the raw_data.txt file in the course_data folder.
Each course item contains several instructor information. The username is generated
by converting the instructor_display_name to lowercase and replacing all the
whitespace to underscore. The password uses the instructor id directly. The
instructor info saving format example is:
“id;;;username;;;password;;;display_name;;;job_title;;;image_1
00x100;;;course_id1–course_id2–course_id3–course_id4”.
Since each instructor can teach more than one course, before saving the instructor
information, you need to check whether the instructor already exists in the
user_instructor.txt file or not. 
If it exists, the course id should be appended to the
existing instructor string. For example, given an instructor string:
'''# 4466306;;;colt_steele;;;***4---***6---***6---***2;;;Colt Steele;;;Developer and Bootcamp Instructor;;;
#https://img-c.aaaaa.com/user/100x100/4466306.jpg;;;625204
'''

If a new course id 55555 is teached by this instructor, the string will be updated as
below:'''
# 4466306;;;colt_steele;;;***4---***6---***6---***2;;;Colt Steele;;;Developer and Bootcamp Instructor;;;
#https://img-c.aaaaa.com/user/100x100/4466306.jpg;;;625204--55555
'''

The format of instructor data will be explained in the Instructor class section.
'''        
    def extract_info():
'''This method calls all the extract info methods defined before, including
extract_course_info(), extract_instructor_info(), extract_students_info() and
extract_review_info().
'''        
    def remove_data():
'''This method can delete all the data in the course.txt, review.txt, user_student.txt and
user_instructor.txt files.'''
    def view_courses(args=[]):
'''This method will call the methods implemented in Course class to perform various
view course methods. The variable “args” can be an empty list or must contain two
elements. The first element is the command(can only be
“TITLE_KEYWORD/ID/INSTRUCTOR_ID”) and the second element is the value(could
be title keyword, course id or instructor id). For example, args=[“TITLE_KEYWORD”,
“web”]. If the “args” is an empty list, printing out the overview of courses (using the
course_overview method implemented in Course class). Add validations to provide
proper output message if user input incorrect command or values.'''
    def view_users():
'''This method prints out the total number of admin, instructor and students separately
with proper description messages.'''
    def view_users()
'''This method prints out the total number of admin, instructor and students separately
with proper description messages.'''
    def view_reviews(args=[]):
'''This method will call the methods implemented in Review class to perform various
view review methods. The args list can be empty or must contain two elements. The
first element is the command(can only be “ID/KEYWORD/COURSE_ID”) and the
second element is the value(could be review id, review keyword or course id). If the
args is an empty list, print out the overview of reviews(using the review_overview
method implemented in Review class); Add validations to provide proper output
message if user input incorrect command or values.'''
    def __str__():
'''Since the Admin class does not have any instance variables different from the User
class, you can use the parent class’s __str__ method directly.'''




class User:
# User class handles the fundamental methods of all users. The User class is the parent class of Admin, Instructor and Student classes.
    def constructor():
        pass
#A user must have id(int, default value -1), username(str, default value “”),
#password(str, default value “”).
    def generate_unique_user_id():
        pass
#This method checks the files user_admin.txt, user_instructor.txt and user_student.txt
#to generate an unique user id. The return result is a 10 digits integer.
    def encryption(input_password):
        pass
#This method encrypts the input_password to a string that is difficult to read by
#humans. Reuse the encryption algorithm that was in A1 to encode the input
#password. The encrypted password will be returned and the type is string.
    def login():
        pass
'''Each user can call the login method to perform authentication. In this login() method,
it is required to call the encryption() method defined before to encode the password.
The encoded password can be used to compare with the password extracted from
files. You are required to to check the user_admin.txt, user_instructor.txt and
user_student.txt file according to the username and password and return a tuple
which contains the login_result(bool type), login_user_role(str type, the values can
only be “Admin”, “Instructor”, “Student”), login_user_info(any type e.g. list or tuple 
or str, this value can be used to create different types of user object (Admin, Student
or Instructor)).'''
    def extract_info():
        pass
#This method prints out a message “You have no permission to extract information”.
    def view_courses(args=[]):
        pass
#This method prints out a message “You have no permission to view courses”.
    def view_users():
        pass
#This method prints out a message “You have no permission to view users”.
    def view_reviews(args=[]):
        pass
#This method prints out a message “You have no permission to view reviews”.
    def remove_data():
        pass
#This method prints out a message “You have no permission to remove data”.
    def __str__():
        pass
#This method returns a formatted user string: “user_id;;;username;;;password”. All the
#attributes are concatenated using “;;;”'''











   