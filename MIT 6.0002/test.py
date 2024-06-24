k ={'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 'Moo Moo': 3, 'Milkshake': 2, 'Millie': 5, 'Lola': 2, 'Florence': 2, 'Henrietta': 9}
sorted= sorted(k.items(), key=lambda items:items[1], reverse=True)
''''def transport_recursion(cow_input, limit,count=0):
        if len(cow) <= 0:
            return count
        else:
            # write the while loop here
            for cows, weight in cow_input:
                while weight[1]
            count += 1
            return transport_recursion(cow_input, limit,count=0)
    '''
# transport_recursion(sorted, limit=10, count=0)
#print(sorted)

# this function is for recursion, it delete the cow when it is able to be transport
# everytime when it runs it will try its best to transport, everytime it runs will only deal with one transportation, 
# so need to write a recursion and record everytime it successfully transport
def transport(item_list, limit, trip_count):
    sum_result = 0
    cow_number = 0
    i = 0
    
    while i < len(item_list):
        # Add item value if it doesn't exceed the limit
        if sum_result + item_list[i][1] <= limit:
            sum_result += item_list[i][1]
            cow_number += 1
            item_list.pop(i)
        else:
            i += 1 
        


        
