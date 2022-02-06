


dinosaurs = {}

def create_dinosaur_dictionary(name, scientific_name, classification, type):
    temp_name = name
    temp_name = {
        name : {
            'scientific_name' : scientific_name,
            'classification' : classification,
            'type' : type
        }
    }
    return temp_name



dino_list = [
    ["tyrannosaurus", "Tyrannosaurus", "Carnivore", "Mountain"],
    ["stegosaurus", "Stegosaurus", "Herbivore", "Grassland"],
    ["triceratops", "Triceratops", "Herbivore", "Grassland"],
    ["spinasaurus", "Spinasaurus", "Carnivore", "Marine"],
    ["velociraptor", "Velociratpor", "Carnivore", "Mountain"],
    ["carnitaurus", "Carnitaurus", "Carnivore", "Grassland"]
]

for dino in dino_list:
    dinosaurs.update(create_dinosaur_dictionary(dino[0], dino[1], dino[2], dino[3]))

print(dinosaurs)