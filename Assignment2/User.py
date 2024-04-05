import random

class User:
    # User class handles the fundamental methods of all users. The User class is the parent class of Admin, Instructor and Student classes.
    def constructor():
        pass
        #   A user must have id(int, default value -1), username(str, default value “”),
        #password(str, default value “”).
    def generate_unique_user_id():
        # rule: the user id should not be the same of all users
        all_admin = open("Assignment2/course_file.txt", r)
    #This method checks the files user_admin.txt, user_instructor.txt and user_student.txt
    #to generate an unique user id. The return result is a 10 digits integer.
    def encryption(input_password):
        pass
    #  This method encrypts the input_password to a string that is difficult to read by
    #humans. Reuse the encryption algorithm that was in A1 to encode the input
    #password. The encrypted password will be returned and the type is string.
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
            if username not in (admin_list and  instructor_list and  student_list):
                #user do not exist
                print("user id do not exist")
                return Main.login()
            if userdata[username]["password"] == password:
                # login successful
                return username
            else:
                # login failed
                print("incorrect username and password\n\
                    input format:username password")
                return User.login()
            
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



