dinosaurs = {}

def create_dinosaur_dictionary(name, scientific_name, classification, type, combat_stats):
        # combat stats should be an array...for now?
        temp_name = name
        temp_name = {
            name : {
                'scientific_name' : scientific_name,
                'classification' : classification,
                'type' : type,
                'combat_stats' : {
                    'attack' : combat_stats[0],
                    'defense' : combat_stats[1],
                    'health' : combat_stats[2]
                }
            }
        }
        return temp_name


# default combat list, mountain + 1 attack, grassland + 1 health, marine + 1 defense
dino_list = [
    ["tyrannosaurus", "Tyrannosaurus", "Carnivore", "Mountain", [3, 2, 5]],
    ["stegosaurus", "Stegosaurus", "Herbivore", "Grassland", [2, 2, 6]],
    ["triceratops", "Triceratops", "Herbivore", "Grassland", [2, 2, 6]],
    ["spinasaurus", "Spinasaurus", "Carnivore", "Marine", [2, 3, 5]],
    ["velociraptor", "Velociratpor", "Carnivore", "Mountain", [3, 2, 5]],
    ["carnitaurus", "Carnitaurus", "Carnivore", "Grassland", [2, 2, 6]]
]

for dino in dino_list:
    dinosaurs.update(create_dinosaur_dictionary(dino[0], dino[1], dino[2], dino[3], dino[4]))
    
print(dinosaurs)