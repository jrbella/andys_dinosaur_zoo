from andy_dino_zoo import Zoo
from andy_player import Player
from andy_location_dictionary import location_dictionary

new_zoo = Zoo()
new_zoo.add_dinosaur_habitat("T-Rex")



jeff = Player("Jeff", Zoo())

print(repr(jeff))

print(location_dictionary.values())