import string
#.1. Get user input function
'''ask the user to input a corresponding value and return its input
1. the input must match"requirements" or will be asked to input again, until 
a valid one is inputted
2. only valid result will return'''
def get_input(requirement, user_input):
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
            
            return get_input('letter', user_input)

    # requirement : numbers only        
    if requirement == 'digit':
        if user_input.isdigit():
            return user_input
        else:
            print("invalid, numbers only")
            user_input == input('only numbers form 0-9\ntype again')
            
            return get_input('digit', user_input)

    # requirement of email
    if requirement == 'email':
        if '@' and '.com' in user_input:
            print('valid email:'+ user_input)
            return user_input
        else:
            print('email should include @ or .com')
            user_input = input('enter email')
            
            return get_input('email', user_input)

    # requirement of 'password = letter(Upper+lower) + digit + @#$@#$  and 16 >=length >= 8'
    if requirement == 'password':
        l = 0
        d = 0
        s = 0
        le = 0
        if len(user_input) >= 16:
            print('too long, should be less than 16')
            user_input = input('input a new password')
            return get_input("password", user_input)
        
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
            print('too simple password')
            user_input = input('letter(Upper + lower) + digit + @#$@#$  and 16 >=length >= 8')
            return get_input("password", user_input)

          
#.2. Encryption function
'''copied from chatgpt
input a message and return a decrypted message
able to decrypt'''
def xor_encrypt_decrypt(message, key):
    # Initialize an empty string to store the result
    result = ""

    # Iterate over each character in the message
    for char in message:
        # Perform XOR operation between the character and the key character
        # Use modulo operator to cycle through the key if it's shorter than the message
        result += chr(ord(char) ^ ord(key))

    return result

# Message to be encrypted
message = "Hello, this is a secret message!"
# Key for encryption
key = "k"

# Encrypt the message
encrypted_message = xor_encrypt_decrypt(message, key)
print("Encrypted message:", encrypted_message)
req = input('what do you want to input:')
m = input('please type here:')

get_input(req, m)

# Decrypt the message using the same key
decrypted_message = xor_encrypt_decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)


#.3. Generate user id function
'''came out with a random number, with specific number_of_digits'''
import random

def generate_user_id(digitsnumber):
    ge_name = ''.join(str(random.randint(0,9)) for i in range(digitsnumber))
    print('your user name:' + ge_name)
    return ge_name




#.4. Check username exist function
def check_username(username, old_list):
    username = str(username)
    i = 0
    for k in old_list:
        if username == k[0]: 
            print('user exist')
            i = 1
    if i != 0:
        return True
    else:
        print("not in list")
        return False


old_list = [["aa123", 2, 3, 4], ["b", 5, 6, 8], ["c", 5, 6, 8], ["d", 67, 6, 8]]    


#.5. Authenticate username and password function
'''1.please type your username
2. check if username exist
3. please enter your password
4. check if password match
5. give access and provide the information list  '''
def authen_username_password(user_name, password):
    user_name = str(user_name)
    password = str(password)
    if check_username(user_name, old_list) == True:
        for m in old_list:
            if user_name == m[0]:

                if password == m[2]:
                    print('password matched')
                    return True
                else:
                    print("password incorrect")
                    return False

    else: 
        print('unexist username')
        return False
    

authen_username_password(username, password)
#. Add user to list function
def add_user(username, password, userid, old_list):
    if check_username(username, old_list) == False:
        return True
#. Test function
username = input("input your name")
if check_username(username, old_list) == True:
    authen_username_password(username, old_list)
else:
    print("user do not exist")
    choice = input("do you want to create a new account? enter y/n ")
    if choice == "y":
        
        add_user(get_input('letter', username), get_input('password', username), generate_user_id(5), old_list)
    else:
        print("press'esc' to close\n to continue, enter 'c'")


#. Code encapsulation