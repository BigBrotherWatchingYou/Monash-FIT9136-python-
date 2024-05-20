import os
cow_names = []
cow_number = []
try:
    with open("MIT 6.0002/ps1_cow_data_2.txt", 'r') as file:
        for k in file.readlines():
            cow_names.append(k.strip().split(',')[0])
            cow_number.append(k.strip().split(',')[1])
            
except FileNotFoundError:
    print("file not findyet")
    
print(cow_names)
print(cow_number)
# watch youtube 6.0002 video learn algorithm00