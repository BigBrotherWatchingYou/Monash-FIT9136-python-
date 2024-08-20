class Post:
    """ Post class for representing and manipulating posts. """

    caption = "" # Class Variable.

    # Constructor (with parameters).
    def __init__(self, image): 
        """ Create a new post. """
        self.image = image
        self.caption = self.caption

    # Methods
    def get_caption(self):
        return self.caption

    def get_image(self):
        return self.image

    def set_caption(self, caption):
        self.caption = caption

    def set_image(self, image):
        self.image = image

    # Overrides the __str__ method.
    # Return a string representation of the instance in a human-readable format
    def __str__(self): 
        return "Image directory = {}, Caption = {}".format(self.image, self.caption)

funny_meme = Post("funny_image.jpg") # Instantiation of a new Post object.
print(funny_meme)
# Prints: 'Image directory = funny_image.jpg, Caption = '

spicy_meme = Post("spicy_image.jpg") # Instantiation of another new Post object.
print(spicy_meme)
# Prints: 'Image directory = spicy_image.jpg, Caption = '

spicy_meme.set_caption("FIT9136? More like MEME9136 XD?!1") # Calling the method (i.e., set_caption) to have the instance variable (i.e., caption) refer to a new string.

print("The new caption is: " + spicy_meme.get_caption()) # Using the method (i.e., get_caption) to have access to the value of the instance variable (i.e., caption).
# Prints 'The new caption is: FIT9136? More like MEME9136 XD?!1'