from andy_dinosaur import Dinosaur
import random

# Combat Engine

# Combat Phase

def combat_phase_trigger(attacking_dinosaur, defending_dinosaur):
    print("The attacking dinosaur is : " + attacking_dinosaur.get_custom_name())
    attack =  attacking_dinosaur.get_attack()
    print("attack is : " + str(attack))
    defense = defending_dinosaur.get_defense() 
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
        current_health = defending_dinosaur.get_health() 
        print("current defending health:  " + str(current_health))
        defending_dinosaur.set_health(current_health - combat_result)
        print("defending dinosaur is : " + defending_dinosaur.get_custom_name())
        print("defeinding dinosaurs health is : " + str(defending_dinosaur.get_health()))
        return defending_dinosaur.get_health()  
        
        
    else:
        # combat failed
        print("Attack has failed")
        return defending_dinosaur.get_health()


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

def combat_turn_trigger(attacking_dinosaur, defending_dinosaur):
    combat = True
    while combat == True:
        if attacking_dinosaur.get_health() > 0 and defending_dinosaur.get_health() > 0:
            combat_phase_trigger(attacking_dinosaur, defending_dinosaur)
            combat_phase_trigger(defending_dinosaur, attacking_dinosaur)
        else:
            combat = False
    
    # determine winner
    if attacking_dinosaur.get_health() > 0:
        return "The attacking dinosaur " + attacking_dinosaur.get_custom_name() + " is Victorious!"
    else:
        return "The defending dinosaur " + defending_dinosaur.get_custom_name() + " is Victorious!"