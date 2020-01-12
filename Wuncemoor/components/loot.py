import tcod as libtcod
from random_utils import random_choice_from_dict


class Loot:
    
    def __init__(self, mob):
        self.mob = mob
        
    loot = []
    
    if mob = orc:
        loot_chances = {
            'healing potion' : 50,
            'NULL' : 50
            }
    elif mob = troll:
        loot_chances = {
            'healing potion' : 40,
            'lightning_scroll' : 40,
            'NULL' : 20
            }
    loot_choice = random_choice_from_dict(loot_chances)
    loot.append[loot_choice]
        