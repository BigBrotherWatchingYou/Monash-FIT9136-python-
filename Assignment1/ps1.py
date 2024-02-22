
'''how this work:
1. let user input info
2. check info
3. create info and store in category'''
import string


class Create_info:
    # create information
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    def print_info(self):
        print('yourname:' + self.name)
        print('yourphone:' + self.phone)
        print('youremail:' + self.email)

def Input_info():
    inputname = input('yourname')
    inputphone = input('yourphone')
    inputemail = input('youremail')
    file = Create_info(inputname, inputphone, inputemail)
    return inputname, inputphone, inputemail
    
def check_name(inputname):
    if inputname.isalpha():
        return inputname 
    else: 
        inputname = input("your name should be letters only, enter a new name")
        return inputname
def check_phone(inputphone):
    if inputphone.isdigit():
        return inputphone
    else:
        inputphone = input("your phone should be digit only, enter a new phone")
        return inputphone