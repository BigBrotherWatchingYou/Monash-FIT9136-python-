import keyword
program = []
variables = set()
def get_user_input():
    print("Enter the Python program to analyze, line by line. Enter 'end' to finish.")
    while True:
        line = input()
        
        if line.lower() == "end":
            break
        program.append(line)
    get_variables(program)

def get_variables(data):
    # cut the program into slices , split with space
    print("-----------")
    print(data)
    print("--------")
    for items in data:
        items = items.strip().split(" ")
        print("test")
        print(items)
        # check each item in the program
        for item in items:   
            # check and remove the keywords
            print("current item:", item)
            if item in keyword.kwlist:
                continue    
            if item.replace("_","").isalpha():
                variables.add(item)
                print("added:--",item)
        
get_user_input()

print("Variables:")
print(variables)