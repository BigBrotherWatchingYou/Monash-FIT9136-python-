
'''how this work:
1. let user input info
2. check info
3. create info and store in category'''
import string
class input:
    





class create:
    # get the user input
    def create_name(self, name):
        self.name = name
    def create_phone(self, phone):
        self.phone = phone
    def create_email(self, email):
        self.email = email


def is_alpha(k):
    alphabet = list(string.ascii_lowercase)
    #check if the input is in alphabet
    i = 0
    for m in k:
        if m not in alphabet:
            i += 1
    if i != 0:
        return False
    else: 
        return True