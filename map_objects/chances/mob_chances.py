from random_utils import from_dungeon_level, from_node_power
from collections import Counter


class MobChances:

    def __init__(self, d_type, subtype, np, mob='mob'):
        self.d_type = d_type
        self.subtype = subtype
        self.np = np
        self.mob = mob
        self.type_dict = None
        self.subtype_dict = None
        self.supertype_dict = None
        

    def get_mob_chances(self):

        self.type_dict = {
            'cave': self.get_cave_type_chances(),
            }
            
        self.subtype_dict = {
            'kobold': self.get_kobold_subtype_chances(),
            'goblin': self.get_goblin_subtype_chances(),
            None: Counter({})
            }
            
        self.supertype_dict = {
            'mob': self.get_mob_supertype_chances(),
            'boss': self.get_boss_supertype_chances(),
            }

        mobset = self.supertype_dict[self.mob]
            
            
            
        return mobset
    
    def get_mob_supertype_chances(self):

        base_chances = self.type_dict[self.d_type]

        
        if self.subtype is None:
            bonus_chances = Counter({})
        else:
            
            bonus_chances = self.subtype_dict[self.subtype]
        return base_chances + bonus_chances
        
    def get_boss_supertype_chances(self):

        base_chances = Counter({})
        
        bonus_chances = self.subtype_dict[self.subtype]
        
        return base_chances + bonus_chances

    def get_cave_type_chances(self):

        cave = Counter({
                    'mini_rat': from_node_power([[100,0], [75,25], [50,50], [25,75], [0,100]], self.np),
                    'rat': from_node_power([[0,0], [50,75], [75, 150], [100, 225], [75, 300], [50, 375], [0, 450]], self.np),
                    'mega_rat': from_node_power([[0,0], [25, 500], [50, 1000], [100, 2500]], self.np), 
                    'mini_bat': from_node_power([[100,0], [75,25], [50,50], [25,75], [0,100]], self.np),
                    'bat': from_node_power([[0,0], [50,75], [75, 150], [100, 225], [75, 300], [50, 375], [0, 450]], self.np),
                    'mega_bat': from_node_power([[0,0], [25, 500], [50, 1000], [100, 2500]], self.np), 
                    'mini_salamander': from_node_power([[100,0], [75,25], [50,50], [25,75], [0,100]], self.np),
                    'salamander': from_node_power([[0,0], [50,75], [75, 150], [100, 225], [75, 300], [50, 375], [0, 450]], self.np),
                    'mega_salamander': from_node_power([[0,0], [25, 500], [50, 1000], [100, 2500]], self.np), 
                    'mini_spider': from_node_power([[100,0], [75,25], [50,50], [25,75], [0,100]], self.np),
                    'spider': from_node_power([[0,0], [50,75], [75, 150], [100, 225], [75, 300], [50, 375], [0, 450]], self.np),
                    'mega_spider': from_node_power([[0,0], [25, 500], [50, 1000], [100, 2500]], self.np), 
                    'mini_snail': from_node_power([[100,0], [75,25], [50,50], [25,75], [0,100]], self.np),
                    'snail': from_node_power([[0,0], [50,75], [75, 150], [100, 225], [75, 300], [50, 375], [0, 450]], self.np),
                    'mega_snail': from_node_power([[0,0], [25, 500], [50, 1000], [100, 2500]], self.np), 
                    'mini_shrimp': from_node_power([[100,0], [75,25], [50,50], [25,75], [0,100]], self.np),
                    'shrimp': from_node_power([[0,0], [50,75], [75, 150], [100, 225], [75, 300], [50, 375], [0, 450]], self.np),
                    'mega_shrimp': from_node_power([[0,0], [25, 500], [50, 1000], [100, 2500]], self.np), 
                    'mini_raccoon': from_node_power([[100,0], [75,25], [50,50], [25,75], [0,100]], self.np),
                    'raccoon': from_node_power([[0,0], [50,75], [75, 150], [100, 225], [75, 300], [50, 375], [0, 450]], self.np),
                    'mega_raccoon': from_node_power([[0,0], [25, 500], [50, 1000], [100, 2500]], self.np), 
                    'mini_bear': from_node_power([[100,0], [75,25], [50,50], [25,75], [0,100]], self.np),
                    'bear': from_node_power([[0,0], [50,75], [75, 150], [100, 225], [75, 300], [50, 375], [0, 450]], self.np),
                    'mega_bear': from_node_power([[0,0], [25, 500], [50, 1000], [100, 2500]], self.np), 
                    })
        return cave                
        
            
    def get_kobold_subtype_chances(self):

        k = Counter({
                        'mini_kobold': from_node_power([[100,0], [75,25], [50,50], [25,75], [0,100]], self.np),
                        'kobold' : from_node_power([[0,0], [50,75], [75, 150], [100, 225], [75, 300], [50, 375], [0, 450]], self.np),
                        'mega_kobold': from_node_power([[0,0], [25, 500], [50, 1000], [100, 2500]], self.np), 
                        'mini_kobold_harasser': from_node_power([[100,0], [75,25], [50,50], [25,75], [0,100]], self.np),
                        'kobold_harasser': from_node_power([[0,0], [50,75], [75, 150], [100, 225], [75, 300], [50, 375], [0, 450]], self.np),
                        'mega_kobold_harasser': from_node_power([[0,0], [25, 500], [50, 1000], [100, 2500]], self.np),
                        'mini_kobold_trickster': from_node_power([[100,0], [75,25], [50,50], [25,75], [0,100]], self.np),
                        'kobold_trickster': from_node_power([[0,0], [50,75], [75, 150], [100, 225], [75, 300], [50, 375], [0, 450]], self.np),
                        'mega_kobold_trickster': from_node_power([[0,0], [25, 500], [50, 1000], [100, 2500]], self.np),
                        'mini_kobold_zealot': from_node_power([[100,0], [75,25], [50,50], [25,75], [0,100]], self.np),
                        'kobold_zealot': from_node_power([[0,0], [50,75], [75, 150], [100, 225], [75, 300], [50, 375], [0, 450]], self.np),
                        'mega_kobold_zealot': from_node_power([[0,0], [25, 500], [50, 1000], [100, 2500]], self.np)
                        })
        
        return k  
        
    def get_goblin_subtype_chances(self):
        
        g = Counter({
                    'mini_goblin': from_node_power([[100,0], [75,25], [50,50], [25,75], [0,100]], self.np),
                    'goblin' : from_node_power([[0,0], [50,75], [75, 150], [100, 225], [75, 300], [50, 375], [0, 450]], self.np),
                    'mega_goblin': from_node_power([[0,0], [25, 500], [50, 1000], [100, 2500]], self.np), 
                    'mini_goblin_rogue': from_node_power([[100,0], [75,25], [50,50], [25,75], [0,100]], self.np),
                    'goblin_rogue': from_node_power([[0,0], [50,75], [75, 150], [100, 225], [75, 300], [50, 375], [0, 450]], self.np),
                    'mega_goblin_rogue': from_node_power([[0,0], [25, 500], [50, 1000], [100, 2500]], self.np),
                    'mini_goblin_mage': from_node_power([[100,0], [75,25], [50,50], [25,75], [0,100]], self.np),
                    'goblin_mage': from_node_power([[0,0], [50,75], [75, 150], [100, 225], [75, 300], [50, 375], [0, 450]], self.np),
                    'mega_goblin_mage': from_node_power([[0,0], [25, 500], [50, 1000], [100, 2500]], self.np),
                    'mini_goblin_shaman': from_node_power([[100,0], [75,25], [50,50], [25,75], [0,100]], self.np),
                    'goblin_shaman': from_node_power([[0,0], [50,75], [75, 150], [100, 225], [75, 300], [50, 375], [0, 450]], self.np),
                    'mega_goblin_shaman': from_node_power([[0,0], [25, 500], [50, 1000], [100, 2500]], self.np)
                    })
        return g
        
        
        
        