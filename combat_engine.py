from andy_dinosaur import Dinosaur
import random

# Combat Engine

# Combat Phase

def combat_phase_trigger(attacking_dinosaur, defending_dinosaur):
    attack =  attacking_dinosaur.combat_stats.get_attack()
    defense = defending_dinosaur.combat_stats.get_defense() 
    attack_total = float(combat_roll_trigger(attack) + attack) * (check_combat_modifiers(attacking_dinosaur.get_type()))
    defense_total = float(combat_roll_trigger(defense) + defense)
    combat_result = attack_total - defense_total

    if combat_result > 0:
        # combat suceeded
        print("Attack was successful")
        return defending_dinosaur.combat_stats.set_health(combat_result) 
        
    else:
        # combat failed
        print("Attack has failed")
        return defending_dinosaur.combat_stats.get_health()


# Modifiers
# Each type is going to segmented out for combat balance.
# Floats equate to percentages

def check_combat_modifiers(attack_dino_type, defense_dino_type):
    if attack_dino_type == "Mountain" and defense_dino_type == "Grassland":
        # returns a multiplier as a float
        return float(1.5)
    elif attack_dino_type == "Grassland" and defense_dino_type == "Marine":
                # returns a multiplier as a float
        return float(1.5)
    elif attack_dino_type == "Marine" and defense_dino_type == "Mountain":
        return float(1.5)
    else:
        return 1

def combat_roll_trigger(combat_number):

    dice_roll = random.randint(1,6)
    return (dice_roll + combat_number)

