def view_courses():
    course_id_list = [] 
    all_course_list = []
    course_instructor_list = []
    
    try:
        with open("Assignment2/course_file.txt", 'r') as c:
            # Use a list comprehension to strip whitespace from each line and iterate over them
            all_course_list = [course.strip() for course in c.readlines()]
            
            # Optionally, you can convert the list comprehension to a list
           
            
            # You can further process each course line as needed
            
    except FileNotFoundError:
        pass

    # Print the list of courses
    print(all_course_list)
    
view_courses()