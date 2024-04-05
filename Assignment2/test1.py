import os

cour_file = open("Assignment2/user_admin.txt",'r' )
cour_list = cour_file.read().split()
file = []
cour_file.close()

for k in cour_list:
    print(k)