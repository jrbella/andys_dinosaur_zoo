from andy_dinosaur_type import DinosaurType


class Dinosaur:


    def __init__(self, custom_name, scientific_name, classification, dino_type, attack = 0, defense = 0, health = 0):
       
        self.custom_name = custom_name
        self.scientific_name = scientific_name
        self.classification = classification
        self.dino_type = dino_type
        self.attack = attack
        self.defense = defense
        self.health = health
        self.max_health = self.health
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
    
    def get_attack(self):
        return self.attack
    
    def get_defense(self):
        return self.defense
    
    def get_health(self):
        return self.health
    
    def get_combat_stats(self):
        combat_output = {
            "attack" : self.attack,
            "defense" : self.defense,
            "health" : self.health
        }
        return combat_output
    
    
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
        self.attack = attack
        self.defense = defense
        self.health = health
        print("Combat stats updated:\n" + "attack : " 
        + str(self.get_attack()) + "\ndefense : " 
        + str(self.get_defense()) + "\nhealth : " 
        + str(self.get_health()))

    def set_attack(self, attack):
        self.attack = attack

    def set_defense(self, defense):
        self.defense = defense
    
    def set_health(self, health):
        self.health = health
    # view
    def __repr__(self):
        output =  "\n\nDinosaur " + self.get_scientific_name() + "\n============\ncustom name : " + self.get_custom_name() + "\nclassification : " + self.get_classification() + "\ndino_type : " + self.get_dino_type() + "\ncombat_stats : " + repr(self.get_combat_stats())
        return output