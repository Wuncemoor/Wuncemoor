
from handlers.views.messages import Message
import random
import math
from config.constants import BLACK, DARK_RED


class Combatant:
    """Component for Entities to fight with"""
    def __init__(self, name, images, phylo, attributes, level, competence, equipment, satchel, ai=None, xp=0, sex=None):
        
        self.name = name
        self.images = images
        self.phylo = phylo
        self.attributes = attributes
        self.level = level
        self.competence = competence
        self.equipment = equipment
        self.satchel = satchel
        self.ai = ai
        self.xp = xp
        self.competence_points = 0
        self.sex = sex

    # Resources
    
    @property
    def max_hp(self):
        if self.owner and self.equipment:
            equipment = self.equipment.max_hp_bonus
        else:
            equipment = 0
        return self.attributes.base_max_hp + equipment
        
    @property
    def max_mp(self):
        if self.owner and self.equipment:
            equipment = self.equipment.max_mp_bonus
        else:
            equipment = 0
        return self.attributes.base_max_mp + equipment
        
    @property
    def max_tp(self):
        if self.owner and self.equipment:
            equipment = self.equipment.max_tp_bonus
        else:
            equipment = 0
        return self.attributes.base_max_tp + equipment
        
    @property
    def max_vp(self):
        if self.owner and self.equipment:
            equipment = self.equipment.max_vp_bonus
        else:
            equipment = 0
        return self.attributes.base_max_vp + equipment
        
    # Primary Stats

    @property
    def power_slash(self):
        if self.owner and self.equipment:
            equipment = self.equipment.power_slash_bonus
        else:
            equipment = 0
            
        return self.attributes.base_power_slash + equipment
        
    @property
    def power_pierce(self):
        if self.owner and self.equipment:
            equipment = self.equipment.power_pierce_bonus
        else:
            equipment = 0
            
        return self.attributes.base_power_pierce + equipment
        
    @property
    def power_blunt(self):
        if self.owner and self.equipment:
            equipment = self.equipment.power_blunt_bonus
        else:
            equipment = 0
            
        return self.attributes.base_power_blunt + equipment

    @property
    def power_heat(self):
        if self.owner and self.equipment:
            equipment = self.equipment.power_heat_bonus
        else:
            equipment = 0
            
        return self.attributes.base_power_heat + equipment
        
    @property
    def power_cold(self):
        if self.owner and self.equipment:
            equipment = self.equipment.power_cold_bonus
        else:
            equipment = 0
            
        return self.attributes.base_power_cold + equipment
        
    @property
    def power_acid(self):
        if self.owner and self.equipment:
            equipment = self.equipment.power_acid_bonus
        else:
            equipment = 0
            
        return self.attributes.base_power_acid + equipment
        
    @property
    def power_current(self):
        if self.owner and self.equipment:
            equipment = self.equipment.power_current_bonus
        else:
            equipment = 0
            
        return self.attributes.base_power_current + equipment
        
    @property
    def power_aether(self):
        if self.owner and self.equipment:
            equipment = self.equipment.power_aether_bonus
        else:
            equipment = 0
            
        return self.attributes.base_power_aether + equipment
    
    @property
    def resist_slash(self):
        if self.owner and self.equipment:
            equipment = self.equipment.resist_slash_bonus
        else:
            equipment = 0
            
        return self.attributes.base_resist_slash + equipment
        
    @property
    def resist_pierce(self):
        if self.owner and self.equipment:
            equipment = self.equipment.resist_pierce_bonus
        else:
            equipment = 0
            
        return self.attributes.base_resist_pierce + equipment
        
    @property
    def resist_blunt(self):
        if self.owner and self.equipment:
            equipment = self.equipment.resist_blunt_bonus
        else:
            equipment = 0
            
        return self.attributes.base_resist_blunt + equipment
        
    @property
    def resist_heat(self):
        if self.owner and self.equipment:
            equipment = self.equipment.resist_heat_bonus
        else:
            equipment = 0
            
        return self.attributes.base_resist_heat + equipment
        
    @property
    def resist_cold(self):
        if self.owner and self.equipment:
            equipment = self.equipment.resist_cold_bonus
        else:
            equipment = 0
            
        return self.attributes.base_resist_cold + equipment
        
    @property
    def resist_acid(self):
        if self.owner and self.equipment:
            equipment = self.equipment.resist_acid_bonus
        else:
            equipment = 0
            
        return self.attributes.base_resist_acid + equipment
        
    @property
    def resist_current(self):
        if self.owner and self.equipment:
            equipment = self.equipment.resist_current_bonus
        else:
            equipment = 0
            
        return self.attributes.base_resist_current + equipment
        
    @property
    def resist_aether(self):
        if self.owner and self.equipment:
            equipment = self.equipment.resist_aether_bonus
        else:
            equipment = 0
            
        return self.attributes.base_resist_aether + equipment

    # Secondary Stats

    @property
    def initiative(self):
        """Who goes first?"""
        if self.owner and self.equipment:
            equipment = self.equipment.initiative_bonus
        else:
            equipment = 0

        return self.attributes.base_initiative + equipment

    @property
    def speed(self):
        """How quickly do they gain action potential?"""
        if self.owner and self.equipment:
            equipment = self.equipment.speed_bonus
        else:
            equipment = 0

        return self.attributes.base_speed + equipment

    @property
    def accuracy(self):
        """How likely to successfully hit a target"""
        if self.owner and self.equipment:
            equipment = self.equipment.accuracy_bonus
        else:
            equipment = 0

        return self.attributes.base_accuracy + equipment

    @property
    def dodge(self):
        """How likely to avoid being hit when targeted"""
        if self.owner and self.equipment:
            equipment = self.equipment.dodge_bonus
        else:
            equipment = 0

        return self.attributes.base_dodge + equipment

    @property
    def critical_strike(self):
        """Crits have more damage and bonus effects"""
        if self.owner and self.equipment:
            equipment = self.equipment.critical_strike_bonus
        else:
            equipment = 0

        return self.attributes.base_critical_strike + equipment


    @property
    def critical_damage(self):
        """How much extra damage crits do"""
        if self.owner and self.equipment:
            equipment = self.equipment.critical_damage_bonus
        else:
            equipment = 0

        return self.attributes.base_critical_damage + equipment


    @property
    def presence(self):
        """Zone of control (ZoC) / and Attacks of Opportunity (AoO)"""
        if self.owner and self.equipment:
            equipment = self.equipment.presence_bonus
        else:
            equipment = 0

        return self.attributes.base_presence + equipment


    @property
    def teamwork(self):
        """Combo moves with multiple combatants"""
        if self.owner and self.equipment:
            equipment = self.equipment.teamwork_bonus
        else:
            equipment = 0

        return self.attributes.base_teamwork + equipment

    # True bonuses (or penalties) to saving throws (default savethrow is d100 +/- bonus)

    @property
    def savethrow_injury(self) -> int:
        if self.owner and self.equipment:
            equipment = self.equipment.savethrow_injury_bonus
        else:
            equipment = 0

        return self.attributes.base_savethrow_injury + equipment

    @property
    def savethrow_illness(self) -> int:
        if self.owner and self.equipment:
            equipment = self.equipment.savethrow_illness_bonus
        else:
            equipment = 0

        return self.attributes.base_savethrow_illness + equipment

    @property
    def savethrow_tenacity(self) -> int:
        if self.owner and self.equipment:
            equipment = self.equipment.savethrow_tenacity_bonus
        else:
            equipment = 0

        return self.attributes.base_savethrow_tenacity + equipment

    @property
    def savethrow_apathy(self) -> int:
        if self.owner and self.equipment:
            equipment = self.equipment.savethrow_apathy_bonus
        else:
            equipment = 0

        return self.attributes.base_savethrow_apathy + equipment

    @property
    def savethrow_composure(self) -> int:
        if self.owner and self.equipment:
            equipment = self.equipment.savethrow_composure_bonus
        else:
            equipment = 0

        return self.attributes.base_savethrow_composure + equipment

    @property
    def savethrow_pain(self) -> int:
        if self.owner and self.equipment:
            equipment = self.equipment.savethrow_pain_bonus
        else:
            equipment = 0

        return self.attributes.base_savethrow_pain + equipment

    @property
    def savethrow_cognition(self) -> int:
        if self.owner and self.equipment:
            equipment = self.equipment.savethrow_cognition_bonus
        else:
            equipment = 0

        return self.attributes.base_savethrow_cognition + equipment

    @property
    def savethrow_force(self) -> int:
        if self.owner and self.equipment:
            equipment = self.equipment.savethrow_force_bonus
        else:
            equipment = 0

        return self.attributes.base_savethrow_force + equipment

    @property
    def savethrow_breath(self) -> int:
        if self.owner and self.equipment:
            equipment = self.equipment.savethrow_breath_bonus
        else:
            equipment = 0

        return self.attributes.base_savethrow_breath + equipment

    @property
    def savethrow_reflex(self) -> int:
        if self.owner and self.equipment:
            equipment = self.equipment.savethrow_reflex_bonus
        else:
            equipment = 0

        return self.attributes.base_savethrow_reflex + equipment

    @property
    def savethrow_corruption(self) -> int:
        if self.owner and self.equipment:
            equipment = self.equipment.savethrow_corruption_bonus
        else:
            equipment = 0

        return self.attributes.base_savethrow_corruption + equipment

    @property
    def savethrow_will(self) -> int:
        if self.owner and self.equipment:
            equipment = self.equipment.savethrow_will_bonus
        else:
            equipment = 0

        return self.attributes.base_savethrow_will + equipment

# Gain/Lose resource functions
    def lose_hp(self, amount):
        
        results = []
        self.attributes.current_hp -= amount

        if self.attributes.current_hp <= 0:
            self.attributes.current_hp = 0
            # add overkill here later
            results.append({'dead': self.owner})
            results.append({'message': Message('{0} is dead!'.format(self.owner.name), DARK_RED)})

        return results
        
    def gain_hp(self, amount):
        self.attributes.current_hp += amount
        
        if self.attributes.current_hp > self.max_hp:
            self.attributes.current_hp = self.max_hp
            
    def lose_mp(self, amount):
    
        self.attributes.current_mp -= amount
        
        if self.attributes.current_mp < 0:
            self.attributes.current_mp = 0

    def gain_mp(self, amount):
    
        self.attributes.current_mp += amount
        
        if self.attributes.current_mp > self.max_mp:
            self.attributes.current_mp = self.max_mp
            
    def lose_tp(self, amount):
        
        self.attributes.current_tp -= amount
        
        if self.attributes.current_tp < 0:
            self.attributes.current_tp = 0
            
    def gain_tp(self, amount):
    
        self.attributes.urrent_tp += amount
        
        if self.attributes.current_tp > self.max_tp:
            self.attributes.current_tp = self.max_tp
            
    def lose_vp(self, amount):
        
        self.attributes.current_vp -= amount
        
        if self.attributes.current_vp < 0:
            self.attributes.current_vp = 0
            
    def gain_vp(self, amount):
    
        self.attributes.current_vp += amount
        
        if self.attributes.current_vp > self.max_vp:
            self.attributes.current_vp = self.max_vp
        
    def attack(self, target):
        compare_slash = self.power_slash - target.combatant.resist_slash
        compare_pierce = self.power_pierce - target.combatant.resist_pierce
        compare_blunt = self.power_blunt - target.combatant.resist_blunt
        attack_type = None
        attack = None
        best_attack = max(compare_slash, compare_pierce, compare_blunt)
        if best_attack == compare_slash:
            attack_type, attack, resist_type = self.power_slash, 'slash', target.combatant.resist_slash
        elif best_attack == compare_pierce:
            attack_type, attack, resist_type = self.power_pierce, 'pierce', target.combatant.resist_pierce
        elif best_attack == compare_blunt:
            attack_type, attack, resist_type = self.power_blunt, 'blunt', target.combatant.resist_blunt

        results = []
        hit_vs_dodge = self.accuracy - target.combatant.dodge + random.randrange(100) - 50
        
        if hit_vs_dodge >= 0:
        
            #damage + or - 5% variation, rounded down
            damage = math.floor(((attack_type ** 2) - (resist_type))*((random.randrange(10)+95)/100))
            
            if damage > 0:
                results.append({'message': Message('{0} attacks {1} for {2} {3} damage.'.format(self.owner.name, target.name, str(damage), attack), BLACK)})
                results.extend(target.combatant.lose_hp(damage))

            else:
                results.append({'message': Message('{0} attacks {1} but does no damage!.'.format(self.owner.name, target.name), BLACK)})

            
        else:
        
            results.append({'message': Message('{0} attacks, but {1} dodges!'.format(self.owner.name, target.name), BLACK)})

        results.append({'end_turn': True})
        return results

    def set_name(self, name):
        self.name = name
        
    def set_image(self, image):
        self.image = image
        
    def set_phylo(self, phylo):
        self.phylo = phylo
        
    def set_attributes(self, attributes):
        self.attributes = attributes
        
    def set_level(self, level):
        self.level = level
        
    def set_competence(self, competence):
        self.competence = competence
        
    def set_equipment(self, equipment):
        self.equipment = equipment
        
    def set_inventory(self, inventory):
        self.inventory = inventory
        
    def set_ai(self, ai):
        self.ai = ai
        
    def set_xp(self, xp):
        self.xp = xp
