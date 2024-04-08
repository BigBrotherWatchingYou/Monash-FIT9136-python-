import os
import re
with open("Assignment2/user_admin.txt") as file:
    userlist = [line.strip().split("username": )[1] for line in file]
print(userlist)