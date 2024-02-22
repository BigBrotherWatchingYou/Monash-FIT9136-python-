
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
    file.print_info()
    return inputname, inputphone, inputemail
    
Input_info()    


