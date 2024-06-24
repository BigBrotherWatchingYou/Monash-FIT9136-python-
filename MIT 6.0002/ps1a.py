###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here

    cows_dict = {}
    try:
        with open(str(filename), 'r') as file:
            for line in file.readlines():
                cow_name = (line.split(','))[0]
                cow_weight = (line.split(','))[1]
                cows_dict[cow_name] = int(cow_weight)
                
    except FileNotFoundError:
        print("file not find")
    
    print('here are the cows:', cows_dict)
    return cows_dict
    
# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    
    # get cows sorted
    cows_sorted = sorted(cows.items(), key=lambda items : items[1], reverse=True)
    

    def transport(item_list, limit, trip_count):
        sum_result = 0
        cow_number = 0
        i = 0
        # this is a 2d list, it will be added to the total_list after recursion is done
        transport_list = []
        # a 3d list that contains all the transport_list result
        total_list = []
        while i < len(item_list):
        # Add item value if it doesn't exceed the limit
            if sum_result + item_list[i][1] <= limit:
                sum_result += item_list[i][1]
                cow_number += 1
                # add it to the list
                transport_list.append(item_list[i])
                item_list.pop(i)
            else:
                i += 1
        # while loop ends


        # add the transport_list to the total_list
        total_list.append(transport_list)
        # need to empty the transport_list after one trip is done
        transport_list = [] 
        
        
        if cow_number >= 1 :
        # check the cows after while loop
            if len(item_list) <= 0:
            # all cows transported, mission done
                print("all cows transported,total trip count = ", trip_count)
                print("total_list, the result")
                return total_list
            else:
                # still cows remaining
                print("Remaining list:", item_list)
                print("Trip:", trip_count)
                trip_count += 1
                return transport(item_list, limit, trip_count)
            
    transport(cows_sorted, limit, trip_count=0)

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    pass
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    trip_nums1 = greedy_cow_transport(cows, limit=10)
    trip_nums_2 = brute_force_cow_transport(cows, limit=10)
    print("this one got a higher efficiency:")
    if trip_nums1 > trip_nums_2:
        print("greedy algo")
    if trip_nums_2 > trip_nums1:
        print("brute algo")
    else:
        print("both have the same efficiency")


cows = load_cows("MIT 6.0002/ps1_cow_data.txt")
greedy_cow_transport(cows,limit=10)