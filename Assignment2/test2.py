import os
import re
matched_result = []
try:
    with open("Assignment2/course_file.txt",'r') as c:
        course_file = [t.strip().split(";;;") for t in c.readlines() if t.strip()]
        print(course_file)
        #for course in course_file:
           # print(course[0])
        
           
    
    #if str(instructor_id) in [course.split(";;;")[2]]:
    #matched_result.append(course)
    
    #if str(instructor_id) == str(course)[0]:
    #    matched_result.append(course)

except FileNotFoundError:
    pass