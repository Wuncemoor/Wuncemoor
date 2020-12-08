
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

    
#True resource maximums
    
    @property
    def max_hp(self):
        if self.owner and self.equipment:
            bonus = self.equipment.max_hp_bonus
        else:
            bonus = 0
        return self.attributes.base_max_hp + bonus
        
    @property
    def max_mp(self):
        if self.owner and self.equipment:
            bonus = self.equipment.max_mp_bonus
        else:
            bonus = 0
        return self.attributes.base_max_mp + bonus
        
    @property
    def max_tp(self):
        if self.owner and self.equipment:
            bonus = self.equipment.max_tp_bonus
        else:
            bonus = 0
        return self.attributes.base_max_tp + bonus
        
    @property
    def max_vp(self):
        if self.owner and self.equipment:
            bonus = self.equipment.max_vp_bonus
        else:
            bonus = 0
        return self.attributes.base_max_vp + bonus
        
#True Power
    @property
    def power_slash(self):
        if self.owner and self.equipment:
            bonus = self.equipment.power_slash_bonus
        else:
            bonus = 0
            
        return self.attributes.base_power_slash + bonus
        
    @property
    def power_pierce(self):
        if self.owner and self.equipment:
            bonus = self.equipment.power_pierce_bonus
        else:
            bonus = 0
            
        return self.attributes.base_power_pierce + bonus
        
    @property
    def power_blunt(self):
        if self.owner and self.equipment:
            bonus = self.equipment.power_blunt_bonus
        else:
            bonus = 0
            
        return self.attributes.base_power_blunt + bonus

    @property
    def power_heat(self):
        if self.owner and self.equipment:
            bonus = self.equipment.power_heat_bonus
        else:
            bonus = 0
            
        return self.attributes.base_spirit_heat + bonus
        
    @property
    def power_cold(self):
        if self.owner and self.equipment:
            bonus = self.equipment.power_cold_bonus
        else:
            bonus = 0
            
        return self.attributes.base_spirit_cold + bonus
        
    @property
    def power_acid(self):
        if self.owner and self.equipment:
            bonus = self.equipment.power_acid_bonus
        else:
            bonus = 0
            
        return self.attributes.base_spirit_acid + bonus
        
    @property
    def power_current(self):
        if self.owner and self.equipment:
            bonus = self.equipment.power_current_bonus
        else:
            bonus = 0
            
        return self.attributes.base_spirit_current + bonus
        
    @property
    def power_aether(self):
        if self.owner and self.equipment:
            bonus = self.equipment.power_aether_bonus
        else:
            bonus = 0
            
        return self.attributes.base_spirit_aether + bonus


#True Resistance          
    
    @property
    def resist_slash(self):
        if self.owner and self.equipment:
            bonus = self.equipment.resist_slash_bonus
        else:
            bonus = 0
            
        return self.attributes.base_resist_slash + bonus
        
    @property
    def resist_pierce(self):
        if self.owner and self.equipment:
            bonus = self.equipment.resist_pierce_bonus
        else:
            bonus = 0
            
        return self.attributes.base_resist_pierce + bonus
        
    @property
    def resist_blunt(self):
        if self.owner and self.equipment:
            bonus = self.equipment.resist_blunt_bonus
        else:
            bonus = 0
            
        return self.attributes.base_resist_blunt + bonus
        
    @property
    def resist_heat(self):
        if self.owner and self.equipment:
            bonus = self.equipment.resist_heat_bonus
        else:
            bonus = 0
            
        return self.attributes.base_resist_heat + bonus
        
    @property
    def resist_cold(self):
        if self.owner and self.equipment:
            bonus = self.equipment.resist_cold_bonus
        else:
            bonus = 0
            
        return self.attributes.base_resist_cold + bonus
        
    @property
    def resist_acid(self):
        if self.owner and self.equipment:
            bonus = self.equipment.resist_acid_bonus
        else:
            bonus = 0
            
        return self.attributes.base_resist_acid + bonus
        
    @property
    def resist_current(self):
        if self.owner and self.equipment:
            bonus = self.equipment.resist_current_bonus
        else:
            bonus = 0
            
        return self.attributes.base_resist_current + bonus
        
    @property
    def resist_aether(self):
        if self.owner and self.equipment:
            bonus = self.equipment.resist_aether_bonus
        else:
            bonus = 0
            
        return self.attributes.base_resist_aether + bonus

    
#True bonuses (or penalties) to saving throws (default savethrow is d100 +/- bonus)    

    # Athletics
    @property
    def savethrow_reflex(self):
        bonus = self.attributes.instinct + self.attributes.improvisation + self.attributes.finesse
        return bonus
        
    @property 
    def savethrow_balance(self):
        bonus = self.attributes.coordination + self.attributes.improvisation + self.attributes.finesse
        return bonus
        
    @property
    def savethrow_breath(self):
        bonus = self.attributes.instinct + self.attributes.vitality 
        return bonus
        
    @property
    def savethrow_grapple(self):
        bonus = self.attributes.strength + self.attributes.instinct + self.attributes.coordination 
        return bonus
    
    @property 
    def savethrow_stun(self):
        bonus = self.attributes.vitality + self.attributes.improvisation
        return bonus

    # Fortitudes
    @property
    def savethrow_panic(self):
        bonus = self.attributes.improvisation + self.attributes.wisdom + self.attributes.charisma
        return bonus
    
    @property
    def savethrow_apathy(self):
        bonus = self.attributes.wisdom + self.attributes.charisma + self.attributes.devotion
        return bonus
    
    @property
    def savethrow_pain(self):
        bonus = self.attributes.vitality + self.attributes.wisdom
        return bonus
        
    @property 
    def savethrow_bewitch(self):
        bonus = self.attributes.instinct + self.attributes.wisdom + self.attributes.charisma + self.attributes.devotion
        return bonus
    
    @property
    def savethrow_enrage(self):
        bonus = self.attributes.wisdom + self.attributes.charisma
        return bonus

    # Resiliences
    @property
    def savethrow_illness(self):
        bonus = self.attributes.vitality 
        return bonus
    
    @property
    def savethrow_tenacity(self):
        bonus = self.attributes.vitality + self.attributes.arcana
        return bonus
    
    @property
    def savethrow_pressure(self):
        bonus = self.attributes.vitality 
        return bonus
    
    @property
    def savethrow_bleed(self):
        bonus = self.attributes.vitality
        return bonus
    
    @property 
    def savethrow_injury(self):
        bonus = self.attributes.strength + self.attributes.vitality
        return bonus
        
#Hit/Dodge
    
    @property
    def accuracy(self):
        if self.owner and self.equipment:
            bonus = self.equipment.accuracy_bonus
        else:
            bonus = 0
            
        return self.attributes.base_accuracy + bonus
    @property
    def dodge(self):
        if self.owner and self.equipment:
            bonus = self.equipment.dodge_bonus
        else:
            bonus = 0
        
        return self.attributes.base_dodge + bonus

        
#Turn order and positioning stats


    @property
    def initiative(self):
        """Who goes first?"""
        ahah = self.attributes.instinct + self.attributes.improvisation
        return ahah

    @property
    def speed(self):
        """How quickly do they gain action potential?"""
        vroom = self.attributes.coordination + self.attributes.finesse
        return vroom

    @property
    def presence(self):
        """Zone of control (ZoC) / and Attacks of Opportunity (AoO)"""
        woah = self.attributes.strength + self.attributes.vitality
        return woah

    @property
    def teamwork(self):
        """Combo moves with multiple combatants"""
        combo_potential = self.attributes.coordination
        return combo_potential

    @property
    def leadership(self):
        """Used to determine formations, designated leader gives aura buffs"""
        captain = self.attributes.coordination + self.attributes.charisma
        return captain
    
    
        
#Gain/Lose resource functions
    def lose_hp(self, amount):
        
        results = []
        self.attributes.current_hp -= amount

        if self.attributes.current_hp <= 0:
            results.append({'dead': self.owner})
            results.append({'message': Message('{0} is dead!'.format(self.owner.name), DARK_RED)})

        return results
        
    def gain_hp(self, amount):
        self.attributes.current_hp += amount
        
        if self.attributes.current_hp > self.max_hp:
            self.attributes.current_hp = self.max_hp
            
    def lose_mp(self, amount):
    
        self.current_mp  -= amount
        
        if self.current_mp <0:
            self.current_mp = 0
    def gain_mp(self, amount):
    
        self.current_mp += amount
        
        if self.current_mp > self.max_mp:
            self.current_mp = self.max_mp
            
    def lose_tp(self, amount):
        
        self.current_tp -= amount
        
        if self.current_tp < 0:
            self.current_tp = 0
            
    def gain_tp(self, amount):
    
        self.current_tp += amount
        
        if self.current_tp > self.max_tp:
            self.current_tp = self.max_tp
            
    def lose_vp(self, amount):
        
        self.current_vp -= amount
        
        if self.current_vp < 0:
            self.current_vp = 0
            
    def gain_vp(self, amount):
    
        self.current_vp += amount
        
        if self.current_vp > self.max_vp:
            self.current_vp = self.max_vp
        
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
