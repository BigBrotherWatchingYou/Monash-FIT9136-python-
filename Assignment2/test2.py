def courses_overview():
    total_number = 0    
    try:
        with open("Assignment2/course_file.txt",'r') as c:
            courses = [t.strip().split(";;;") for t in c.readlines() if t.strip()]
            total_number = len(courses)                
                    
                
    except FileNotFoundError:
        print("file does not exist")
        
    return total_number
course_num = courses_overview()
print(course_num)