
import tcod as libtcod
from game_messages import Message
import random
import math

class Combatant:
    def __init__(self, attributes, xp=0):
        self.attributes = attributes
        self.xp = xp
    
#True resource maximums
    
    @property
    def max_hp(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_hp_bonus
        else:
            bonus = 0
        return self.attributes.base_max_hp + bonus
        
    @property
    def max_mp(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_mp_bonus
        else:
            bonus = 0
        return self.attributes.base_max_mp + bonus
        
    @property
    def max_tp(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_tp_bonus
        else:
            bonus = 0
        return self.attributes.base_max_tp + bonus
        
    @property
    def max_vp(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_vp_bonus
        else:
            bonus = 0
        return self.attributes.base_max_vp + bonus
        
#True Power
    @property
    def power_slash(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.power_slash_bonus
        else:
            bonus = 0
            
        return self.attributes.base_power_slash + bonus
        
    @property
    def power_pierce(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.power_pierce_bonus
        else:
            bonus = 0
            
        return self.attributes.base_power_pierce + bonus
        
    @property
    def power_blunt(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.power_blunt_bonus
        else:
            bonus = 0
            
        return self.attributes.base_power_blunt + bonus
        
#True Spirits
    
    @property
    def spirit_heat(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.spirit_heat_bonus
        else:
            bonus = 0
            
        return self.attributes.base_spirit_heat + bonus
        
    @property
    def spirit_cold(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.spirit_cold_bonus
        else:
            bonus = 0
            
        return self.attributes.base_spirit_cold + bonus
        
    @property
    def spirit_acid(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.spirit_acid_bonus
        else:
            bonus = 0
            
        return self.attributes.base_spirit_acid + bonus
        
    @property
    def spirit_current(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.spirit_current_bonus
        else:
            bonus = 0
            
        return self.attributes.base_spirit_current + bonus
        
    @property
    def spirit_aether(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.spirit_aether_bonus
        else:
            bonus = 0
            
        return self.attributes.base_spirit_aether + bonus


#True Resistance          
    
    @property
    def resist_slash(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.resist_slash_bonus
        else:
            bonus = 0
            
        return self.attributes.base_resist_slash + bonus
        
    @property
    def resist_pierce(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.resist_pierce_bonus
        else:
            bonus = 0
            
        return self.attributes.base_resist_pierce + bonus
        
    @property
    def resist_blunt(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.resist_blunt_bonus
        else:
            bonus = 0
            
        return self.attributes.base_resist_blunt + bonus
        
    @property
    def resist_heat(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.resist_heat_bonus
        else:
            bonus = 0
            
        return self.attributes.base_resist_heat + bonus
        
    @property
    def resist_cold(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.resist_cold_bonus
        else:
            bonus = 0
            
        return self.attributes.base_resist_cold + bonus
        
    @property
    def resist_acid(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.resist_acid_bonus
        else:
            bonus = 0
            
        return self.attributes.base_resist_acid + bonus
        
    @property
    def resist_current(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.resist_current_bonus
        else:
            bonus = 0
            
        return self.attributes.base_resist_current + bonus
        
    @property
    def resist_aether(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.resist_aether_bonus
        else:
            bonus = 0
            
        return self.attributes.base_resist_aether + bonus

    
#True bonuses (or penalties) to saving throws (default savethrow is d100 +/- bonus)    
    
    @property
    def savethrow_reflex(self):
        bonus = self.instinct + self.improvisation + self.finesse
        return bonus
        
    @property 
    def savethrow_balance(self):
        bonus = self.coordination + self.improvisation + self.finesse
        return bonus
        
    @property
    def savethrow_breath(self):
        bonus = self.instinct + self.vitality 
        return bonus
        
    @property
    def savethrow_grapple(self):
        bonus = self.strength + self.instinct + self.coordination 
        return bonus
    
    @property 
    def savethrow_stun(self):
        bonus = self.vitality + self.improvisation
        return bonus
    
    @property
    def savethrow_panic(self):
        bonus = self.improvisation + self.wisdom + self.charisma
        return bonus
    
    @property
    def savethrow_apathy(self):
        bonus = self.wisdom + self.charisma + self.devotion
        return bonus
    
    @property
    def savethrow_pain(self):
        bonus = self.vitality + self.wisdom
        return bonus
        
    @property 
    def savethrow_bewitch(self):
        bonus = self.instinct + self.wisdom + self.charisma + self.devotion
        return bonus
    
    @property
    def savethrow_enrage(self):
        bonus = self.wisdom + self.charisma
        
    @property
    def savethrow_illness(self):
        bonus = self.vitality 
        return bonus
    
    @property
    def savethrow_tenacity(self):
        bonus = self.vitality + self.arcana
        return bonus
    
    @property
    def savethrow_pressure(self):
        bonus = self.vitality 
        return bonus
    
    @property
    def savethrow_bleed(self):
        bonus = self.vitality
        return bonus
    
    @property 
    def savethrow_injury(self):
        bonus = self.strength + self.vitality
        return bonus
        
#Hit/Dodge
    
    @property
    def accuracy(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.accuracy_bonus
        else:
            bonus = 0
            
        return self.attributes.base_accuracy + bonus
    @property
    def dodge(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.dodge_bonus
        else:
            bonus = 0
        
        return self.attributes.base_dodge + bonus

        
#Turn order and positioning stats

    #Who goes first?
    @property
    def initiative(self):
        bonus = self.instinct + self.improvisation
        return bonus
    #How quickly do they gain action potential?    
    @property
    def speed(self):
        vroom = self.coordination + self.finesse
        return vroom
    #Zone of control (ZoC) / and Attacks of Opportunity (AoO)
    @property
    def presence(self):
        woah = self.strength + self.vitality
        return woah
    #Combo moves with multiple combatants
    @property
    def teamwork(self):
        combo_potential = self.coordination
        return combo_potential
    #Used to determine formations, designated leader gives aura buffs
    @property
    def leadership(self):
        captain = self.coordination + self.charisma
        return captain
    
    
        
#Gain/Lose resource functions
    def lose_hp(self, amount):
        
        results = []
        self.attributes.current_hp -= amount
        
        if self.attributes.current_hp <= 0:
            results.append({'dead': self.owner, 'xp':self.xp})
            
        return results
        
    def gain_hp(self, amount):
        self.current_hp += amount
        
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp
            
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
                results.append({'message': Message('{0} attacks {1} for {2} {3} damage.'.format(self.owner.name.capitalize(), target.name, str(damage), attack), libtcod.white)})
                results.extend(target.combatant.lose_hp(damage))
            else:
                results.append({'message': Message('{0} attacks {1} but does no damage!.'.format(self.owner.name.capitalize(), target.name), libtcod.white)})
            return results
            
        else:
        
            results.append({'message': Message('{0} attacks, but {1} dodges!'.format(self.owner.name.capitalize(), target.name), libtcod.white)})
            return results