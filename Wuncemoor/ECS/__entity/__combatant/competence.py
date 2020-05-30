from game_messages import Message

class Competence:
    
    def __init__(self, strength, instinct, coordination, vitality, arcana, improvisation, wisdom, finesee, charisma, devotion):
        self.strength = Strength()
        self.instinct = Instinct()
        self.coordination = Coordination()
        self.vitality = Vitality()
        self.arcana = Arcana()
        self.improvisation = Improvisation()
        self.wisdom = Wisdom()
        self.finesse = Finesse()
        self.charisma = Charisma()
        self.devotion = Devotion()
        
        
        self.benefits = 0
        
    def comp_setter(self, attribute, competence):
        att_set = attribute
        comp_set = competence
        self.att_set.comp_set = True
        
    def spend_competence(self):
    
        comp_spender = self.owner
        if comp_spender.competence >= 0:
            results.append({'message': Message('What would you like to be better at?', libtcod.yellow)})
            return True
        else:
            results.append({'message': Message("You don't have the competence to spare!" , libtcod.yellow)})
            return False
        
        
class Strength:

    def __init__(self):

        self.mighty_strength_flag = False
        self.better_slash_flag = False
        self.better_stab_flag = False
        self.better_blunt_flag = False
    
    @property
    def mighty_strength(self):
        if self.mighty_strength_flag == True:
            return True
        else:
            return False

    @property    
    def better_stab(self):
        if self.better_stab_flag == True:
            return True
        else:
            return False

    @property        
    def better_slash(self):
        if self.better_slash_flag == True:
            return True
        else:
            return False
    @property        
    def better_blunt(self):
        if self.better_blunt_flag == True:
            return True
        else:
            return False
            
class Instinct:
    
    def __init__(self):
        
        self.mighty_instinct_flag = False
    
    @property
    def mighty_instinct(self):
        if self.mighty_instinct_flag == True:
            return True
        else:
            return False
            
class Coordination:

    def __init__(self):
        
        self.mighty_coordination_flag = False
    
    @property
    def mighty_coordination(self):
        if self.mighty_coordination_flag == True:
            return True
        else:
            return False
            
        
class Vitality:

    def __init__(self):

        self.mighty_vitality_flag = False       
 
    @property
    def mighty_vitality(self):
        if self.mighty_vitality_flag == True:
            return True
        else:
            return False
            

class Arcana:

    def __init_(self):
        
        self.mighty_arcana_flag = False
        
    def mighty_arcana(self):
        if self.mighty_arcana_flag == True:
            return True
        else:
            return False
            


class Improvisation:

    def __init_(self):
        
        self.mighty_improvisation_flag = False

    def mighty_improvisation(self):
        if self.mighty_improvisation_flag == True:
            return True
        else:
            return False
            

class Wisdom:

    def __init_(self):
        
        self.mighty_wisdom_flag = False

    def mighty_wisdom(self):
        if self.mighty_wisdom_flag == True:
            return True
        else:
            return False
            

class Finesse:

    def __init_(self):
        
        self.mighty_finesse_flag = False

    def mighty_finesse(self):
        if self.mighty_finesse_flag == True:
            return True
        else:
            return False
            

class Charisma:

    def __init_(self):
        
        self.mighty_charisma_flag = False

    def mighty_charisma(self):
        if self.mighty_charisma_flag == True:
            return True
        else:
            return False
            

class Devotion:

    def __init_(self):
        
        self.mighty_devotion_flag = False

    def mighty_devotion(self):
        if self.mighty_devotion_flag == True:
            return True
        else:
            return False
            

        

