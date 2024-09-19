'''
 a program that, on top of the previous options, 
 offers to rename variables.
a program that allows a user 
to list the variables of a Python program. 
We suppose that each variable follows one of three cases:
'''
import keyword

program = []
variables = set()
# default setting

def main_menu():
    print("==================================")
    print("Enter your choice:")
    print("1. Print program.")
    print("2. List.")
    print("0. Quit.")
    print("==================================")
    choice = input().strip()
    if choice == "1":
        print_program()
    if choice == "2":
        list_variables()
    '''elif choice == "3":
        format_variable()
    elif choice == "4":
        rename_variable()
    '''
    if choice == "0":
        quit()
    #else:
        #print("Invalid choice, please try again.")
    return main_menu()



def get_user_input():
    print("Enter the Python program to analyze, line by line. Enter 'end' to finish.")
    while True:
        line = input()
        
        if line.lower() == "end":
            break
        program.append(line)
    get_variables(program)




def list_variables():
    print("Variables:")
    for items in variables:
        print(items)

def rename_variable():
    pass

def print_program():
    print("Program:")
    for items in program:
        print(items)

def get_variables(data):
    # cut the program into slices , split with space
    for items in data:
        items = items.strip().split(" ")
        # check each item in the program
        for item in items:   
            # check and remove the keywords
            if item in keyword.kwlist:
                continue    
            if item.replace("_","").isalpha():
                variables.add(item)

    




def to_snake_case():
    pass

if __name__ == "__main__":
    #main_menu()
    get_user_input()

    variables = sorted(variables)
    main_menu()
    



