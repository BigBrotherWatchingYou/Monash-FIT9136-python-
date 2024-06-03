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
    

    # build a loop that calculate
    
    trip_count = []

    def transport(cows, limit):
        trip_capacity = 0
        remained_cows = []
        trip_cows = []
        for cow,weight in cows:
            if trip_capacity + weight <= limit:
                trip_capacity += weight
                trip_cows.append((cow,weight))
            else:    
                remained_cows.append((cow,weight))
    
        return trip_cows,remained_cows

    remained_cows = cows_sorted
    i=0
    while remained_cows:
        trip_cows, remained_cows = transport(remained_cows,limit =10)
        trip_count.append(trip_cows)
        i +=1
        print((i,trip_cows))
    
k ={'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 'Moo Moo': 3, 'Milkshake': 2, 'Millie': 5, 'Lola': 2, 'Florence': 2, 'Henrietta': 9}
greedy_cow_transport(k, limit = 10)