def courses_overview():
    total_number = 0    
    try:
        with open("Assignment2/course_file.txt",'r') as c:
            course_file = [t.strip().split(";;;") for t in c.readlines() if t.strip()]
            total_number = len(course_file)                
                    
                
    except FileNotFoundError:
        print("file does not exist")
        
    return total_number

print(courses_overview())