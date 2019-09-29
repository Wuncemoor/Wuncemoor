
import tcod as libtcod
from game_messages import Message
import random
import math

class Combatant:
    def __init__(self, attributes, xp=0):
        self.attributes = attributes
        self.current_hp = attributes.current_hp
        self.current_mp = attributes.current_mp
        self.current_tp = attributes.current_tp
        self.current_vp = attributes.current_vp
        self.base_max_hp = attributes.base_max_hp
        self.base_max_mp = attributes.base_max_mp
        self.base_max_tp = attributes.base_max_tp
        self.base_max_vp = attributes.base_max_vp
        self.base_defence = attributes.vitality
        self.base_power = attributes.strength
        self.xp = xp
        self.hit = attributes.coordination
        self.dodge = attributes.finesse
        
       

    
#Maximum resources with equipment on
    @property
    def max_hp(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_hp_bonus
        else:
            bonus = 0
        return self.base_max_hp + bonus
    @property
    def max_mp(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_mp_bonus
        else:
            bonus = 0
        return self.base_max_mp + bonus
    @property
    def max_tp(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_tp_bonus
        else:
            bonus = 0
        return self.base_max_tp + bonus
    @property
    def max_vp(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_vp_bonus
        else:
            bonus = 0
        return self.base_max_vp + bonus
    @property
    def power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.power_bonus
        else:
            bonus = 0
            
        return self.base_power + bonus
        
    @property
    def defence(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.defence_bonus
        else:
            bonus = 0
            
        return self.base_defence + bonus

#Resistances to reduce damage taken of various types  , each point of resistance provides 1% effective health (EHP)  
    @property
    def resist_slash(self):
        resist = self.vitality
        return resist
        
    @property
    def resist_pierce(self):
        resist = self.vitality
        return resist
        
    @property
    def resist_blunt(self):
        resist = self.vitality
        return resist
        
    @property
    def resist_heat(self):
        resist = self.vitality + self.arcana
        return resist
        
    @property
    def resist_cold(self):
        resist = self.vitality + self.arcana
        return resist
        
    @property
    def resist_acid(self):
        resist = self.vitality + self.arcana
        return resist
    
    @property
    def resist_current(self):
        resist = self.vitality + self.arcana
        return resist
    
    @property
    def resist_aether(self):
        resist = self.vitality + self.devotion
        return resist
        
    
#bonuses (or penalties) to saving throws (default savethrow is d100 +/- bonus)    
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
        self.current_hp -= amount
        
        if self.current_hp <= 0:
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
        results = []
        hit_vs_dodge = self.hit - target.combatant.dodge + random.randrange(100) - 50
        
        if hit_vs_dodge >= 0:
        
            #damage + or - 5% variation, rounded down
            damage = math.floor(((self.power ** 2) - (target.combatant.defence))*((random.randrange(10)+95)/100))
            
            if damage > 0:
                results.append({'message': Message('{0} attacks {1} for {2} hit points.'.format(self.owner.name.capitalize(), target.name, str(damage)), libtcod.white)})
                results.extend(target.combatant.lose_hp(damage))
            else:
                results.append({'message': Message('{0} attacks {1} but does no damage!.'.format(self.owner.name.capitalize(), target.name), libtcod.white)})
            return results
            
        else:
        
            results.append({'message': Message('{0} attacks, but {1} dodges!'.format(self.owner.name.capitalize(), target.name), libtcod.white)})
            return results