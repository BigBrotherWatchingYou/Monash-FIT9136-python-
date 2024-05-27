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
    
    return cows_dict

print(load_cows("MIT 6.0002/ps1_cow_data.txt"))