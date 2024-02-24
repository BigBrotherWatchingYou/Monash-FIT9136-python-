old_list = [["a", 2, 3, 4], ["b", 5, 6, 8], ["c", 5, 6, 8], ["d", 67, 6, 8]]
name = input(" check username:")

def check_username(n, old_list):
    n = str(n)
    for k in old_list:
        if n == k[0]: 
            print('yes')
            return True
    
check_username(name, old_list)

