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
    # function of the movement, of each number, returns the behaviour that the robots perform
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
    # search the location of the key, returns the horizontal and vertical location in integers
    
    #check if it is of the first line of list
    for dics in dictionary:
        if the_key in dics:
            the_key_location_ver = dics.index(the_key)
            the_key_location_hor = dictionary.index(dics)
 



    return the_key_location_ver, the_key_location_hor
        


def check_valid(input_key, dictionary):
    # before the programm starts, check if the key is valid
    return_value = True
    dictionary = ''.join(dictionary)
    for item in input_key:
        if item not in dictionary:
            return_value = False

    return return_value





def main_programm(string, configuration):
    # main programm
    if check_valid(string, configuration) == False:
        # invalid key
        print("The string cannot be typed out.")
    
    # valid key
    else:
        # initialize
        operation = ''
        start_location_ver = 0
        start_location_hor = 0
        # the key is valid
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




def combination(dictionary):
    min = 100000000
    key_num = 9999
    for values in dictionary:
        length = len(dictionary[values])
        if length < min: 
            min = length
            result = dictionary[values]
            key_num = values
            
    return key_num, result

dict = {}
for i in range(4):
    if check_valid(string, configuration[i]) == True:
        #print(i)
        dict[str(i)] = str(main_programm(string, configuration[i]))


key_num, result = combination(dict)
print("Configuration used:")
print((len(configuration[int(key_num)])+4)*"-")
for item in configuration[int(key_num)]:
    print("|", item,"|")
print((len(configuration[int(key_num)])+4)*"-")
print("The robot must perform the following operations:\n", result)




