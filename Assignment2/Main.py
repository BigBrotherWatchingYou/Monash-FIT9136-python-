class User:
# User class handles the fundamental methods of all users. The User class is the parent class of Admin, Instructor and Student classes.
    def constructor():
#A user must have id(int, default value -1), username(str, default value “”),
#password(str, default value “”).
    def generate_unique_user_id():
#This method checks the files user_admin.txt, user_instructor.txt and user_student.txt
#to generate an unique user id. The return result is a 10 digits integer.
    def encryption(input_password):
#This method encrypts the input_password to a string that is difficult to read by
#humans. Reuse the encryption algorithm that was in A1 to encode the input
#password. The encrypted password will be returned and the type is string.
    def login():
'''Each user can call the login method to perform authentication. In this login() method,
it is required to call the encryption() method defined before to encode the password.
The encoded password can be used to compare with the password extracted from
files. You are required to to check the user_admin.txt, user_instructor.txt and
user_student.txt file according to the username and password and return a tuple
which contains the login_result(bool type), login_user_role(str type, the values can
only be “Admin”, “Instructor”, “Student”), login_user_info(any type e.g. list or tuple 8
or str, this value can be used to create different types of user object (Admin, Student
or Instructor)).'''
    def extract_info():
#This method prints out a message “You have no permission to extract information”.
    def view_courses(args=[]):
#This method prints out a message “You have no permission to view courses”.
    def view_users():
#This method prints out a message “You have no permission to view users”.
    def view_reviews(args=[]):
#This method prints out a message “You have no permission to view reviews”.
    def remove_data():
#This method prints out a message “You have no permission to remove data”.
    def __str__():
#This method returns a formatted user string: “user_id;;;username;;;password”. All the
#attributes are concatenated using “;;;”'''