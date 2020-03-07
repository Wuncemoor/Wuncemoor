from components.combatant import Combatant
from components.competence import Competence, Strength, Instinct, Coordination, Vitality, Arcana, Improvisation, Wisdom, Finesse, Charisma, Devotion
from components.level import Level
from components.attributes import Attributes
from components.equipment import Equipment
from components.inventory import Inventory
from components.ai import BasicMonster

class MobDirector:
    
    __builder = None
    
    def set_builder(self, builder):
        self.__builder = builder
        
    def get_combatant(self):
        combatant = Combatant('NAME_UNDEFINED', 'IMAGE_UNDEFINED', Attributes(), Level(), Competence(Strength(), Instinct(), Coordination(), Vitality(), Arcana(), Improvisation(), Wisdom(), Finesse(), Charisma(), Devotion()), Equipment(), Inventory(26))
        
        name = self.__builder.get_name()
        combatant.set_name(name)
        
        image = self.__builder.get_image()
        combatant.set_image(image)
        
        attributes = self.__builder.get_attributes()
        combatant.set_attributes(attributes)
        
        level = self.__builder.get_level()
        combatant.set_level(level)
        
        competence = self.__builder.get_competence()
        combatant.set_competence(competence)
        
        equipment = self.__builder.get_equipment()
        combatant.set_equipment(equipment)
        
        inventory = self.__builder.get_inventory()
        combatant.set_inventory(inventory)
        
        ai = self.__builder.get_ai()
        combatant.set_ai(ai)
        
        xp = self.__builder.get_xp()
        combatant.set_xp(xp)
        
        
        
        return combatant
        
class MobBuilder:
        
        def __init__(self, node_power, mob):
            self.node_power = node_power
            self.mob = mob
            
        def get_name(self):
            return self.mob
            
        def get_image(self):
            mobs = { 'orc': 'o', 'troll': 'T' }
            image = mobs[self.mob]
            return image
            
        def get_attributes(self):
            
            mobs = { 'orc': Attributes(5,0,0,7,10,10,10,10,10,10), 'troll': Attributes(1,0,0,10,10,10,10,10,10,10)}
            attributes = mobs[self.mob]
            return attributes
            
        def get_level(self):
            
            level = Level()
            return level
            
        def get_competence(self):
            
            competence = Competence(Strength(),Instinct(),Coordination(),Vitality(),Arcana(),Improvisation(),Wisdom(),Finesse(),Charisma(),Devotion())
            
            return competence
        
        def get_equipment(self):
            
            return Equipment()
            
        def get_inventory(self):
            
            return Inventory(26)
            
        def get_ai(self):
        
            return BasicMonster()
            
        def get_xp(self):
            
            dict = { 'orc': 350, 'troll': 1000}
            xp = dict[self.mob]
            return xp
            
            
        
      