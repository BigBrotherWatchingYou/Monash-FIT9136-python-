class Course:
    def constructor():
        pass
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
        try:
            with open("Assignment2/course_file.txt",'r') as file:
                course_list = [k.strip() for k in file.readlines()]
                matched_course = []
                for course in course_list:
                    if keyword.lower() in str(course.lower()):
                        matched_course.append(course)
            
        except FileNotFoundError:
            return "File not find"
        
        return matched_course
    
    def find_course_by_id(course_id):
        matched_id = []
        try:
            with open("Assignment2/course_file.txt",'r') as c:
                course_file = [t.strip().split("::") for t in c]
                for course in course_file:
                    if str(course_id) == course[0]:
                        matched_id.append(course)
                
        except FileNotFoundError:
            return "File not find"
        
        return matched_id
        
    '''This method has a positional argument course id(int or str). You are required to
search for the course according to the course id. A course object will be returned. If
not found, return None.'''
    def find_course_by_instructor_id(instructor_id):
        matched_id = []
        try:
            with open("Assignment2/course_file.txt",'r') as c:
                course_file = [t.strip().split(";;;") for t in c.readlines() if t.strip()]
                
                for course in course_file:
                    if str(instructor_id) == course[2]:
                        matched_id.append(course)
                    
                
        except FileNotFoundError:
            return "File not find"
        
        return matched_id
        #print("matched:", matched_id)
    
    '''This method has a positional argument instructor id(int or str). Based on the
instructor id, a list of course objects will be generated and returned. The result list
looks like [Course(), Course(), Course()….]. If not found, return an empty list.'''
    def courses_overview():
        total_number = 0    
        try:
            with open("Assignment2/course_file.txt",'r') as c:
                courses = [t.strip().split(";;;") for t in c.readlines() if t.strip()]
                total_number = len(courses)                
                    
                
        except FileNotFoundError:
            print("file does not exist")
        
        return total_number
    
print(course_num)
    '''This method returns a string that shows the total number of courses.'''
    def __str__():
        pass
    '''Return a string containing all course information.'''



course = "course_id;;;course_title;;;image_100x100;;;   ;;;num_of_\
subscribers;;;avg_rating;;;course_content_length”.\
For each line in the raw_data.txt file, you can copy and paste it to Json Parser Online\
to check the format. Each line contains more than one course. All the corresponding\
attributes can be found in the text. You can use the library re or str methods to\
extract the data. The course content length in the text is like “40.5 hours”. Only 40.5\
need to be retrieved. The course data will be saved into the course.txt file."

review = "“review_id;;;review_content;;;review_rating;;;course_id”\
The course id can be obtained from each file's name in the review_data folder.\
'''"



   