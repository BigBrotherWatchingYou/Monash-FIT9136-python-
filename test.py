class Create_info:
    # create information
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    def print_info(self):
        print(self.name)
        print(self.phone)
        print(self.email)
inputname = input('yourname')
inputphone = input('yourphone')
inputemail = input('youremail')
file = Create_info(inputname, inputphone, inputemail)
file.print_info()