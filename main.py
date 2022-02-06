from andy_dino_zoo import Zoo
from andy_dinosaur import Dinosaur
from andy_player import Player
from andy_dinosaur_type import DinosaurType
from location_dictionary import location_dictionary




#Test block

# create player
jeff = Player("Jeff", Zoo())

# create zoo
new_zoo = Zoo()

# create a dinosaur
T_Rex = Dinosaur("Tyranosaurus", "", DinosaurType("Mountain"), "Carnivore" )
Richies_T_Rex = Dinosaur("Tyranosaurus", "Rich",DinosaurType("Mountain"), "Carnivore" )

# Change the name of our T-Rex
T_Rex.custom_name = "T-Bone"

#print(repr(T_Rex))
#print(repr(Richies_T_Rex))
# add a dinosaur to the players team

# view player
jeff.add_dino(T_Rex)
jeff.add_dino(Richies_T_Rex)
print(repr(jeff))


