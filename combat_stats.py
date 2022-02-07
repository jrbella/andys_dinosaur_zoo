class CombatStats:
    #instanced variable
    max_health = 0

    def __init__(self, attack_number, defense_number, health_number):
        self.attack_number = attack_number
        self.defense_number = defense_number
        self.health_number = health_number
        self.max_health = health_number

    
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

    # repr
    def __repr__(self) -> str:
        output = "Attack Number: " + str(self.attack_number) + "\n Defense Number : " + str(self.defense_number ) + "\n Health Number : " + str(self.health_number)
        return output
    
    # set the max health
    def set_max_health(self):
        self.health_number = self.max_health