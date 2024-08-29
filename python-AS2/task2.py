    def create_parental_relationship(self):
        while True:
            # get the user input
            print("Input the new parent's name:")# input parent name
            parent_name = input().strip()

            print("Input the new kitten's name:")# input kitten name
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
            self.rabbits[kitten_name].parent = str(parent_name)# add the rabbit a [parent]
            
            self.rabbits[parent_name].kitten = str(kitten_name)# add the rabbit a [kitten]
                
                
def list_family(self):
    
    print("Input the rabbit's name:")
    rabbit_name = input().strip
    #check if the rabbit exist
    if Validation.rabbit_exists(rabbit_name, self.rabbits):# rabbit exists
        # print the Relationship
        print(f"Parents of {rabbit_name}:")# parent
        print(f"{rabbit.parent})

        print(f"Kittens of {rabbit_name}:")# kitten
        print(f"{rabbit.kitten})
    

