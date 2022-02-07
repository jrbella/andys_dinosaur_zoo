from andy_dinosaur import Dinosaur
import random

# Combat Engine

# Combat Phase

def combat_phase_trigger(attacking_dinosaur, defending_dinosaur):
    attack =  attacking_dinosaur.combat_stats.get_attack_number()
    print("attack is : " + str(attack))
    defense = defending_dinosaur.combat_stats.get_defense_number() 
    print("defense is : " + str(defense))
    attack_total = float(combat_roll_trigger(attack) + attack) * (check_combat_modifiers(attacking_dinosaur.get_dino_type(), defending_dinosaur.get_dino_type()))
    print("attack_total : " + str(attack_total))
    defense_total = float(combat_roll_trigger(defense) + defense)
    print("defense_total : " + str(defense_total))
    combat_result = attack_total - defense_total
    print("combat result : " + str(combat_result))

    if combat_result > 0:
        # combat suceeded
        print("Attack was successful")
        current_health = defending_dinosaur.combat_stats.get_health_number() 
        print("current defending health:  " + str(current_health))
        defending_dinosaur.combat_stats.set_health_number(current_health - combat_result)
        print("defending dinosaur is : " + defending_dinosaur.get_custom_name())
        return defending_dinosaur.combat_stats.get_health_number()
        
        
    else:
        # combat failed
        print("Attack has failed")
        return defending_dinosaur.combat_stats.get_health_number()


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

