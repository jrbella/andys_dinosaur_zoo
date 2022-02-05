class CombatStats:

    def __init__(self, attack_number, defense_number, health_number):
        self.attack_number = attack_number
        self.defense_number = defense_number
        self.health_number = health_number
    
    # setters
    def set_attack_number(self, number):
        self.attack_number = number
    
    def set_defense_number(self, number):
        self.defense_number = number
    
    def set_health_number(self, number):
        self.health_number = number
    
    # getters
    def get_attack_number(self):
        return self.attack_number
    
    def get_defense_number(self):
        return self.defense_number
        
    def get_health_number(self):
        return self.health_number