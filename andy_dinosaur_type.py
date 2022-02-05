class DinosaurType:

    def __init__(self, dino_type):
        self.dino_type = dino_type
    
    # repr
    def __repr__(self):
        return "The Dinosaur Type is : " + self.dino_type
        
    # getter
    def get_type(self, type):
        return self.dino_type

    # setter
    def set_type(self, new_type):
        self.set_type = new_type

    # future methods