class Instructor(User):
#The Instructor class inherits from the User class.
    def constructor:
'''The attributes of instructor are id(int, default value -1), username(str, default value
“”), password(str, default value “”), display_name(str, default value “”), job_title(str,
default value “”), image_100x100(str, default value “”), course_id_list(list, default
value []).'''
    def view_courses(args=[]):
'''Print out all the courses taught by this instructor. This can be reached by calling the
method implemented in the Course class. If the number of courses is greater than 10,
only print 10 courses. The args positional argument is not used in this method.'''
    def view_reviews(args=[]):
'''Print out all the reviews belong to the courses this instructor teaches. This can be
achieved by calling the method implemented in the Course class. If the number of
reviews is greater than 10, only print 10 reviews. Also print out the total number of
all reviews. The args positional argument is not used in this method.'''
    def __str__():
        #user the parent class __str__ metod. The return result format is:
'''“user_id;;;username;;;password;;;display_name;;;job_title;;;im
age_100x100;;;123123-323-32-3123-3123”.'''