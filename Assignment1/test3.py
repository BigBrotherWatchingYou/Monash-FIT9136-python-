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
    
username = input('username:')
password = input('type passwrod:')
authen_username_password(username, password)