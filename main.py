from andy_dino_zoo import Zoo
from andy_dinosaur import Dinosaur
from andy_player import Player
from andy_dinosaur_type import DinosaurType
from location_dictionary import location_dictionary
from combat_engine import *
from dinosaur_dictionary import *
from dinosaur_capture_engine import *




#Test block

# create player
jeff = Player("Jeff", Zoo())

# create zoo
new_zoo = Zoo()


# create a dinosaur
Richies_T_Rex = Dinosaur("",dinosaurs['tyrannosaurus']['scientific_name'], 
dinosaurs['tyrannosaurus']['classification'], dinosaurs['tyrannosaurus']['dino_type'] )
T_Rex = Dinosaur("",dinosaurs['tyrannosaurus']['scientific_name'], 
dinosaurs['tyrannosaurus']['classification'], dinosaurs['tyrannosaurus']['dino_type'] )

# Change the name of our T-Rex
Richies_T_Rex.custom_name = "T-Bone"


# set the attack and defense
T_Rex.set_combat_stats(
    dinosaurs['tyrannosaurus']['combat_stats']['attack'],
    dinosaurs['tyrannosaurus']['combat_stats']['defense'],
    dinosaurs['tyrannosaurus']['combat_stats']['health']
)

Richies_T_Rex.set_combat_stats(
    dinosaurs['tyrannosaurus']['combat_stats']['attack'],
    dinosaurs['tyrannosaurus']['combat_stats']['defense'],
    dinosaurs['tyrannosaurus']['combat_stats']['health']
)

# add a dinosaur to the players team

# view player
jeff.add_dino(T_Rex)
jeff.add_dino(Richies_T_Rex)



# Test combat engine
attacking_test = jeff.dino_team[0]
defending_test = jeff.dino_team[1]



# run combat engine

combat_turn_trigger(attacking_test, defending_test)
capture_trigger(jeff, defending_test)
combat_turn_trigger(attacking_test, defending_test)
capture_trigger(jeff, defending_test)
combat_turn_trigger(attacking_test, defending_test)
capture_trigger(jeff, defending_test)



