import requests
url = "https://github.com/BigBrotherWatchingYou/Monash-FIT9136-python-/blob/main/Assignment2/raw_data.txt"
read_file = requests.get(url)
if read_file.status_code == 200:
    # Get the file contents from the read_file
    file_contents = read_file.text

    # Print the contents
    print(file_contents)
else:
    print("Failed to fetch file:", read_file.status_code)