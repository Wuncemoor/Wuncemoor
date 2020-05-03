from components.combatant import Combatant
from components.competence import Competence, Strength, Instinct, Coordination, Vitality, Arcana, Improvisation, Wisdom, Finesse, Charisma, Devotion
from components.level import Level
from components.attributes import Attributes
from components.equipment import Equipment
from components.inventory import Inventory
from components.phylo import Phylo
from components.ai import BasicMonster
from map_objects.mobs import orc, troll, goblin, goblin_mage, goblin_rogue, goblin_shaman, mini_goblin, mini_goblin_mage, mini_goblin_rogue, mini_goblin_shaman, mega_goblin, mega_goblin_rogue, mega_goblin_mage, mega_goblin_shaman, mini_kobold, mini_kobold_harasser, mini_kobold_trickster, mini_kobold_zealot, kobold, kobold_harasser, kobold_trickster, kobold_zealot, mega_kobold, mega_kobold_harasser, mega_kobold_trickster, mega_kobold_zealot, mini_rat, rat, mega_rat, mini_bat, bat, mega_bat, mini_salamander, salamander, mega_salamander, mini_spider, spider, mega_spider, mini_snail, snail, mega_snail, mini_shrimp, shrimp, mega_shrimp, mini_raccoon, raccoon, mega_raccoon, mini_bear, bear, mega_bear, mini_bramblelasher, bramblelasher, mega_bramblelasher

class MobDirector:
    
    __builder = None
    
    def set_builder(self, builder):
        self.__builder = builder
        
    def get_combatant(self):
        
        combatant = self.__builder.get_combatant()
        
        
        
        return combatant
        
class MobBuilder:
        
        def __init__(self, node_power, mob):
            self.node_power = node_power
            self.mob = mob
            
        def get_combatant(self):
            mobs = { 'orc': orc(),
            'troll': troll(),
            'mini_goblin': mini_goblin(),
            'goblin': goblin(),
            'mega_goblin': mega_goblin(),
            'mini_goblin_mage': mini_goblin_mage(),
            'goblin_mage': goblin_mage(),
            'mega_goblin_mage': mega_goblin_mage(),
            'mini_goblin_rogue': mini_goblin_rogue(),
            'goblin_rogue': goblin_rogue(),
            'mega_goblin_rogue': mega_goblin_rogue(),
            'mini_goblin_shaman': mini_goblin_shaman(),
            'goblin_shaman': goblin_shaman(),
            'mega_goblin_shaman': mega_goblin_shaman(),
            'mini_kobold': mini_kobold(),
            'kobold': kobold(),
            'mega_kobold': mega_kobold(),
            'mini_kobold_harasser': mini_kobold_harasser(),
            'kobold_harasser': kobold_harasser(),
            'mega_kobold_harasser': mega_kobold_harasser(),
            'mini_kobold_trickster': mini_kobold_trickster(),
            'kobold_trickster': kobold_trickster(),
            'mega_kobold_trickster': mega_kobold_trickster(),
            'mini_kobold_zealot': mini_kobold_zealot(),
            'kobold_zealot': kobold_zealot(),
            'mega_kobold_zealot': mega_kobold_zealot(),
            'mini_rat': mini_rat(),
            'rat': rat(),
            'mega_rat': mega_rat(),
            'mini_bat': mini_bat(),
            'bat': bat(),
            'mega_bat': mega_bat(),
            'mini_salamander': mini_salamander(),
            'salamander': salamander(),
            'mega_salamander': mega_salamander(),
            'mini_spider': mini_spider(),
            'spider': spider(),
            'mega_spider': mega_spider(),
            'mini_snail': mini_snail(),
            'snail': snail(),
            'mega_snail': mega_snail(),
            'mini_shrimp': mini_shrimp(),
            'shrimp': shrimp(),
            'mega_shrimp': mega_shrimp(),
            'mini_raccoon': mini_raccoon(),
            'raccoon': raccoon(),
            'mega_raccoon': mega_raccoon(),
            'mini_bear': mini_bear(),
            'bear': bear(),
            'mega_bear': mega_bear(),
            'mini_bramblelasher' : mini_bramblelasher(),
            'bramblelasher': bramblelasher(),
            'mega_bramblelasher': mega_bramblelasher(),
            }
            return mobs[self.mob]            
            
        
      