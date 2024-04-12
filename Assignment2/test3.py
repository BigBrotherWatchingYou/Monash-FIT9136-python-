class a:
    def find_course_by_instructor_id(instructor_id):
        matched_id = []
        try:
            with open("Assignment2/course_file.txt",'r') as c:
                course_file = [t.strip().split(";;;") for t in c.readlines() if t.strip()]
                
                for course in course_file:
                    if str(instructor_id) == course[2]:
                        matched_id.append(course)
                    
                
        except FileNotFoundError:
            pass
        
        return matched_id
        #print("matched:", matched_id)
    
a.find_course_by_instructor_id(4287)