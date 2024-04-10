import os
import re
def view_users():
    try:
        with open("Assignment2/user_admin.txt") as file:
            admin_list = file.readlines()
            
    except FileNotFoundError:
        admin_list = []    
    print("total number of Admin: " , len(admin_list))
    # print("total number of instructor: " + len(instructor_list))
    # print("total number of student: " + len(student_list))
    
view_users()