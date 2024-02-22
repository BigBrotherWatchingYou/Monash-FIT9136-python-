import string
#. Get user input function
'''ask the user to input a corresponding value and return its input
1. the input must match"requirements" or will be asked to input again, until 
a valid one is inputted
2. only valid result will return'''
def check_input_requirements(requirement, user_input):
    '''# requirement type: 
    1.letter only
    2.digits only
    3.email only
    4. complex_password 
    # tips: type and press'Enter' can pass the section
    user_input = str(user_input)
    # deal with space input in Feb.23.2024'''
    if user_input == '':
        return False
    if requirement == 'letter':
        if user_input.isalpha():
            print('valid letter')
            return user_input
        else:
            print("invalid, letters only")
            user_input = input('only be letters from a-z(or A-Z)\ntype again')
            user_input = str(user_input)
            return check_input_requirements('letter', user_input)

    # requirement : numbers only        
    if requirement == 'digit':
        if user_input.isdigit():
            return user_input
        else:
            print("invalid, numbers only")
            user_input == input('only numbers form 0-9\ntype again')
            user_input = str(user_input)
            return check_input_requirements('digit', user_input)

    # requirement of email
    if requirement == 'email':
        if '@' and '.com' in user_input:
            print('valid email:'+ user_input)
            return user_input
        else:
            print('email should include @ or .com')
            user_input = input('enter email')
            user_input = str(user_input)
            return check_input_requirements('email', user_input)

    # requirement of 'password = letter(Upper+lower) + digit + @#$@#$  and 16 >=length >= 8'
    if requirement == 'password':
        l = 0
        d = 0
        s = 0
        le = 0
        if len(user_input) >= 16:
            print('too long, should be less than 16')
            user_input = input('input a new password')
            return check_input_requirements("password", user_input)
        
        if len(user_input) >= 8 and len(user_input) <= 16:
            le += 1
            for char in user_input:
                if char.isalpha():
                    l += 1
                    return l 
                if char.isdigit():
                    d += 1
                    return d
                if char in r'[^a-zA-Z0-9\s]':
                    s += 1
                    return s
            
            if l != 0 and d != 0 and s != 0 and le != 0:
                print('valid password')
                return user_input
        else:
            print('too simple password')
            user_input = input('letter(Upper + lower) + digit + @#$@#$  and 16 >=length >= 8')
            return check_input_requirements("password", user_input)
check_input_requirements("password", "aaaaaaaaaaaaaaa@#$123")
#. Encryption function

#. Generate user id function

#. Check username exist function

#. Authenticate username and password function

#. Add user to list function

#. Test function

#. Code encapsulation