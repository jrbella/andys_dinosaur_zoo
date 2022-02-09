from andy_player import Player
from andy_dinosaur import Dinosaur

class Location:

    def __init__(self, location_continent = "Home", location_region = "Home"):
        
        self.location_continent = location_continent
        self.location_region = location_region

        # getter

        def get_location_continent(self):
            return self.location_continent

        def get_location_region(self):
            return self.location_region
        
        # setter
        def set_location_continent(self, new_continent):
            self.location_continent = new_continent
        
        def set_location_region(self, new_region):
            self.location_region = new_region
        

        # custom game methods

        # input is player.dino_team
        def return_home(self, dino_team):
            self.location_continent = "Home"
            self.location_Region = "Home"
            
            # dinosaur.combat_stats, this heals the dino team
            for dino in dino_team:
                dino.set_max_health()
