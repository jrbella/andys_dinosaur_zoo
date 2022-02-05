class Player:

    def __init__(self, name, dino_team, zoo):
        self.name = name
        self.dino_team = []
        self.zoo = zoo

    # getters

    def get_name(self):
        return self.name
    
    def get_dino_team(self):
        return self.dino_team
    
    def get_zoo(self):
        return self.zoo
    
    # setters
    
    def set_name(self, name):
        self.name = name


    # add dino to team

    def add_dino(self, dinosaur):
        if self.dino_team < 4:
            self.dino_team.append(dinosaur)
        else:
            print("could not add dinosaur because the team is full")
            # placeholder value
            return False
    