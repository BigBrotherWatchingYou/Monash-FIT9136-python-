def view_courses():
        course_id_list = [] 
        all_course_list =[]
        course_instructor_list = []
        
        try:
            with open("Assignment2/course_file.txt") as c:
                course_id_list = [k.strip().split("::")[0] for k in c if k.strip()]
                all_course_list = [c]
                course_instructor_list = [k.strip().split(";;;")[2] for k in c if k.strip()]
                
        except FileNotFoundError:
            course_id_list = [] 
            all_course_list =[]
            course_instructor_list = []

        print(course_id_list)#all_course_list,course_instructor_list)
        
view_courses()