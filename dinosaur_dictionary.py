dinosaurs = {}

def print_dino_dictionary(dinosaurs):
    print(dinosaurs)

def create_dinosaur_dictionary(name, scientific_name, classification, dino_type, combat_stats):
        # combat stats should be an array...for now?
        temp_name = {
            name : {
                'scientific_name' : scientific_name,
                'classification' : classification,
                'dino_type' : dino_type,
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
    ["tyrannosaurus", "Tyrannosaurus", "Carnivore", "Mountain", [3, 2, 50]],
    ["stegosaurus", "Stegosaurus", "Herbivore", "Grassland", [2, 2, 60]],
    ["triceratops", "Triceratops", "Herbivore", "Grassland", [2, 2, 60]],
    ["spinasaurus", "Spinasaurus", "Carnivore", "Marine", [2, 3, 50]],
    ["velociraptor", "Velociratpor", "Carnivore", "Mountain", [3, 2, 50]],
    ["carnitaurus", "Carnitaurus", "Carnivore", "Grassland", [2, 2, 60]]
]

for dino in dino_list:
    dinosaurs.update(create_dinosaur_dictionary(dino[0], dino[1], dino[2], dino[3], dino[4]))
    
# execution
print_dino_dictionary(dinosaurs)
