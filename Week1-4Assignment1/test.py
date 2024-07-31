operation = "pla00"
check_list = ["abcdefghijklm",
 "nopqrstuvwxyz"]


def check_key_valid(input_key, checking_list):
    # check if the key is valid
    for items in input_key:
        print(items)
        if items in checking_list[0]:
            print("list1")
        elif items in checking_list[1]:
            print('list2')    
        else:
            print("invalid")

def check_valid(input_key, dictionary):
    return_value = True
    for item in input_key:
        if item not in dictionary[0] and item not in dictionary[1]:
            return_value  = False
        
    return return_value
        
print(check_valid("pla00", check_list))

# check_key_valid(operation, check_list)