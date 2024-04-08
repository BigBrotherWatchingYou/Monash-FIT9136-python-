import os
try:
    with open("Assignment2/user_admin.txt") as f:
        admin_data = [k.strip().split(";;;")[1].strip("{}") for k in f]
except FileExistsError:
    admin_data = []
print(admin_data)    
while True:
    # loop
    username = input(("Enter your name (or 'quit' to quit): ").strip())
    if username.lower() == "quit":
        break
    
    if any (username in  admin_data ):
        # username exists
        print("Username already exists. Please choose a different username.")
        continue
        