k ={'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 'Moo Moo': 3, 'Milkshake': 2, 'Millie': 5, 'Lola': 2, 'Florence': 2, 'Henrietta': 9}
def organize_cow_trips(cow_weights, max_trip_weight):
    # Sort the cows by weight in descending order
    sorted_cows = sorted(cow_weights.items(), key=lambda item: item[1], reverse=True)
    trips = []
    
    # Function to pack cows into a ship for one trip
    def pack_cows_for_trip(cows, max_weight):
        trip_weight = 0
        trip_cows = []
        remaining_cows = []
        
        for cow, weight in cows:
            if trip_weight + weight <= max_weight:
                trip_cows.append(cow)
                trip_weight += weight
            else:
                remaining_cows.append((cow, weight))
        
        return trip_cows, remaining_cows

    remaining_cows = sorted_cows
    
    # Organize cows into trips
    while remaining_cows:
        trip_cows, remaining_cows = pack_cows_for_trip(remaining_cows, max_trip_weight)
        trips.append(trip_cows)
    
    # Display the result of each trip
    for i, trip in enumerate(trips, 1):
        trip_weight = sum(cow_weights[cow] for cow in trip)
        print(f"Trip {i}: {trip}, Total weight: {trip_weight} kg")

# Example usage
cow_weights = {
    'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 'Moo Moo': 3,
    'Milkshake': 2, 'Millie': 5, 'Lola': 2, 'Florence': 2, 'Henrietta': 9
}
max_trip_weight = 10
organize_cow_trips(cow_weights, max_trip_weight)