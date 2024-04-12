def find_course_by_title_keyword(keyword):
        
        '''This method has a positional argument keyword(str). Based on the given keyword, it
        searches the course title of all courses in the course.txt file to find the result. All the
        result courses will be created as a course object and added into a result list. Finally,
        return the result list. The result list looks like [Course(), Course(), Course()….]. If not
        found, return an empty list.'''
        try:
            with open("Assignment2/course_file.txt",'r') as file:
                course_list = [k.strip() for k in file.readlines()]
                for course in course_list:
                    if keyword.lower() in str(course.lower()):
                        print("matched result: ",course)
            
        except FileNotFoundError:
            pass
        
find_course_by_title_keyword("Introduction")        