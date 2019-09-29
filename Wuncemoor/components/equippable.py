class Equippable:
    def __init__(self, slot, resource_bonuses=[0,0,0,0],power_bonuses=[0,0,0], spirit_bonuses=[0,0,0,0,0], resist_phys_bonuses=[0,0,0], resist_ele_bonuses=[0,0,0,0,0], hit_dodge_bonuses=[0,0]):
        self.slot = slot
        
        self.max_hp_bonus = resource_bonuses[0]
        self.max_mp_bonus = resource_bonuses[1]
        self.max_tp_bonus = resource_bonuses[2]
        self.max_vp_bonus = resource_bonuses[3]
        
        self.power_slash_bonus = power_bonuses[0]
        self.power_pierce_bonus = power_bonuses[1]
        self.power_blunt_bonus = power_bonuses[2]
        
        self.spirit_heat_bonus = spirit_bonuses[0]
        self.spirit_cold_bonus = spirit_bonuses[1]
        self.spirit_acid_bonus = spirit_bonuses[2]
        self.spirit_current_bonus = spirit_bonuses[3]
        self.spirit_aether_bonus = spirit_bonuses[4]
        
        self.resist_slash_bonus = resist_phys_bonuses[0]
        self.resist_pierce_bonus = resist_phys_bonuses[1]
        self.resist_blunt_bonus = resist_phys_bonuses[2]
        
        self.resist_heat_bonus = resist_ele_bonuses[0]
        self.resist_cold_bonus = resist_ele_bonuses[1]
        self.resist_acid_bonus = resist_ele_bonuses[2]
        self.resist_current_bonus = resist_ele_bonuses[3]
        self.resist_aether_bonus = resist_ele_bonuses[4]
        
        self.accuracy_bonus = hit_dodge_bonuses[0]
        self.dodge_bonus = hit_dodge_bonuses[1]