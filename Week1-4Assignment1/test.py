configuration = [["abcdefghijklm", "nopqrstuvwxyz"],
["789","456","123","0.-"],
[ "chunk", "vibex", "gymps", "fjord", "waltz"],
[ "bemix", "vozhd", "grypt", "clunk", "waqfs"]]



string = str(input("Enter a string to type: "))
# signal for stopping the loop should base on the count on the key
# stop_signal = len(string)
operation = ""
# starts from the beginning
start_location_ver = 0
start_location_hor = 0

def goes_to_the_key(start_ver,start_hor, end_ver, end_hor):
    # function that returns the operation that the robot takes
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
    # Everytime it finished moving, it press the key
    movement += 'p'
    
    return movement

def search_key(current_key, dictionary):
    the_key_location_ver = 0
    the_key_location_hor = 0
    for lines in dictionary:
        #check if it is of the first line
        if current_key in lines:
            # this will turn the key location into numbers
            the_key_location_ver = dictionary.index(lines)
            
            the_key_location_hor = (lines.index(current_key))

    return the_key_location_ver, the_key_location_hor
        


# programm that print the operations that robot will print
def operate(string,  start_location_ver,start_location_hor,configuration):
    operation = ""
    while len(string) > 0:
        current_key = string[0]
        destination_ver, destination_hor = search_key(current_key, configuration)

        operation += goes_to_the_key(start_location_ver, start_location_hor, destination_ver, destination_hor)
        # update start location
        start_location_ver = destination_ver
        start_location_hor = destination_hor
        # remove the first character of string
        string = string[1:]
        
    return operation

def comparison(dic_of_all_operations):
    for strings in dic_of_all_operations:
        pass






def check_valid(string, configuration):
    # check if the input string is valid
    return_value = True
    for key in string:
        if key not in configuration:
            return_value = False

          
    return return_value


# main programm
'''if check_valid(string) == False:
    print("The string cannot be typed out.") 
else:
    # format: {configuration:"rrrrrrrplllll", configuration:"wefwefwe"}'''

'''for i in range(4):
    if check_valid(string, configuration[i]) == True:
        dic_of_all_operations[i] = operate(string,0,0,configuration[i])'''
dic_0 = []
dic_1 = []
dic_2 = []
dic_3 = []

if check_valid(string, configuration[0]) != False:
    dic_0 = operate(string,0,0,configuration[0])

if check_valid(string, configuration[1]) != False:
    dic_1 = operate(string,0,0,configuration[1])

if check_valid(string, configuration[2]) != False:
    dic_2 = operate(string,0,0,configuration[2])

if check_valid(string, configuration[3]) != False:
    dic_3 = operate(string,0,0,configuration[3])


print(dic_0,dic_1,dic_2,dic_3)
    # invaid string


