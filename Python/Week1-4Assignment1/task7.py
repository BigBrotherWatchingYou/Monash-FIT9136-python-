your_variable_name = ["abcdefghijklm", "nopqrstuvwxyz"]


string = str(input("Enter a string to type: "))
# signal for stopping the loop should base on the count on the key
# stop_signal = len(string)
operation = ""
# starts from the beginning
start_location_ver = 0
start_location_hor = 0

def goes_to_the_key(start_ver,start_hor, end_ver, end_hor):
    # no action if start==end
    movement = ""
    vertical_move = int(start_ver - end_ver)
    #print("start", start_ver,".",start_hor)
    #print("end",end_ver,".",end_hor)
    horizontal_move = int(start_hor - end_hor)
    #print("horizontal_move",horizontal_move)
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
    #print("movement",movement)
    #print("-----------------")
    return movement

def search_key(the_key, dictionary):
    
    
    #check if it is of the first line
    if the_key in dictionary[0]:
        the_key_location_ver = 0
        # this will turn the key location into 0.1, 0.2 or something like that
        the_key_location_hor =  (dictionary[0].index(the_key))

    elif the_key in dictionary[1]:
        the_key_location_ver = 1
        the_key_location_hor =  (dictionary[1].index(the_key)) 
 



    return the_key_location_ver, the_key_location_hor
        


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
        destination_ver, destination_hor = search_key(current_key, your_variable_name)

        operation += goes_to_the_key(start_location_ver, start_location_hor, destination_ver, destination_hor)
        # update start location
        start_location_ver = destination_ver
        start_location_hor = destination_hor
        # remove the first character of string
        string = string[1:]
        
    

    print("The robot must perform the following operations:\n"+ operation)