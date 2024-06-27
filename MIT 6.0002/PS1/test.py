k ={'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 'Moo Moo': 3, 'Milkshake': 2, 'Millie': 5, 'Lola': 2, 'Florence': 2, 'Henrietta': 9}
sorted= sorted(k.items(), key=lambda items:items[1], reverse=True)

total_list = []
def transport(item_list, limit, trip_count, total_list):
        sum_result = 0
        
        i = 0
        transport_list = []
        while i < len(item_list):
        # Add item value if it doesn't exceed the limit
            if sum_result + item_list[i][1] <= limit:
                sum_result += item_list[i][1]
                
                # add it to the list
                transport_list.append(item_list[i])
                item_list.pop(i)
            else:
                i += 1
        # while loop ends


        # add the transport_list to the total_list
        total_list.append(transport_list)
    
        if len(item_list) > 0:
            # still cows remaining
            trip_count += 1
            print("transported cows:", transport_list)
            print("Trip:", trip_count)
                
            return transport(item_list, limit, trip_count, total_list)
        if len(item_list) <= 0:
            # all transportation done
            print(" all transportation done")
            print(" total list: ", total_list)


transport(sorted, limit=10, trip_count=0, total_list=total_list)
