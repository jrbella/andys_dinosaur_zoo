from andy_dinosaur import Dinosaur

# Combat Engine

# Attackers Phase

def attack_phase_trigger(attacking_dinosaur, defending_dinosaur):
    attack =  attacking_dinosaur.combat_stats.get_attack()
    defense = defending_dinosaur.combat_stats.get_defense()
# Defenders Phase
