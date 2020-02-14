import tcod as libtcod
from entity import Entity
from render_functions import RenderOrder
from random import randint
from builders.random_item_maker import Director, EquippableBuilder
from builders.mob_builder import MobDirector, MobBuilder
from game_messages import Message
from equipment_slots import EquipmentSlots
from map_objects.tile import Tile
from map_objects.rectangle import Rect
from map_objects.lloydarray import LloydArray
from components.ai import BasicMonster
from components.item import Item
from components.useable import Useable
from components.stairs import Stairs
from components.attributes import Attributes
from components.combatant import Combatant
from components.equipment import Equipment
from components.equippable import Equippable
from components.inventory import Inventory
from components.equippable_core import EquippableCore
from components.equippable_material import EquippableMaterial
from components.equippable_quality import EquippableQuality
from components.level import Level
from components.competence import Competence, Strength, Instinct, Coordination, Vitality, Arcana, Improvisation, Wisdom, Finesse, Charisma, Devotion
from components.shopkeeper import ShopKeeper
from random_utils import random_choice_from_dict, from_dungeon_level
from item_functions import heal, cast_lightning, cast_fireball, cast_confuse





class GameMap:
    
    def __init__(self, current_map):
        
        self.current_map = current_map
    @property    
    def width(self):
        return self.current_map.width
    @property
    def height(self):
        return self.current_map.height
    
    @property    
    def tiles(self):
        return self.current_map.tiles
    @property    
    def dungeon_level(self):
        return self.current_map.dungeon_level
        
        
    def is_blocked(self, x, y):
        if self.current_map.tiles[x][y].blocked:
            return True
            
        return False
        
               
    
    def set_current_map(self, new_map):
        self.current_map = new_map
        

    
        

                    
       

        
