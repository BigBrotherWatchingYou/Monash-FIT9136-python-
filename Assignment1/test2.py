import random

def generate_user_id(digitsnumber):
    user_name = ''.join(str(random.randint(0,9)) for i in range(digitsnumber))
    
    return user_name

f = generate_user_id(8)  
print(f)
