class CombatLog:

    def __init__(self, combat_log_list = []):
        #default
        self.combat_log_list = combat_log_list

    def add_entry(self, combat_log_list):
        combat_log_list.append(entry)
        
    def display_combat_log(self, combat_log_list):
        for line in combat_log_list:
            print("/n" + line)
    

