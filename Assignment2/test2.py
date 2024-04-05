import os

def read_and_print_txt_files():
    current_directory = os.path.join(os.getcwd(), 'Assignment2')
    file_path = os.path.join(current_directory, 'course_file.txt')
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            print(file.read())
    else:
        print("The file 'course_file.txt' does not exist in the 'Assignment2' directory.")

read_and_print_txt_files()