import re
import os
import random
from User import User
from Course import Course
from Review import Review

class Admin(User):
    def constructor():
        print("1")
        pass
    #Admin only have attributes id(int, default value -1), username(str, default value “”)
    #and password(str, default value “”) which can be inherited from the parent class.
    
    def regis():
        print("welcome to register, your role is: admin")
        # open and read admin.txt
        try:
            with open("Assignment2/user_admin.txt") as file:
                admin_list = [k.split(";;;")[1].strip("{}") for k in file if k.strip()]
                # unable to read space lines
            print("admin_list:",admin_list)
        except FileNotFoundError:
            admin_list = []
            
        try:
            with open("Assignment2/user_admin.txt") as file_2:
                id_list = [m.split(";;;")[0].strip("{}") for m in file_2 if m.strip()]
                # unable to read space lines
            print("userid_list:",id_list)
        except FileNotFoundError:
            id_list = []
    
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
        
        def generate_userid():
            gen_id = random.randint(10000,99999)
            if gen_id in id_list: # userid already exists
                return generate_userid
            else:
                return gen_id
                
        username = input_username()    
        password = input_password()    
        userid = generate_userid()
        userinfo = f"{userid};;;{username};;;{password}"
            
        with open("Assignment2/user_admin.txt",'a') as f:
            f.write(f"\n{userinfo}")
        print("Admin created successfully.")
     
            
    #This method checks the user_admin.txt file to find out whether the username already
        #exists or not. If not, register this admin. If it exists, do nothing.
    def extract_course_info():
        pass
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
        print(review)
        '''This method can get review information from the review_data folder. The extracted
review info saving format is
“review_id;;;review_content;;;review_rating;;;course_id”
The course id can be obtained from each file's name in the review_data folder.
'''
    def extract_students_info():
        print(student_list)
        '''This method can get student information from the review_data folder. Each review
string contains one user information. Assume each user only has one review. The
attributes of each student are id, username, password, user_title, user_image_50x50,
user_initials and review_id. If a student''s id cannot be found in the string, you need
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
    def extract_instructor_info():
        print(instructor_list)
        pass
        '''This method extracts information from the raw_data.txt file in the course_data folder.
            Each course item contains several instructor information. The username is generated
        by converting the instructor_display_name to lowercase and replacing all the
                whitespace to underscore. The password uses the instructor id directly. The
        instructor info saving format example is:
        “id;;;username;;;password;;;display_name;;;job_title;;;image_1
                00x100;;;course_id1-course_id2-course_id3-course_id4”.
        Since each instructor can teach more than one course, before saving the instructor
        information, you need to check whether the instructor already exists in the
        user_instructor.txt file or not. 
        If it exists, the course id should be appended to the
        existing instructor string. For example, given an instructor string:
        '''# 4466306;;;colt_steele;;;***4---***6---***6---***2;;;Colt Steele;;;Developer and Bootcamp Instructor;;;
        #https://img-c.aaaaa.com/user/100x100/4466306.jpg;;;625204
        '''If a new course id 55555 is teached by this instructor, the string will be updated as
        below:'''
        # 4466306;;;colt_steele;;;***4---***6---***6---***2;;;Colt Steele;;;Developer and Bootcamp Instructor;;;
        #https://img-c.aaaaa.com/user/100x100/4466306.jpg;;;625204--55555
        '''

    The format of instructor data will be explained in the Instructor class section.
    '''        
    def extract_info():
        pass
        '''This method calls all the extract info methods defined before, including
        extract_course_info(), extract_instructor_info(), extract_students_info() and
        extract_review_info().
        '''        
    def remove_data():
        pass
        '''This method can delete all the data in the course.txt, review.txt, user_student.txt and
        user_instructor.txt files.'''
    def view_courses(args=[]):
        Course.
        '''This method will call the methods implemented in Course class to perform various
        view course methods. The variable “args” can be an empty list or must contain two
        elements. The first element is the command(can only be
        “TITLE_KEYWORD/ID/INSTRUCTOR_ID”) and the second element is the value(could
        be title keyword, course id or instructor id). For example, args=[“TITLE_KEYWORD”,
        “web”]. If the “args” is an empty list, printing out the overview of courses (using the
        course_overview method implemented in Course class). Add validations to provide
        proper output message if user input incorrect command or values.'''

        
    def view_users():
        try:
            with open("Assignment2/user_admin.txt") as file:
                admin_list = file.readlines()
            
        except FileNotFoundError:
            admin_list = []    
        print("total number of Admin: " , len(admin_list))
        # print("total number of instructor: " + len(instructor_list))
        # print("total number of student: " + len(student_list))

        '''This method prints out the total number of admin, instructor and students separately
        with proper description messages.'''

    
    def view_reviews(args=[]):
        print(review)
    '''This method will call the methods implemented in Review class to perform various
view review methods. The args list can be empty or must contain two elements. The
first element is the command(can only be “ID/KEYWORD/COURSE_ID”) and the
second element is the value(could be review id, review keyword or course id). If the
args is an empty list, print out the overview of reviews(using the review_overview
method implemented in Review class); Add validations to provide proper output
message if user input incorrect command or values.'''

    def __str__():
        pass
    '''Since the Admin class does not have any instance variables different from the User
class, you can use the parent class's __str__ method directly.'''