import tcod as libtcod
from random import randint
from components.attributes import Attributes
from components.ai import BasicMonster
from components.combatant import Combatant
from entity import Entity
from render_functions import RenderOrder
from random_utils import random_choice_from_dict, from_dungeon_level

def orc():
    name = 'Orc'
    attribute_component = Attributes(5,0,0,7,10,10,10,10,10,10)
    combatant_component = Combatant(attribute_component, xp=350 )
    ai_component = BasicMonster()
    loot_component = Loot(orc)
    return name, attribute_component, combatant_component, ai_component
    
def troll():
    name = 'Troll'
    attribute_component = Attributes(1,0,0,10,10,10,10,10,10,10)
    combatant_component = Combatant(attribute_component, xp=1000)
    ai_component = BasicMonster()
    loot_component = Loot(troll)
    return name, attribute_component, combatant_component, ai_component