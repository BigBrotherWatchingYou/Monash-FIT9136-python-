import os
def append_to_txt_file(file_name, text_to_append):
    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            file_contents = file.read()

        # Append the new text
        file_contents += '\n' + text_to_append

        # Open the file in write mode and overwrite the existing content
        with open(file_name, 'w') as file:
            file.write(file_contents)
        
        print("Text appended successfully to", file_name)
    
    except FileNotFoundError:
        print("Error: File not found.")

# Example usage:
append_to_txt_file("Assignment2/user_admin.txt", 'This is new text to append.')