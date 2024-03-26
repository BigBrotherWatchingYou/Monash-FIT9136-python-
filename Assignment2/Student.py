class Student(User):

Student class inherits from the User class.
    def constructor:
'''The attributes of student are id(int, default value -1), username(str, default value “”),
password(str, default value “”), user_title(str, default value “”), user_image_50x50(str,
default value “”), user_initials(str, default value “”), review_id(int, default value -1).'''
    def view_courses(args=[]):
'''This method prints out the course this student registered. If a student reviews a
course, it is assumed that the student is registered in that course. The args positional
argument is not used in this method. Just have it when doing method declaration.'''
    def view_reviews(args=[]):
'''This method prints out the review this student wrote. The args positional argument is
not used in this method. Just have it when doing method declaration.'''
    def __str__():
'''Use the parent class __str__ method. The return result format
is:”user_id;;;username;;;password;;;title;;;image_50x50;;;initia
ls;;;review_id”.'''