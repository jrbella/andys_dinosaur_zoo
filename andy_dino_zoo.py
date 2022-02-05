class Zoo:

    name = "Dino Zoo"
    dinosaur_habitat = {}


    def __repr__(self):
        print("The Zoo name is " + str(self.name))
        
        for habitats in self.dinosaur_habitat.keys():
            print("A habitat for :  " + habitats + " has been created")

    def set_name(self, custom_name):
        self.name = custom_name

    def add_dinosaur_habitat(self, habitat_name):
        self.dinosaur_habitat[habitat_name] = []