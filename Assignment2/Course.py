class Course:
    def constructor():
'''The attributes of course are course_id(int, default value -1), course_title(str, default
value “”), course_image_100x100(str, default value “”), course_headline(str, default

value “”), course_num_subscribers(int, default value -1), course_avg_rating(float,
default value -1.0), course_content_length(float, default value -1.).'''
    def find_course_by_title_keyword(keyword):
'''This method has a positional argument keyword(str). Based on the given keyword, it
searches the course title of all courses in the course.txt file to find the result. All the
result courses will be created as a course object and added into a result list. Finally,
return the result list. The result list looks like [Course(), Course(), Course()….]. If not
found, return an empty list.'''
    def find_course_by_id(course_id):
'''This method has a positional argument course id(int or str). You are required to
search for the course according to the course id. A course object will be returned. If
not found, return None.'''
    def find_course_by_instructor_id(instructor_id):
'''This method has a positional argument instructor id(int or str). Based on the
instructor id, a list of course objects will be generated and returned. The result list
looks like [Course(), Course(), Course()….]. If not found, return an empty list.'''
    def courses_overview():
'''This method returns a string that shows the total number of courses.'''
    def __str__():
'''Return a string containing all course information.'''