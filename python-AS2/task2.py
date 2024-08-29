class Rabbit:
    # This class represents a Rabbit with a name and an age.
    def __init__(self, name):
        # Initialize the Rabbit with a name and set the age to "Unknown".
        self.name = name
        self.age = "Unknown"
        # parent
        self.parent = []
        # kitten
        self.kitten = []

class Validation:
    # This class provides static methods for validating input data.

    
    def rabbit_exists(name, rabbits):
        # Check if the provided rabbit name exists within the rabbits dictionary.
        # returns True if rabbit exists, False otherwise.
        return name in rabbits

    
    def is_valid_age(age):
        # Check if the provided age is a valid integer.
        # return True is valid age
        if age.isdigit():
            return True
        return False

class RabbitManager:
    # This class manages the operations related to Rabbits, including creating,
    # updating, and listing Rabbits.

    def __init__(self):
        # Initialize the RabbitManager with an empty dictionary to store rabbits.
        self.rabbits = {}

    def main_menu(self):
        # Display the main menu and handle user choices.
        while True:
            print("==================================")
            print("Enter your choice:")
            print("1. Create a Rabbit.")
            print("2. Input Age of a Rabbit.")
            print("3. List Rabbytes.")
            print("4. Create a Parental Relationship.")
            print("5. List Direct Family of a Rabbit.")
            print("0. Quit.")
            print("==================================")
            
            choice = input().strip()

            if choice == "1":
                # Call the method to create a rabbit.
                self.create_rabbit()
            elif choice == "2":
                # Call the method to input or update the age of a rabbit.
                self.input_rabbit_age()
            elif choice == "3":
                # Call the method to list all rabbits.
                self.list_rabbytes()

            elif choice == "4":
                # create a parental relationship
                self.create_parental_relationship()
            elif choice == "5":
                # list direct family of a rabbit
                self.list_family()
            elif choice == "0":
                # Exit the program.
                break
            else:
                # If the input is invalid, prompt the user to try again.
                print("Invalid choice, please try again.")

    def create_rabbit(self):
        # Handle the creation of a new rabbit with a unique name.
        while True:
            print("Input the new rabbit's name:")
            rabbit_name = input().strip()
            
            if not Validation.rabbit_exists(rabbit_name, self.rabbits):
                # If the name is unique (doesn't exist), create a new Rabbit object and add it to the dictionary.
                self.rabbits[rabbit_name] = Rabbit(rabbit_name)
                break
            else:
                # If the name already exists, inform the user.
                print("That name is already in the database.")

    def create_parental_relationship(self):
        
        # get the user input
        print("Input the parent's name:")# input parent name
        parent_name = input().strip()

        print("Input the kitten's name:")# input kitten name
        kitten_name = input().strip()

        # check if the[parent] rabbit exists
        if not Validation.rabbit_exists(parent_name, self.rabbits):
            # if the [parent] name does not exist, create a new Rabbit
            self.rabbits[parent_name] = Rabbit(parent_name)
        
        # check if the [kitten] rabbit exists
        if not Validation.rabbit_exists(kitten_name, self.rabbits):
            # if the [kitten] name does not exist, create a new Rabbit
            self.rabbits[kitten_name] = Rabbit(kitten_name)

        # create relationship            
        self.rabbits[kitten_name].parent.append(str(parent_name))# add the rabbit a [parent]
        
        self.rabbits[parent_name].kitten.append(str(kitten_name))# add the rabbit a [kitten]
                

    def input_rabbit_age(self):
        # Handle the input or update of a rabbit's age.
        while True:
            print("Input the rabbit's name:")
            rabbit_name = input().strip()
            
            if Validation.rabbit_exists(rabbit_name, self.rabbits):
                # If the rabbit exists, prompt for its age.
                print(f"Input {rabbit_name}'s age:")
                rabbit_age = input().strip()
                if Validation.is_valid_age(rabbit_age):
                    # If the age is valid, update the rabbit's age.
                    self.rabbits[rabbit_name].age = int(rabbit_age)
                    break
                else:
                    # If the age is not valid, inform the user.
                    print("Please enter a valid integer for the age.")
            else:
                # If the rabbit does not exist, inform the user.
                print("That name is not in the database.")

    def list_rabbytes(self):
        # Display the list of all rabbits with their names and ages.
        print("Rabbytes:")
        for rabbit in self.rabbits.values():
            # Print each rabbit's name and age.
            print(f"{rabbit.name} ({rabbit.age})")

    def list_family(self):
        #  list the family members/relationship
        print("Input the rabbit's name:")
        name = input().strip()
        #check if the rabbit exist
        if Validation.rabbit_exists(name, self.rabbits):
            rabbit = self.rabbits[name]
            # print the Relationship
            print(f"Parents of {name}:")# parent
            if rabbit.parent:# there might be multiple parent
                for parent_name in sorted(rabbit.parent):# sorted is for the result (the result need to be printed in order)
                    print(parent_name)
            
            print(f"Kittens of {rabbit.name}:")
            if rabbit.kitten:# there might be multiple kitten
                for kitten_name in sorted(rabbit.kitten):# sorted is for the result (the result need to be printed in order)
                    print(kitten_name)
    
    

manager = RabbitManager()
manager.main_menu()