def search_courses(keyword):
    try:
        with open("Assignment2/course_file.txt", 'r') as file:
            # Read all lines and strip any leading or trailing whitespace
            all_courses = [course.strip() for course in file.readlines()]
            
            # Initialize a list to store matching courses
            matching_courses = []

            # Iterate through each course line in all_courses
            for course in all_courses:
                # Check if the keyword exists in the course line
                if keyword.lower() in course.lower():
                    matching_courses.append(course)

            # If there are matching courses, print them
            if matching_courses:
                print("Matching courses for keyword '{}':".format(keyword))
                for course in matching_courses:
                    print(course)
            else:
                print("No matching courses found for keyword '{}'.".format(keyword))
                
    except FileNotFoundError:
        print("File not found.")

# Example usage:
search_courses("intro")