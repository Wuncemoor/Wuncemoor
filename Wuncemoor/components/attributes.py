import tcod as libtcod

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

        
    