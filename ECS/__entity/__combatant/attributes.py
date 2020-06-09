
#Primary stats and their base derivations
class Attributes:
    def __init__(self, strength=0, instinct=0, coordination=0, vitality=0, arcana=0, improvisation=0, wisdom=0, finesse=0, charisma=0, devotion=0):
        self.strength=strength
        self.instinct=instinct
        self.coordination=coordination
        self.vitality=vitality
        self.arcana=arcana
        self.improvisation=improvisation
        self.wisdom=wisdom
        self.finesse=finesse
        self.charisma=charisma
        self.devotion=devotion
        self.current_hp = (20*(self.strength + self.strength + self.instinct + self.coordination + self.vitality))
        self.current_mp = (20*(self.arcana + self.arcana + self.instinct + self.improvisation + self.wisdom))
        self.current_tp = (20*(self.finesse + self.finesse + self.coordination + self.improvisation + self.charisma))
        self.current_vp = (20*(self.devotion + self.devotion + self.vitality + self.wisdom + self.charisma))
#Base maximum resource functions
    @property
    def base_max_hp(self):
        return (20*(self.strength + self.strength + self.instinct + self.coordination + self.vitality))
        
    @property
    def base_max_mp(self):
        return (20*(self.arcana + self.arcana + self.instinct + self.improvisation + self.wisdom))
        
    @property
    def base_max_tp(self):
        return (20*(self.finesse + self.finesse + self.coordination + self.improvisation + self.charisma))
        
    @property
    def base_max_vp(self):
        return (20*(self.devotion + self.devotion + self.vitality + self.wisdom + self.charisma))
        
#Base adversarial stats
    @property
    def base_accuracy(self):
        return self.coordination
        
    @property
    def base_dodge(self):
        return self.finesse
        
    @property 
    def base_power_slash(self):
        return self.strength
        
    @property
    def base_power_pierce(self):
        return self.strength
        
    @property
    def base_power_blunt(self):
        return self.strength
        
    @property
    def base_spirit_heat(self):
        return self.arcana
        
    @property
    def base_spirit_cold(self):
        return self.arcana
        
    @property
    def base_spirit_acid(self):
        return self.arcana
        
    @property
    def base_spirit_current(self):
        return self.arcana
        
    @property
    def base_spirit_aether(self):
        return self.devotion
        
    @property
    def base_resist_slash(self):
        return self.vitality
        
    @property
    def base_resist_pierce(self):
        return self.vitality
        
    @property
    def base_resist_blunt(self):
        return self.vitality
        
    @property 
    def base_resist_heat(self):
        return self.vitality +self.arcana
        
    @property
    def base_resist_cold(self):
        return self.vitality + self.arcana
        
    @property
    def base_resist_acid(self):
        return self.vitality + self.arcana
        
    @property
    def base_resist_current(self):
        return self.vitality +self.arcana
        
    @property
    def base_resist_aether(self):
        return self.vitality + self.devotion
        
#Base Saving Throws
    
    @property
    def base_savethrow_reflex(self):
        bonus = self.instinct + self.improvisation + self.finesse
        return bonus
        
    @property 
    def base_savethrow_balance(self):
        bonus = self.coordination + self.improvisation + self.finesse
        return bonus
        
    @property
    def base_savethrow_breath(self):
        bonus = self.instinct + self.vitality 
        return bonus
        
    @property
    def base_savethrow_grapple(self):
        bonus = self.strength + self.instinct + self.coordination 
        return bonus
    
    @property 
    def base_savethrow_stun(self):
        bonus = self.vitality + self.improvisation
        return bonus
    
    @property
    def base_savethrow_panic(self):
        bonus = self.improvisation + self.wisdom + self.charisma
        return bonus
    
    @property
    def base_savethrow_apathy(self):
        bonus = self.wisdom + self.charisma + self.devotion
        return bonus
    
    @property
    def base_savethrow_pain(self):
        bonus = self.vitality + self.wisdom
        return bonus
        
    @property 
    def base_savethrow_bewitch(self):
        bonus = self.instinct + self.wisdom + self.charisma + self.devotion
        return bonus
    
    @property
    def base_savethrow_enrage(self):
        bonus = self.wisdom + self.charisma
        
    @property
    def base_savethrow_illness(self):
        bonus = self.vitality 
        return bonus
    
    @property
    def base_savethrow_tenacity(self):
        bonus = self.vitality + self.arcana
        return bonus
    
    @property
    def base_savethrow_pressure(self):
        bonus = self.vitality 
        return bonus
    
    @property
    def base_savethrow_bleed(self):
        bonus = self.vitality
        return bonus
    
    @property 
    def base_savethrow_injury(self):
        bonus = self.strength + self.vitality
        return bonus
        
    def set_strength(self,strength):
        self.strength = strength
        
    def set_instinct(self, instinct):
        self.instinct = instinct
        
    def set_coordination(self, coordination):
        self.coordination = coordination
        
    def set_vitality(self, vitality):
        self.vitality = vitality
        
    def set_arcana(self, arcana):
        self.arcana = arcana
        
    def set_improvisation(self, improvisation):
        self.improvisation = improvisation
        
    def set_wisdom(self, wisdom):
        self.wisdom = wisdom
        
    def set_finesse(self, finesse):
        self.finesse = finesse
        
    def set_charisma(self, charisma):
        self.charisma = charisma
        
    def set_devotion(self, devotion):
        self.devotion = devotion
        

        
    