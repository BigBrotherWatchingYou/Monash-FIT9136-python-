import os
try:
    with open("Assignment2/course_file.txt",'r') as c:
        course_file = [t.strip().split(";;;") for t in c.readlines() if t.strip()]
        total_number = len(course_file)
                
                    
                
except FileNotFoundError:
    pass
        
print(total_number)