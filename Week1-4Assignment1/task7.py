your_variable_name = ["abcdefghijklm", "nopqrstuvwxyz"]


string = str(input("Enter a string to type: "))
# signal for stopping the loop should base on the count on the key
# stop_signal = len(string)
operation = ""


def goes_to_the_key(input_key, operation):
    # Everytime it press the key, stop_signal -=1
    operation += 'p'
    return operation

def search_key(input_key, dictionary):
    return_value = 
    #check if it is of the first line
    for items in input_key:
        if items in dictionary[0]:
        #check position of the key in the line
            return dictionary[0][items]
        elif input_key in dictionary[1]:
        


def check_valid(input_key, dictionary):
    return_value = True
    for item in input_key:
        if item not in dictionary[0] and item not in dictionary[1]:
            return_value = False
    return return_value





# main programm
if check_valid(string, your_variable_name) == False:
    # invalid key
    print("The string cannot be typed out.")

else:
    # the key is valid
    while len(string) > 0:
        current_key = string[0]
        new_key = string[1]
        current_location = search_key(current_key)
        new_key_location = search_key(new_key)

        operation += goes_to_the_key(current_key_location, new_key_location)
        # remove the first character of string
        string = string[1:]
        
    

print("The robot must perform the following operations:\n"+ operation)