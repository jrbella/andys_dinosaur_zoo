from andy_dinosaur import Dinosaur

class Player:

    def __init__(self, name, zoo, dino_team = [],  location = "Home"):
        self.name = name
        self.dino_team = dino_team
        self.zoo = zoo
        self.location = location

    def __repr__(self):
        return("player_name : " + self.name 
        + "\nplayer_zoo : " + self.zoo.name
        + "\nplayer_location : " + self.location
        + "\nplayer_dino_team : " + str([dino.get_custom_name() for dino in self.dino_team ]))

  
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
        if len(self.dino_team) < 4:
            self.dino_team.append(dinosaur)
        else:
            print("could not add dinosaur because the team is full")
            # placeholder value
            return "Failed to add the dinosaur to the team because the team is full"
    