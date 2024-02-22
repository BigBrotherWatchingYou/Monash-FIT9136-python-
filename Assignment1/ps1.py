import string
#. Get user input function
'''ask the user to input a corresponding value and return its input
1. the input must match"requirements" or will be asked to input again, until 
a valid one is inputted
2. only valid result will return'''
def check_input_requirements(requirement, user_input):
    # requirement : letter only
    if requirement == 'letter':
        if user_input.isalpha():
            return user_input
        else:
            print("invalid, letters only")
            user_input = input('only be letters from a-z(or A-Z)\ntype again')

    # requirement : numbers only        
    if requirement == 'digit':
        if user_input.isdigit():
            return user_input
        else:
            print("invalid, numbers only")
            user_input == input('only numbers form 0-9\ntype again')

    # requirement of email
    if requirement == 'email':
        if '@' and '.com' in user_input:
            return user_input
        else:
            print('email should include @ or .com')
            user_input = input('enter email')

    # requirement of 'password = letter(Upper+lower) + digit + @#$@#$  and 16 >=length >= 8'
    if requirement == 'password':
        L = 0
        D = 0
        S = 0
        Le = 0
        if 16 >= len(user_input) >= 8:
            Le += 1
            for char in user_input:
                if char.isalpha():
                    L += 1
                    return L 
                if char.isdigit():
                    D += 1
                    return D
                if char in r'[^a-zA-Z0-9\s]':
                    S += 1
                    return S
            return Le, L, D, S
        if L != 0 and D != 0 and S != 0 and Le != 0:
            return True
        else:
            print("password should include:\nletter(Upper or lower) + digit + @#$@#$  and 16 >=length >= 8") 
            return False

                

        else:
            print('too simple password')
            
            user_input = input('letter(Upper + lower) + digit + @#$@#$  and 16 >=length >= 8')

#. Encryption function

#. Generate user id function

#. Check username exist function

#. Authenticate username and password function

#. Add user to list function

#. Test function

#. Code encapsulation