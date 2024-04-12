def find_course_by_id(course_id):
    try:
        with open("Assignment2/course_file.txt",'r') as c:
            course_file = [t.strip().split("::") for t in c]
            for course in course_file:
                
                if str(course_id) == course[0]:
                    print("find course:", course)
                
    except FileNotFoundError:
        pass
    
find_course_by_id(34567)