your_variable_name = ["abcdefghijklm", "nopqrstuvwxyz"]


string = str(input("Enter a string to type: "))
# signal for stopping the loop should base on the count on the key
# stop_signal = len(string)
operation = ""
# starts from the beginning
start_location = 0.00

def goes_to_the_key(start, end):
    # no action if start==end
    movement = ""
    vertical_move = int(start) - int(end)
    print("vertical_move", vertical_move)
    horizontal_move = ((start%1) - (end%1))*100
    # goes right
    if horizontal_move < 0:
        movement += int(-horizontal_move) * 'r'
        #goes left
    elif horizontal_move > 0:
        movement += int(horizontal_move) * 'l'
        
    # goes down
    if vertical_move < 0:
        movement += int(-vertical_move) * 'd'
        #goes up
    elif vertical_move > 0:
        movement += int(vertical_move) * 'u'

    
        

    # Everytime it press the key, stop_signal -=1
    movement += 'p'
    return movement

def search_key(the_key, dictionary):
    the_key_location = 0
    
    #check if it is of the first line
    if the_key in dictionary[0]:
        # this will turn the key location into 0.1, 0.2 or something like that
        the_key_location =  (dictionary[0].index(the_key)*0.01) + 0
    elif the_key in dictionary[1]:
        the_key_location =  (dictionary[1].index(the_key)*0.01) + 1
 



    return the_key_location
        


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
        destination = search_key(current_key, your_variable_name)

        operation += goes_to_the_key(start_location, destination)
        # update start location
        start_location = destination
        # remove the first character of string
        string = string[1:]
        
    

print("The robot must perform the following operations:\n"+ operation)