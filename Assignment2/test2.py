import os
import re
def view_courses():
       
        try:
            with open("Assignment2/course_file.txt", 'r') as c:
                all_course_list =[m.strip() for m in c.readlines()]
                #course_id_list = [k.strip().split(";;;")[0] for k in all_course_list]
                course_instructor_list = [] 
                
                for course in all_course_list:
                    part = course.split(";;;")
                    if len(part) >= 2:
                        course_instructor_list.append(part[3])
                '''course_instructor_list = []
                for m in all_course_list:
                    list = m.split(";;;")
                    course_instructor_list.append(list)'''
                
                
        except FileNotFoundError:
            pass
        #for course_id in course_id_list:
            #print( "id:---",course_id)    
        #print("all course_list): ",all_course_list)
        print("instructor:",course_instructor_list)
view_courses()        
