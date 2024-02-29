class data_function(object):
    # for 1.encrypt\decrypt and 2.check input requirements
    input0 = str(object)
    def xor_encrypt_decrypt(input0):
        # Initialize an empty string to store the result
        result = ""
        key = "k"
        # Iterate over each character in the message
        for char in input0:
            # Perform XOR operation between the character and the key character
            # Use modulo operator to cycle through the key if it's shorter than the message
            result += chr(ord(char) ^ ord(key))
        return(result) 
    def check_req(requirement, user_input):
        '''# requirement type: 
        1.letter only
        2.digits only
        3.email only
        4. complex_password 
        # tips: type and press'Enter' can pass the section
    
        # deal with space input in Feb.23.2024'''
        user_input = str(user_input)
        requirement = str(requirement)
        if user_input == '':
            return False
        
        if requirement == 'letter':
            
            if user_input.isalpha():
                print('valid letter')
                return user_input
            else:
                print("invalid, letters only")
                user_input = input('only be letters from a-z(or A-Z)\ntype again')
                return check_req('letter', user_input)

        # requirement : numbers only        
        if requirement == 'digit':
            
            if user_input.isdigit():
                return user_input
        else:
            print("invalid, numbers only")
            user_input == input('only numbers form 0-9\ntype again')
            
            return check_req('digit', user_input)

        # requirement of email
        if requirement == 'email':
            
            if '@' and '.com' in user_input:
                print('valid email:'+ user_input)
                return user_input
            else:
                print('email should include @ or .com')
                user_input = input('enter email')
            
                return check_req('email', user_input)

        # requirement of 'password = letter(Upper+lower) + digit + @#$@#$  and 16 >=length >= 8'
        if requirement == 'password':
            l = 0
            d = 0
            s = 0

            if len(user_input) >= 16:
                print('too long, should be less than 16')
        
            if len(user_input) >= 8 and len(user_input) <= 16:
                le += 1
            for char in user_input:
                    if char.isalpha():
                        l += 1
 
                    if char.isdigit():
                        d += 1

                    if char in r'[^a-zA-Z0-9\s]':
                        s += 1
            
            if l != 0 and d != 0 and s != 0 and le != 0:
                print('valid password')
                return user_input
            else:
                print('password should be : letter+ digit + symbols and length between 8-16')
                return False      


class User_management(self):
    def user__init__(self, username, userid, password, email):
        self.list = {}
        self.username = username
        self.userid = userid
        self.password = password
        self.email = email
        self.list[userid] = {self.username, self.userid, self.password, self.email}
        
    def add_user_to_user_id_list(userid, user_id_list):
        user_id_list.append(userid)

    def check_user(userid):
        if userid in user_id_list:
            print(f"user{userid}exists")
            return True
        else:
            print(f"user{userid}does not exists")
            return False
        
    
    def add_user(self, username, userid, password, email):
        self.list[userid] = {"username": username, "userid": userid, "userpassword": password, "useremail": email}
        user_id_list.append(userid)
    
    def authenticate_user(userid, password):
        if user_id_list[userid]["password"] == password:
            return True
        else:
            print("password incorrect")
            return False
            
    def update_user(self, userid, new_id = None, new_password = None, new_email = None):
        if userid in user_id_list:
            if new_id:
                self.list[userid]["userid"] = new_id
            if new_password:
                self.list[userid]["password"] = new_password
            if new_email:
                self.list[userid]["email"] = new_email

    
    def generate_user_id(digitsnumber):
        ge_name = ''.join(str(random.randint(0,9)) for i in range(digitsnumber))
        print('your user name:' + ge_name)
        return ge_name

data_function.check_req("letter","fuckyou")
