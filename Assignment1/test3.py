old_list = [["aa123", 2, 3, 4], ["b", 5, 6, 8], ["c", 5, 6, 8], ["d", 67, 6, 8]]
name = input(" check username:")

def check_username(n, old_list):
    n = str(n)
    i = 0
    for k in old_list:
        if n == k[0]: 
            print('yes')
            i = 1
    if i != 0:
        return True
    else:
        print("not in list")
        return False
check_username(name, old_list)

