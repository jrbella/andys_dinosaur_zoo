class Zoo:

    name = "Dino Zoo"
    dinosaur_habitat = {}


    def __repr__(self):

        print("The Zoo name is " + str(self.name))
        for habitat in self.dinosaur_habitat.keys():
            print("A habitat for :  " + habitat + " has been created")

    # setters
    def set_name(self, custom_name):
        self.name = custom_name

    # add habitat
    def add_dinosaur_habitat(self, habitat_name):
        self.dinosaur_habitat[habitat_name] = []

    # getters
    def get_dinosaur_habitats(self):
        return self.dinosaur_habitat
    
    def get_name(self):
        return self.name