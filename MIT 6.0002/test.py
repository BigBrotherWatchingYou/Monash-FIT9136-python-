cow_names = []
try:
    with open("MIT 6.0002/ps1_cow_data_2.txt", 'r') as file:
        for data in file:
            cow_names.append(data.split()[0])
except FileNotFoundError:
    print("file not find")
    
print(cow_names)