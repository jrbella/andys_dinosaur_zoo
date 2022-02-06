from combat_stats import CombatStats
from andy_dinosaur_type import DinosaurType


class Dinosaur:

    def __init__(self, scientific_name, custom_name, dino_type, classification, combat_stats = CombatStats(0, 0, 0)):
        self.scientific_name = scientific_name
        self.dino_type = dino_type
        self.classification = classification

        # set a default name
        if custom_name == "":
            self.custom_name = scientific_name
        else:
            self.custom_name = custom_name

        # Dinosaurs get initialized with 0 stats
        # Dinosaurs get updated from a dictionary depending on
        # The dinosaur dictionary
        self.combat_stats = combat_stats
    

    # getters

    def get_scientific_name(self):
        return self.scientific_name
    
    def get_custom_name(self):
        return self.custom_name 
    
    def get_dino_type(self):
        return self.dino_type.get_type()
    
    def get_classification(self):
        return self.classification
    
    def get_combat_stats(self):
        return self.combat_stats
    
    # setters
    def set_scientific_name(self, name):
        self.set_scientific_name = name
    
    def set_custom_name(self, name):
        self.custom_name = name
    
    def set_dino_type(self, type):
        self.dino_type = type
    
    def set_classificaiton(self, classification):
        self.classification = classification
    
    # view
    def __repr__(self):
        return ("The scientific_name : " + self.scientific_name
        + "\n custom_name : " + self.custom_name
        + "\n type : " + self.get_dino_type() 
        + "\n classification : " + self.classification)