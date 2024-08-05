your_variable_name = ["abcdefghijklm", "nopqrstuvwxyz"]
your_variable_name_1 = ["789","456","123","0.-"]
your_variable_name_2 = [ "chunk", "vibex", "gymps", "fjord", "waltz"]
your_variable_name_3 = [ "bemix", "vozhd", "grypt", "clunk", "waqfs"]
all_list = your_variable_name + your_variable_name_1 + your_variable_name_2 + your_variable_name_3



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
    for lines in dictionary:
        #check if it is of the first line
        if the_key in lines:
            the_key_location_ver = dictionary.index(lines)
            # this will turn the key location into 0.1, 0.2 or something like that
            the_key_location_hor =  (lines.index(the_key))
    return the_key_location_ver, the_key_location_hor
        


def check_valid(input_key, dictionary):
    return_value = False
    for dics in dictionary:
        if any( all(key in dics) for key in input_key):
            return return_value





# main programm
def main_programm(string,operation, start_location_ver,start_location_hor,your_variable_name):
    while len(string) > 0:
        current_key = string[0]
        destination_ver, destination_hor = search_key(current_key, your_variable_name)

        operation += goes_to_the_key(start_location_ver, start_location_hor, destination_ver, destination_hor)
        # update start location
        start_location_ver = destination_ver
        start_location_hor = destination_hor
        # remove the first character of string
        string = string[1:]
        
    return operation



if check_valid(string, all_list) == False:
    # invalid key
    print("The string cannot be typed out.")    
else:
    moves_0 = main_programm(string,operation, start_location_ver,start_location_hor,your_variable_name)
    moves_1 = main_programm(string,operation, start_location_ver,start_location_hor,your_variable_name_1)
    moves_2 = main_programm(string,operation, start_location_ver,start_location_hor,your_variable_name_2)
    moves_3 = main_programm(string,operation, start_location_ver,start_location_hor,your_variable_name_3)
# choose = min(len(moves_0),len(moves_1),len(moves_2),len(moves_3))


print(moves_0,"\n",moves_1,"\n",moves_3)
