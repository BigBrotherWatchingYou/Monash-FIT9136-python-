import os

file_path = "course_file.txt"

# Check if the file exists
if os.path.exists(file_path):
    # Open the text file in read mode
    with open(file_path, 'r') as file:
        # Read the contents of the file
        file_contents = file.read()

        # Print the contents
        print(file_contents)
else:
    print(f"The file '{file_path}' does not exist.")