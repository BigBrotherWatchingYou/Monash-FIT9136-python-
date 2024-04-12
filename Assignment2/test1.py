import os
import re
def view_courses():
       
        try:
            with open("Assignment2/course_file.txt", 'r') as c:
                course_id_list = [k.strip().split(";;;")[0] for k in c.readlines()]
                
                all_course_list =[]
                for info in c.readlines():
                    all_course_list.append(info.strip().split(";;;")[0])

                #course_id_list = [k.strip().split("::")[0] for k in c.readlines()]
                
                #all_course_list = [course.strip() for course in c.readlines()]
                
                '''course_instructor_list = []
                for m in all_course_list:
                    list = m.split(";;;")
                    course_instructor_list.append(list)'''
                
                
        except FileNotFoundError:
            pass
        for course_id in course_id_list:
            print( "id:---",course_id)    
        print("all course_list): ",all_course_list)
        #for k in all_course_list:
        #    print(k)
        #print(course_instructor_list)
        
view_courses()