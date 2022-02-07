from combat_stats import CombatStats
from andy_dinosaur_type import DinosaurType


class Dinosaur:


    def __init__(self, custom_name, scientific_name, classification, dino_type, combat_stats = CombatStats(0,0,0)):
       
        self.custom_name = custom_name
        self.scientific_name = scientific_name
        self.classification = classification
        self.dino_type = dino_type
        self.combat_stats = combat_stats
        # set a default name
        if self.custom_name == "":
            self.custom_name = self.get_scientific_name()


        # Dinosaurs get initialized with 0 stats
        # Dinosaurs get updated from a dictionary depending on
        # The dinosaur dictionary
    

    # getters

    def get_scientific_name(self):
        return self.scientific_name
    
    def get_custom_name(self):
        return self.custom_name 
    
    def get_dino_type(self):
        return self.dino_type
    
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
    
    def set_combat_stats(self, attack, defense, health):
        self.combat_stats.set_attack_number(attack)
        self.combat_stats.set_defense_number(defense)
        self.combat_stats.set_health_number(health)
        print("health : " + str(health) 
                + "\nattack : " + str(attack)
                + "\ndefense : " + str(defense))
    
    # view
    def __repr__(self):
        output =  "\n\nDinosaur " + self.get_scientific_name() + "\n============\ncustom name : " + self.get_custom_name() + "\nclassification : " + self.get_classification() + "\ndino_type : " + self.get_dino_type() + "\ncombat_stats : " + repr(self.get_combat_stats())
        return output