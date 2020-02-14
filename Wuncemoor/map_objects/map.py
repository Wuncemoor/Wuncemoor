import tcod as libtcod

from entity import Entity
from equipment_slots import EquipmentSlots
from game_messages import Message
from item_functions import heal, cast_lightning, cast_fireball, cast_confuse
from random import randint
from random_utils import random_choice_from_dict, from_dungeon_level
from render_functions import RenderOrder

from builders.random_item_maker import Director, EquippableBuilder
from builders.mob_builder import MobDirector, MobBuilder
from components.equippable import Equippable
from components.equippable_core import EquippableCore
from components.equippable_material import EquippableMaterial
from components.equippable_quality import EquippableQuality
from components.item import Item
from components.stairs import Stairs
from components.useable import Useable
from map_objects.rectangle import Rect
from map_objects.tile import Tile



class Map:
    
    def __init__(self, width, height, tiles, map_entities, dungeon_level=0):
        
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()
        self.dungeon_level = dungeon_level
        self.map_entities = self.initialize_entities()
        self.entrance = None
        self.exit = None
        
    def initialize_tiles(self):
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]
        return tiles
        
    def initialize_entities(self):
        entities = []
        return entities
    
    def set_dungeon_level(self, level):
        self.dungeon_level = level
        
    def create_room(self, room):
        #go through the tiles in the rectangle and make them not blocked
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False
                
    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False
        
    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) +1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    #Create everything except stairs
    def fill_map(self, max_rooms, room_min_size, room_max_size, map_width, map_height):
        rooms = []
        num_rooms = 0
        center_of_last_room_x = None
        center_of_last_room_y = None
        
        for r in range(max_rooms):
            w = randint(room_min_size, room_max_size)
            h = randint(room_min_size, room_max_size)
            #random posiition without going out of boundaries of the map
            x = randint(0, map_width - w - 1)
            y = randint(0, map_height - h - 1)
            #Rect class makes rectangless easier to work  with
            new_room = Rect(x, y, w, h)
            for other_room in rooms:
                if new_room.intersect(other_room):
                    break
            else:
                #No intersections, ergo valid room
                #"paint" to map's tiles
                self.create_room(new_room)
                #center coordinates of new room, useful later
                (new_x, new_y) = new_room.center()
                center_of_last_room_x = new_x
                center_of_last_room_y = new_y
                     
                if num_rooms == 0:
                #First room, where player starts
                    self.entrance = (new_x, new_y)

                else:
                #all rooms after first
                #connect it to previous room with a tunnel
                #center of previous room
                    (prev_x, prev_y) = rooms[num_rooms - 1].center()
                #flip a coin
                    if randint(0,1) == 1:
                    #first horizontal, then vertical
                        self.create_h_tunnel(prev_x, new_x, prev_y)
                        self.create_v_tunnel(prev_y, new_y, new_x)
                    else:
                    #first vertical, then horizontal
                        self.create_v_tunnel(prev_y, new_y, prev_x)
                        self.create_h_tunnel(prev_x, new_x, new_y)
                #append room to list
                self.place_entities(new_room)
                rooms.append(new_room)
                self.exit = (center_of_last_room_x, center_of_last_room_y)
                num_rooms += 1
        
        #upstairs_component = Stairs('Stairs Up', '<', 'start', (40, 40), floor = 1)
        #up_stairs = Entity(self.entrance[0], self.entrance[1], libtcod.white, render_order=RenderOrder.STAIRS, stairs=upstairs_component)
        
        #downstairs_component = Stairs('Stairs Down', '>', self.dungeon_level + 1)
        #down_stairs = Entity(center_of_last_room_x, center_of_last_room_y, libtcod.white, render_order=RenderOrder.STAIRS, stairs=downstairs_component)
        #self.map_entities.append(up_stairs)

    def place_entities(self, room):
        #Get random number of monsters
        number_of_monsters = from_dungeon_level([[2,1], [3,4], [5,6]], self.dungeon_level)
        
        number_of_items = from_dungeon_level([[1, 1], [2, 4]], self.dungeon_level)

        monster_chances = { 
            'orc' : 80, 
            'troll': from_dungeon_level([[20,1], [40,2], [80,3]], self.dungeon_level)
            }
        
        item_chances = {
            'healing_potion' : 35,
            'sword': from_dungeon_level([[15,2]], self.dungeon_level),
            'shield': from_dungeon_level([[15, 2]], self.dungeon_level),
            'lightning_scroll': from_dungeon_level([[25,2]], self.dungeon_level),
            'fireball_scroll': from_dungeon_level([[25,2]], self.dungeon_level),
            'confusion_scroll': from_dungeon_level([[10,2]], self.dungeon_level)
            }
            
        for i in range(number_of_monsters):
            #choose location in room
            x = randint(room.x1 +1, room.x2 -1)
            y = randint(room.y1 +1, room.y2 -1)
            
            if not any([entity for entity in self.map_entities if entity.x == x and entity.y == y]):
                monster_choice = random_choice_from_dict(monster_chances)
                mob_builder = MobBuilder(0,monster_choice)
                mob_director = MobDirector()
                mob_director.set_builder(mob_builder)
                combatant_component = mob_director.get_combatant()
                monster = Entity(x, y, libtcod.desaturated_green, blocks=True, render_order=RenderOrder.ACTOR, combatant=combatant_component)
                    
                self.map_entities.append(monster)
                     
        for i in range(number_of_items):
            x = randint(room.x1 + 1, room.x2 -1)
            y = randint(room.y1 + 1, room.y2 -1)
            
            if not any([entity for entity in self.map_entities if entity.x == x and entity.y == y]):
                item_choice = random_choice_from_dict(item_chances)
                
                
                if item_choice == 'healing_potion':
                    item_component = Item(useable_component=Useable('Healing Potion', '!', use_function=heal, amount=400))
                    item = Entity(x, y, libtcod.violet, render_order=RenderOrder.ITEM, item=item_component)
                elif item_choice == 'sword':
                    equippable_core = EquippableCore('longsword')
                    equippable_material = EquippableMaterial('wood')
                    equippable_quality = EquippableQuality('average')
                    equippable_component = Equippable('Sword', '/', EquipmentSlots.MAIN_HAND, equippable_core, equippable_material, equippable_quality)
                    item_component = Item(equippable_component)
                    item = Entity(x, y, libtcod.sky, item=item_component)
                elif item_choice == 'shield':
                    equippable_core = EquippableCore('shield')
                    equippable_material = EquippableMaterial('iron')
                    equippable_quality = EquippableQuality('average')
                    equippable_component = Equippable('Shield', '[', EquipmentSlots.OFF_HAND, equippable_core, equippable_material, equippable_quality)
                    item_component = Item(equippable_component)
                    item = Entity(x, y, libtcod.darker_orange, item=item_component)
                elif item_choice == 'fireball_scroll':
                    item_component = Item(useable_component=Useable('Fireball Scroll', '#', use_function=cast_fireball, targeting = True, targeting_message=Message('Left-click a target tile for the fireball, or right-click to rethink your life decisions.', libtcod.light_cyan), damage=250, radius=3))
                    item = Entity(x, y, libtcod.red, render_order=RenderOrder.ITEM, item=item_component)
                elif item_choice == 'confusion_scroll':
                    item_component = Item(useable_component=Useable('Confusion Scroll', '#', use_function=cast_confuse, targeting=True, targeting_message=Message('Left-click an enemy to confuse it, or right-click to cancel.', libtcod.light_cyan)))
                    item = Entity(x, y, libtcod.light_pink, render_order=RenderOrder.ITEM, item=item_component)
                elif item_choice == 'lightning_scroll':
                    item_component = Item(useable_component=Useable('Lightning Scroll', '#', use_function = cast_lightning, damage=400, maximum_range=5))
                    item = Entity(x, y, libtcod.yellow, render_order=RenderOrder.ITEM, item=item_component)
                    
                self.map_entities.append(item)
                    
